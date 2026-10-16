> **Note:** **The 300-question reserved evaluation set (`prepared/samples_eval_reserved.jsonl`) is included for team reproducibility and final evaluation only; it must not be used for debugging, prompt tuning, threshold selection, or policy development.**
# Prepare Question Data

This package supports the W1 milestone: 8 HotpotQA debug questions, 8 2WikiMultiHopQA debug questions, and 4 source-derived custom multipart debug questions. It also reserves 150 evaluation questions per benchmark, excluded from the debug set. These counts are implementation choices, not fixed requirements from the original proposal.

No GPU, API key, model training, or third-party Python package is needed. The script loads one official dev JSON array at a time. Raw datasets and archives remain outside Git. The 2Wiki archive contains more data than is needed immediately; the script reads only its dev.json without extracting the full archive.


## 1. Download official data

### Dataset Downloads

Run the commands below from the repository root.

### 1. HotpotQA

The original download URL was inaccessible, so use the RAGLAB mirror on
Hugging Face. This is a third-party mirror. Its published SHA256 matches
the checksum recorded in Hugging Face dataset metadata for the original
HotpotQA dev distractor file.

- **Original source:** <http://curtis.ml.cmu.edu/datasets/hotpot/hotpot_dev_distractor_v1.json>
- **Actual download source:** <https://huggingface.co/datasets/RAGLAB/data/resolve/main/eval_datasets/HotPotQA/hotpot_dev_distractor_v1.json>

Create the download directory if needed:

```bash
mkdir -p b_work/step2/raw
```

Download the file:

```bash
curl --fail --location --retry 2 \
  --output b_work/step2/raw/hotpot_dev_distractor_v1.json.part \
  'https://huggingface.co/datasets/RAGLAB/data/resolve/main/eval_datasets/HotPotQA/hotpot_dev_distractor_v1.json?download=true'
```

After the download succeeds, calculate the file's SHA256:

```bash
sha256sum b_work/step2/raw/hotpot_dev_distractor_v1.json.part
```

Expected SHA256:

```text
4e9ecb5c8d3b719f624d66b60f8d56bf227f03914f5f0753d6fa1b359d7104ea
```

**Only if the checksum matches**, rename the file:

```bash
mv b_work/step2/raw/hotpot_dev_distractor_v1.json.part \
  b_work/step2/raw/hotpot_dev_distractor_v1.json
```

### 2. 2WikiMultiHopQA

Use the April 7, 2021 package linked from the official repository,
which corrected sentence segmentation and includes the ID-based data update.

- **Download source:** <https://www.dropbox.com/s/ms2m13252h6xubs/data_ids_april7.zip?dl=1>

Download the package:

```bash
curl --fail --location --retry 2 \
  --output b_work/step2/raw/data_ids_april7.zip.part \
  'https://www.dropbox.com/s/ms2m13252h6xubs/data_ids_april7.zip?dl=1'
```

**Only after the download succeeds**, rename the file:

```bash
mv b_work/step2/raw/data_ids_april7.zip.part \
  b_work/step2/raw/data_ids_april7.zip
```

### Alternative: Browser Download

Alternatively, download these files in a browser and upload them to
`b_work/step2/raw/`. Keep the final filenames unchanged:

- `hotpot_dev_distractor_v1.json`
- `data_ids_april7.zip`

For a browser-downloaded HotpotQA file, calculate the SHA256 after uploading:

```bash
sha256sum b_work/step2/raw/hotpot_dev_distractor_v1.json
```

Compare the result with the expected checksum above before proceeding.

### Preparation and Reproducibility

The preparation script records the SHA256 of each input file.
Keep the actual download URLs in this README alongside the generated
split manifest.

**Downloading the files alone does not generate the debug or reserved
evaluation subsets.** Run `prepare_step2.py` afterward using the
arguments specified in the preparation instructions.

## 2. Run the preparation script

```bash
python3 b_work/step2/prepare_step2.py \
  --hotpot b_work/step2/raw/hotpot_dev_distractor_v1.json \
  --twowiki b_work/step2/raw/data_ids_april7.zip \
  --out b_work/step2/prepared
```

Expected counts after a successful run on the official files:

