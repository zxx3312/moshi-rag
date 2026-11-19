param(
    [Parameter(Mandatory=$true)][string]$TextPath,
    [Parameter(Mandatory=$true)][string]$WavePath,
    [ValidateSet('zh','en')][string]$Language = 'en'
)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$speaker = New-Object System.Speech.Synthesis.SpeechSynthesizer
try {
    $matchingVoice = $speaker.GetInstalledVoices() | Where-Object {
        $_.Enabled -and $_.VoiceInfo.Culture.TwoLetterISOLanguageName -eq $Language
    } | Select-Object -First 1
    if ($null -eq $matchingVoice) {
        [Console]::Error.WriteLine('No enabled Windows voice for requested language.')
        exit 12
    }
    $speaker.SelectVoice($matchingVoice.VoiceInfo.Name)
    $spokenText = [System.IO.File]::ReadAllText($TextPath, [System.Text.Encoding]::UTF8)
    $speaker.SetOutputToWaveFile($WavePath)
    $speaker.Speak($spokenText)
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    Write-Output $matchingVoice.VoiceInfo.Name
} finally {
    $speaker.Dispose()
}
