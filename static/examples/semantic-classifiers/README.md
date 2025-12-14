# Semantic Intent Classifier Examples

Working code examples from the blog post: [How to Build a Semantic Intent Classifier Without Training a Model](https://gmsharpe.github.io/blog/semantic-classifiers)

## Setup

### Install dependencies

**Using pip:**
```bash
pip install -r requirements.txt
```

**Using uv (faster):**
```bash
uv pip install -r requirements.txt
```

Or create a virtual environment with uv:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

### Additional setup for specific examples

For spaCy, also download the language model:
```bash
python -m spacy download en_core_web_md
```

For FastText, download the pretrained model:
```bash
wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.en.300.bin.gz
gunzip cc.en.300.bin.gz
```

## Examples

### Zero-Shot Classification
```bash
python zero_shot.py
```
Uses `facebook/bart-large-mnli` for zero-shot classification. No examples needed.

### Sentence Transformers
```bash
python sentence_transformers.py
```
Uses transformer-based embeddings for high-accuracy similarity matching.

### spaCy Word Vectors
```bash
python spacy_similarity.py
```
Balanced approach using spaCy's built-in word vectors.

### FastText
```bash
python fasttext_similarity.py
```
Ultra-lightweight approach using pretrained FastText embeddings.

## Comparison

| Approach | Accuracy | Model Size | Speed | Setup Complexity |
|----------|----------|------------|-------|------------------|
| Zero-Shot | ~90% | ~1.3 GB | Slower | Easy |
| SentenceTransformers | 85-90% | ~60 MB | Fast | Easy |
| spaCy | 75-80% | ~50 MB | Fast | Medium |
| FastText | 60-70% | <200 MB | Fastest | Medium (download) |

## Customization

To add your own intents, modify the `intents` dictionary in each example:

```python
intents = {
    "YourIntent": ["example phrase 1", "example phrase 2"],
    "AnotherIntent": ["different example", "another example"]
}
```

For zero-shot, just add labels to `candidate_labels`:
```python
candidate_labels = ["YourIntent", "AnotherIntent"]
```
