param(
    [ValidateSet('auto','zh','en')][string]$Language = 'auto',
    [double]$InitialSilenceSeconds = 10,
    [double]$EndSilenceSeconds = 1,
    [string]$WavePath,
    [string]$InputWave,
    [switch]$InfoOnly
)
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Add-Type -AssemblyName System.Speech
$available = @([System.Speech.Recognition.SpeechRecognitionEngine]::InstalledRecognizers())
if ($InfoOnly) {
    $rows = @($available | ForEach-Object { @{ id = $_.Id; language = $_.Culture.Name; name = $_.Name } })
    @{ recognizers = $rows } | ConvertTo-Json -Depth 5 -Compress
    exit 0
}
if ($Language -eq 'auto') {
    $Language = [System.Globalization.CultureInfo]::CurrentUICulture.TwoLetterISOLanguageName
    if ($Language -notin @('zh','en')) { $Language = 'en' }
}
$info = $available | Where-Object { $_.Culture.TwoLetterISOLanguageName -eq $Language } | Select-Object -First 1
if ($null -eq $info) {
    [Console]::Error.WriteLine('Requested speech recognizer is not installed.')
    exit 13
}
$recognizer = New-Object System.Speech.Recognition.SpeechRecognitionEngine($info)
try {
    $recognizer.InitialSilenceTimeout = [TimeSpan]::FromSeconds($InitialSilenceSeconds)
    $recognizer.BabbleTimeout = [TimeSpan]::FromSeconds(10)
    $recognizer.EndSilenceTimeout = [TimeSpan]::FromSeconds($EndSilenceSeconds)
    $recognizer.EndSilenceTimeoutAmbiguous = [TimeSpan]::FromSeconds($EndSilenceSeconds)
    $recognizer.LoadGrammar((New-Object System.Speech.Recognition.DictationGrammar))
    # Command phrases are decoded from ASCII JSON, avoiding Windows PowerShell source-encoding issues.
    $phrases = if ($Language -eq 'zh') {
        ConvertFrom-Json '["\u9000\u51fa\u5bf9\u8bdd","\u7ed3\u675f\u5bf9\u8bdd","\u5207\u6362\u82f1\u6587","\u5207\u6362\u4e2d\u6587","\u6e05\u7a7a\u4e0a\u4e0b\u6587"]'
    } else { @('exit', 'quit', 'goodbye', 'switch to Chinese', 'switch to English') }
    $choices = New-Object System.Speech.Recognition.Choices
    foreach ($phrase in $phrases) { $choices.Add([string]$phrase) }
    $builder = New-Object System.Speech.Recognition.GrammarBuilder
    $builder.Culture = $info.Culture
    $builder.Append($choices)
    $commands = New-Object System.Speech.Recognition.Grammar($builder)
    $commands.Name = 'session_commands'
    $recognizer.LoadGrammar($commands)
    if ($InputWave) {
        $recognizer.SetInputToWaveFile($InputWave)
    } else {
        try { $recognizer.SetInputToDefaultAudioDevice() }
        catch {
            [Console]::Error.WriteLine('Cannot open the default microphone.')
            exit 14
        }
    }
    $result = $recognizer.Recognize([TimeSpan]::FromSeconds($InitialSilenceSeconds))
    if ($null -eq $result) {
        @{ status = 'no_speech'; text = ''; confidence = 0.0; language = $info.Culture.Name } | ConvertTo-Json -Compress
    } else {
        $audioFile = $null
        if ($WavePath -and $null -ne $result.Audio) {
            $stream = [System.IO.File]::Open($WavePath, [System.IO.FileMode]::CreateNew)
            try { $result.Audio.WriteToWaveStream($stream) } finally { $stream.Dispose() }
            $audioFile = $WavePath
        }
        @{ status = 'recognized'; text = $result.Text; confidence = [double]$result.Confidence;
           language = $info.Culture.Name; recognizer_id = $info.Id; input_audio = $audioFile;
           audio_duration_s = $(if ($null -ne $result.Audio) { $result.Audio.Duration.TotalSeconds } else { $null })
        } | ConvertTo-Json -Depth 5 -Compress
    }
} finally {
    $recognizer.Dispose()
}
