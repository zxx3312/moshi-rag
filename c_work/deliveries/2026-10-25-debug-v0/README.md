# C Group MoshiRAG Debug Delivery

## Scope
Functional pilot on B group's 20 debug-v0 questions.
This is not a formal benchmark or A group's controller evaluation.

## Completed runs
- 11675327: 20 questions without reference.
- 11760936: Apollo 11 comparison, with and without reference.
- 11761507: 20 questions with reference.

## Input handling
Questions were supplied as synthesized speech.
The reference batch used all context documents in source order.
Gold answers and supporting-fact mappings were not model inputs.
Reference injection started after the question audio file ended.
B group's progressive evidence schedules were not used.

## Preliminary findings
Text-only review found all four NASA date questions fully correct
with reference. Multi-hop responses remained unreliable.
Audio review and independent scoring are still required.

## Limitations
The no-reference batch used 15 seconds of trailing silence.
The reference batch allowed reference delivery plus 20 seconds.
These runs are not a matched timing comparison.

## Contents
Scripts, installation adjustments, logs, inputs, results, and review CSV.
file_checksums.json records hashes of the 19 copied source files.
environment.json captures the environment at packaging time.

## Reproduction notes
This is a debug snapshot, not a standalone runnable package.
Scripts retain paths to the original cluster project and model assets.
Model weights, tokenizer assets, and audio files are not included.
Audio locations in result files refer to the cluster.
A shared audio location remains to be added.

## Next work
Audio review, B interface adaptation, progressive trace replay,
matched experiments, and human evaluation.