```text
hotpotqa: selected 8 debug and 150 reserved evaluation questions
2wikimultihopqa: selected 8 debug and 150 reserved evaluation questions
Debug total: 20
Reserved evaluation total: 300
```

Existing outputs are not overwritten. Do not change seeds repeatedly to choose favorable questions. Keep the first valid split manifest, or explicitly version and explain a necessary replacement.

## 3. Inspect the outputs

```bash
wc -l b_work/step2/prepared/samples_debug.jsonl
wc -l b_work/step2/prepared/samples_eval_reserved.jsonl
python3 -m json.tool b_work/step2/prepared/split_manifest.json
```

- `samples_debug.jsonl`: internal B data with answers, context, and supporting facts. Manually read all 20 questions before using them for unit annotation.
- `samples_eval_reserved.jsonl`: reserved answers/context for B's later evaluation; do not tune prompts or thresholds on these questions.
- `split_manifest.json`: seed, source hashes, split IDs, counts, exclusions, and pending work. A computed SHA256 identifies bytes, but does not claim an official checksum was verified.

The script checks source IDs, nonempty answers, supporting titles, sentence bounds, and duplicate normalized question text across the two selected splits. Sampling cycles through question types after deterministic shuffling. It logs structural exclusions before sampling. Semantic duplicates and evidence sufficiency still need human review.

For 2Wiki it preserves available `evidences`, `answer_id`, `evidences_id`, and `entity_ids`. Keep the original archive and alias table for later official scoring. Aliases may be distributed separately; never invent missing IDs or aliases.

## 4. Custom debug questions

`custom_debug.json` contains four newly composed multipart questions based on NASA primary sources: Apollo 11, Voyager 1, Perseverance, and Voyager 2. Each contains two source-derived context blocks, source URLs, short source excerpts, and a suggested answer. Context blocks are paraphrases, not original Wikipedia paragraphs. They are deliberately simple debugging cases and are not a representative final evaluation set. They remain marked for human review.

Here provides no evidence arrival schedule and no gold units yet. Keep custom multipart results separate from benchmark results.

## 5. What is still pending

The W1 milestone is complete only after the script succeeds and all 20 debug records are reviewed. The full data-preparation stage additionally requires:

1. Download the official train files, preserving source metadata and hashes.
2. Build judge-SFT training and development splits from official train. Exclude all debug/evaluation IDs and normalized question text using this manifest, including any overlap between official sources.
3. Keep every time snapshot, delay schedule, and policy run of a question in the same split.
4. Expand the custom set with diverse, documented sources; do not reuse these debug questions for final evaluation.
5. Create `samples_train.jsonl` and `samples_dev.jsonl` only when real records exist; do not create empty files and report them as completed data.

This script intentionally leaves train/dev marked pending. The reserved 300-question file is an initial benchmark evaluation reservation from official dev, not a complete final evaluation suite and not the hidden official test set.

## 7. Notice
These normalized sample records are B-internal artifacts, not ordinary model inputs. Use the Step 1 filtering rules before inference; never pass gold answers or support mappings to an ordinary policy.

## References

- [HotpotQA official repository](https://github.com/hotpotqa/hotpot): data downloads and supporting-fact format.
- [HotpotQA official homepage](https://hotpotqa.github.io/): official data links.
- [2WikiMultiHopQA official repository](https://github.com/Alab-NII/2wikimultihop): April 7 corrected package, evidence triples, IDs, and alias-based evaluation.
- Custom-question primary sources and exact short excerpts are recorded per question in `custom_debug.json`.

Validation performed: deterministic split selection, valid support indices, duplicate exclusion, missing-evidence exclusion, no output overwrite, and JSON/ZIP integrity were checked with explicitly synthetic fixtures. The preparation script was successfully run on the downloaded HotpotQA dev distractor and 2WikiMultiHopQA dev data. It generated 20 debug questions: 8 HotpotQA, 8 2WikiMultiHopQA, and 4 source-derived custom questions. It also reserved 300 separate benchmark evaluation questions, with 150 from each dataset. Source hashes and split IDs are recorded in split_manifest.json. Human review of the debug questions and train/dev preparation remain pending. No retrieval or model inference was performed in this step.
