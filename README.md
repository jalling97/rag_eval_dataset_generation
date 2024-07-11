# rag_eval_dataset_generation
Tests and Experiments for generating qa datasets for RAG-focused task evaluations

## Install Dependencies
Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

Install the dependencies:
```bash
python -m pip install -r requirements
```

## Usage

### Downloading Documents
Run the following bash script to download the pre-selected documents
```bash
./fetch_documents.sh
```

### Generating Datasets
The following script uses DeepEval's [Synthesizer](https://docs.confident-ai.com/docs/evaluation-datasets-synthetic-data) to generate evaluation datasets that are focused on RAG use-cases.

```
usage: Synthetic Dataset Generator [-h] -f FILES [FILES ...] [-c COUNT]

Uses a list of documents to generate question-answer pairs for RAG evaluations

options:
  -h, --help            show this help message and exit
  -f FILES [FILES ...], --files FILES [FILES ...]
  -c COUNT, --count COUNT
```

Run the script using the downloaded documents as a contextual basis:

```bash
python test_generate.py -f documents/*.pdf
```