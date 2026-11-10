# C group trace v1 debug delivery

Slurm job `12189299` ran 20 debug questions under three evidence schedules
(`immediate`, `short`, and `long`), for a total of 60 MoshiRAG responses.
The schedules come from B's frozen debug trace input. Its SHA-256 is
`3b50bd415ed44c5e0d20bc685a33cbfee3cebf80f234be36e6dc431850bdbf49`.

| File | Contents |
| --- | --- |
| `comparison_by_question.csv` | 20 questions with three responses side by side. |
| `trace_audit.csv` | 60 runs with generated text, evidence delivery counts, injection timing, audio duration, and source artifact paths. |
| `summary.json` | Job status, run counts, and trace and worker hashes. |

All 20 Slurm tasks completed, and all 60 runs passed execution and artifact
checks. Formal answer scoring, evidence alignment, and human listening
ratings are pending. The last injection time is measured relative to the
estimated end of the question. It describes evidence delivery in the audio
stream. Speech onset and the timing of individual spoken facts require a
separate alignment step.

The audio and per-run JSON files are located on the campus cluster. Their
paths are recorded in the audit table. Use `trace_id` to match a response
with its recording and detailed trace. The shared audio link in the earlier
debug delivery refers to that earlier experiment.
