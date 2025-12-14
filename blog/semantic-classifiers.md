---
title: "How to Build a Semantic Intent Classifier Without Training a Model"
date: 2025-12-13
author: Gary Sharpe
tags: [nlp, machine-learning, embeddings, intent-classification]
---

import { Reference, References } from '@site/src/components/Reference';

While building some of my first agentic workflows, I quickly realized the importance of taking ownership of the control flow. With it you can impose structure, reliability, safety, and governance on systems that are fundamentally designed to maximize autonomy while producing non-deterministic but measurable results. 

Typical control flow components are too rigid and brittle, though, and rob your workflows of the agency you envisioned at the start.

Semantic classifiers provide a means to understand the user's intent and help 'guide' the conversation.

## Understanding Semantic Classification

Semantic classification focuses on meaning, not just keywords.

**Example:**
```
"I need to catch a flight to Madrid tomorrow."
"Can you book me a ticket to Spain?"
```

These two sentences have different words but the same intent: `BookFlight`.

Keyword or regex-based systems would miss that connection, but semantic models capture it naturally using embeddings - high-dimensional representations of meaning.

### Vector Embeddings as Control Flow Components 

As Masood noted [1], embeddings have become core infrastructure for many systems. They're no longer niche research tools - they power search engines, recommendation systems, and conversational AI pipelines. Now, because modern embedding models are increasingly compact, available and optimized for domain specific--even multilingual usage--smaller models can be easily deployed within or alongside an application.  Easily accessible, these models can be used to power critical components, even trivial control flow, including the nodes in conversational agentic AI applications.

## Two Approaches to Training-Free Classification

There are two fundamentally different ways to build intent classifiers without training:

**1. Zero-Shot Classification** - The model interprets your label names and decides which one best matches the input. You just provide label strings like `"BookFlight"` or `"WeatherInfo"`, and the model uses its built-in language understanding to classify. No examples needed.

**2. Embedding Similarity** - You provide a few example phrases for each intent, and the system finds which example set is most semantically similar to the input. This requires you to define what each intent "looks like" with examples.

The trade-off is flexibility vs. control: zero-shot works with any labels you dream up, while embedding similarity requires examples but gives you more control over what matches what.

Let's explore both approaches.

## Zero-Shot Classification: Let the Model Decide

Large pretrained models can classify text into categories they've never been explicitly trained on, a technique known as **zero-shot classification**.

### How Zero-Shot Works

Zero-shot classifiers are typically trained on Natural Language Inference (NLI) tasks, where they learn to determine if one sentence entails, contradicts, or is neutral to another. At inference time, they reframe classification as: "Does the input text entail the hypothesis 'This is about [LABEL]'?"

The quality of zero-shot classification varies significantly based on:

**Model Selection:**

There are three main options for deploying zero-shot classifiers:

**1. Local Models (Recommended for privacy & reliability)**
- **Large (Best accuracy, highest resource use):** `facebook/bart-large-mnli` - 400M params, ~1.3 GB on disk, excellent ~92% accuracy, requires 6-8 GB RAM when loaded
- **Medium (Good balance):** `MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli` - 184M params, ~700 MB on disk, ~90% accuracy, needs 4-6 GB RAM
- **Small (Lightweight, still accurate):** `cross-encoder/nli-deberta-v3-small` - 44M params, ~180 MB on disk, ~88% accuracy, works with 2-3 GB RAM

**2. Remote APIs (Zero local resource overhead)**
- **OpenAI GPT-4o:** Extremely flexible, handles reasoning and context. Cost: ~$0.03/1K tokens. No model download needed, pay-per-use.
- **Anthropic Claude:** Similar capabilities to GPT-4. Cost varies by model. Good for complex intent reasoning.
- **Hugging Face Inference API:** Provides on-demand access to many models without hosting. Smaller latency than local GPU, predictable costs.

**3. Hybrid Approach (Best of both)**
- Cache infrequent intents via API, keep common ones locally
- Use local model for quick classification, escalate uncertain cases to a more powerful model

**Model Selection Guidance:**
- **For production with privacy concerns:** Use local small/medium models
- **For maximum accuracy and flexibility:** Use local large models or remote APIs
- **For mobile/edge deployment:** Use small models or remote APIs
- **For prototyping:** Start with either local large model or free API tier

**Label Design:**
- **Better:** Descriptive labels that match natural language: `"booking a flight"`, `"weather information"`, `"casual conversation"`
- **Worse:** Cryptic abbreviations: `"BF"`, `"WI"`, `"SC"`
- **Critical:** Keep the number of candidate labels reasonable (typically 3-10). Too many degrades performance.

**LLM-Based Zero-Shot:**
You can also use chat models like GPT-4, Claude, or Llama via API calls or local inference. These can be prompted with instructions and examples (few-shot) or just instructions (pure zero-shot). Trade-offs:
- **Pros:** Extremely flexible, can handle complex reasoning, natural language instructions
- **Cons:** Requires API calls (cost, latency, data privacy) or large local models (8B+ parameters)

Here's an example using the `facebook/bart-large-mnli` model (large local variant):

```python
from transformers import pipeline

# Local model - downloads on first run, then cached
classifier = pipeline(
    "zero-shot-classification", model="facebook/bart-large-mnli"
)

result = classifier(
    "Book me a flight to Tokyo",
    candidate_labels=["BookFlight", "WeatherInfo", "SmallTalk"]
)

print(result)
```

For a smaller footprint, swap the model:

```python
# Lightweight local version
classifier = pipeline(
    "zero-shot-classification", 
    model="cross-encoder/nli-deberta-v3-small"  # Only 180MB
)
```

Or use a remote API:

```python
# Using OpenAI's API (requires API key)
import openai

client = openai.OpenAI(api_key="your-key-here")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "system",
        "content": "You are a classification assistant. Classify the user message as one of: BookFlight, WeatherInfo, SmallTalk",
        "role": "user",
        "content": "Book me a flight to Tokyo"
    }]
)

intent = response.choices[0].message.content
```

[Download complete working example →](https://gmsharpe.github.io/examples/semantic-classifiers/zero_shot.py)

You'll get probabilities for each intent, and you can pick the top-scoring one. This approach works surprisingly well for generic intents and requires no dataset or fine-tuning.

**Pros:**
- Excellent accuracy (≈90%) with proper model and label choices
- Works out of the box, no examples or training needed
- Can handle novel intent categories immediately
- You can download and host the model locally (i.e., in your own application codebase or service) rather than relying on a remote API
- Standard‑hardware (desktop/server) setups with sufficient RAM (say 4–16 GB) can load and run it
- For prototyping or batch classification the convenience is high

**Cons:**
- **Model size (200MB-1.3 GB):** Larger than embedding models. The memory footprint when loaded (plus tokenizer, buffers, intermediate activations) will likely be multiple gigabytes of RAM or VRAM if using GPU. On embedded devices (mobile, IoT, edge with low memory), even small NLI models may be too large
- **Slower than lightweight options:** In latency‑sensitive or cost‑sensitive production settings you may prefer embedding similarity approaches
- If you expect many concurrent inferences, resource usage becomes non‑trivial (CPU cycles, memory bandwidth)
- Quality depends heavily on label wording and model selection

## Embedding Similarity: Example-Based Classification

If zero-shot feels too "magical" or you want more control, embedding similarity offers a different paradigm: **you define what each intent looks like by providing examples**.

Instead of relying on the model to interpret label names, you encode both your example phrases and user input into numerical vectors, then find which example set is most similar using cosine similarity.

This approach requires smaller, faster models and typically uses less resources than zero-shot. The trade-off is that you need good example phrases, and the system won't generalize to completely new intent types without adding examples for them.

There are several embedding approaches available, each with different accuracy and resource trade-offs. Let's explore them from highest to lowest accuracy.

### High Accuracy: Transformer-Based Embeddings

SentenceTransformers provides state-of-the-art semantic embeddings with excellent accuracy while remaining relatively lightweight.

**Example with SentenceTransformers:**

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

intents = {
    "BookFlight": ["book a flight", "find me tickets"],
    "WeatherInfo": ["what's the weather", "is it raining"],
}

intent_embeddings = {k: model.encode(v) for k, v in intents.items()}

def classify(text):
    v = model.encode(text)
    scores = {k: max(util.cos_sim(v, e).item() for e in emb)
              for k, emb in intent_embeddings.items()}
    return max(scores, key=scores.get)

print(classify("Is it going to rain in Berlin?"))
```

[Download complete working example →](https://gmsharpe.github.io/examples/semantic-classifiers/sentence_transformers.py)

This approach is fast, offline-capable, and typically reaches 85–90% accuracy - close to heavy zero-shot models but much more efficient.

**Pros:**
- Excellent semantic understanding (85–90% accuracy)
- Runs locally, no API calls
- Lightweight (~60 MB model)
- Easy to add or modify intents

**Cons:**
- Needs good example phrases per intent
- Doesn't generalize to unseen intents

### Balanced Approach: spaCy Word Vectors

spaCy offers a middle ground with good accuracy and the benefit of integrating with other NLP tasks like entity recognition and parsing.

**Example with spaCy:**

```python
import spacy

nlp = spacy.load("en_core_web_md")

intents = {
    "BookFlight": ["book a flight", "flight schedule"],
    "WeatherInfo": ["weather today", "is it raining"]
}

def classify(text):
    doc = nlp(text)
    scores = {intent: max(doc.similarity(nlp(ex)) for ex in examples)
              for intent, examples in intents.items()}
    return max(scores, key=scores.get)
```

[Download complete working example →](https://gmsharpe.github.io/examples/semantic-classifiers/spacy_similarity.py)

**Pros:**
- Good accuracy (75–80%)
- Integrates with other NLP tasks (NER, POS tagging, parsing)
- Moderate model size (~50 MB for `en_core_web_md`)
- Simple API

**Cons:**
- Lower semantic understanding than transformer models
- Requires downloading language models

[Learn more in the spaCy documentation](https://spacy.io/usage/linguistic-features#vectors-similarity).

### Ultra-Lightweight: FastText

For resource-constrained environments where speed and size are critical, FastText offers the smallest footprint with acceptable accuracy for well-defined domains.

**Example with FastText:**

```python
import fasttext
import numpy as np

# Load pretrained FastText model (download from fasttext.cc)
model = fasttext.load_model('cc.en.300.bin')

intents = {
    "BookFlight": ["book a flight", "find me tickets", "flight schedule"],
    "WeatherInfo": ["weather today", "is it raining", "temperature forecast"]
}

def get_phrase_vector(phrase):
    words = phrase.split()
    vectors = [model.get_word_vector(word) for word in words]
    return np.mean(vectors, axis=0)

# Compute intent embeddings
intent_vectors = {
    intent: [get_phrase_vector(ex) for ex in examples]
    for intent, examples in intents.items()
}

def classify(text):
    text_vec = get_phrase_vector(text)
    scores = {}
    for intent, examples in intent_vectors.items():
        # Calculate cosine similarity with each example
        similarities = [
            np.dot(text_vec, ex) / (np.linalg.norm(text_vec) * np.linalg.norm(ex))
            for ex in examples
        ]
        scores[intent] = max(similarities)
    return max(scores, key=scores.get)

print(classify("Book me a ticket to Paris"))  # Output: BookFlight
```

[Download complete working example →](https://gmsharpe.github.io/examples/semantic-classifiers/fasttext_similarity.py)

**Pros:**
- Extremely fast inference, even on CPUs
- Smallest footprint (under 200 MB, quantized versions available)
- Works offline, no API calls
- Simple implementation

**Cons:**
- Lower accuracy (60–70%) compared to transformer models
- Word-level embeddings don't capture sentence-level semantics as well
- Best for domains with predictable, constrained vocabulary

[Download pretrained models from fasttext.cc](https://fasttext.cc/).

## Choosing the Right Approach

**Quick decision matrix:**

### Zero-Shot Options (No Examples Required)

**Zero-Shot: Large Local Model (BART)**
- Accuracy: ~92%
- Model size: ~1.3 GB (6-8 GB RAM when loaded)
- Speed: Slower (100-500ms per inference)
- Use when: Maximum accuracy needed, privacy critical, stable intents
- Deployment: Self-hosted, offline
- Tradeoff: Highest resource use

**Zero-Shot: Medium Local Model (DeBERTa-v3-base)**
- Accuracy: ~90%
- Model size: ~700 MB (4-6 GB RAM when loaded)
- Speed: Moderate (50-200ms per inference)
- Use when: Good accuracy/resource balance, privacy important
- Deployment: Self-hosted, offline
- Recommendation: Often the best choice for production systems
- Tradeoff: More resources than SentenceTransformers but more flexible

**Zero-Shot: Small Local Model (DeBERTa-v3-small)**
- Accuracy: ~88%
- Model size: ~180 MB (2-3 GB RAM when loaded)
- Speed: Fast (30-100ms per inference)
- Use when: Limited resources, still need high accuracy
- Deployment: Self-hosted, offline
- Tradeoff: Slightly lower accuracy than large models

**Zero-Shot: Remote API (OpenAI, Claude, Hugging Face)**
- Accuracy: 92-95%+ (depends on model)
- Model size: Zero local overhead
- Speed: Slower (200ms-1s per inference, includes network latency)
- Use when: Maximum flexibility, complex reasoning needed, no privacy concerns
- Deployment: Cloud-based, pay-per-use
- Cost: $0.01-0.10 per classification
- Tradeoff: Ongoing costs, internet dependency, data privacy

### Embedding-Based Options (Require Examples)

**SentenceTransformers (MiniLM)**
- Accuracy: 85-90%
- Model size: ~60 MB
- Speed: Fast (10-50ms per inference)
- Use when: Production systems, good accuracy/resource balance, need examples for control
- Deployment: Self-hosted, offline
- Recommendation: Best overall choice for most production use cases
- Tradeoff: Requires examples to define intent boundaries

**spaCy (Word Vectors)**
- Accuracy: 75-80%
- Model size: ~50 MB
- Speed: Fast (5-20ms per inference)
- Use when: Already using spaCy for other NLP tasks, need entity recognition alongside classification
- Deployment: Self-hosted, offline
- Tradeoff: Lower accuracy than transformers, limited semantic understanding

**FastText (Pretrained Embeddings)**
- Accuracy: 60-70%
- Model size: Under 200 MB (quantized: under 50 MB)
- Speed: Fastest (&lt;5ms per inference)
- Use when: Edge devices, mobile apps, severely resource-constrained environments
- Deployment: Self-hosted, offline
- Tradeoff: Lowest accuracy, word-level semantics only

### Decision Process

1. **Maximum accuracy + no privacy concerns?** → Remote API (OpenAI/Claude) if budget allows
2. **Need high accuracy (90%+) with privacy?** → Zero-Shot medium/large local model or SentenceTransformers
3. **Want to define boundaries with examples?** → SentenceTransformers (best accuracy/resource) or FastText (most lightweight)
4. **Already using spaCy?** → spaCy for integration benefits
5. **Severe resource constraints?** → FastText or Zero-Shot small model
6. **Frequently changing intents?** → Zero-Shot (any size) for maximum flexibility
7. **Best overall production balance?** → SentenceTransformers or Zero-Shot medium local model

### Tips for Improving Accuracy

- Use multiple example phrases per intent to cover paraphrases and variations
- Consider a hybrid approach: first do nearest-neighbor embedding matching, then optionally pass the top candidate to a small reasoning or zero-shot model to disambiguate
- Use a similarity threshold and fallback mechanism: if the match is too weak, ask the user for clarification rather than guessing
- Test your approach on representative user inputs before deployment

## Complete Working Examples

All code examples from this article are available as runnable Python scripts:

- [View all examples on GitHub](https://github.com/gmsharpe/gmsharpe.github.io/tree/main/static/examples/semantic-classifiers)
- [Download zero_shot.py](/examples/semantic-classifiers/zero_shot.py) - Zero-shot classification with BART
- [Download sentence_transformers.py](/examples/semantic-classifiers/sentence_transformers.py) - High-accuracy embeddings
- [Download spacy_similarity.py](/examples/semantic-classifiers/spacy_similarity.py) - Balanced spaCy approach
- [Download fasttext_similarity.py](/examples/semantic-classifiers/fasttext_similarity.py) - Ultra-lightweight FastText
- [Download requirements.txt](/examples/semantic-classifiers/requirements.txt) - Python dependencies
- [Setup instructions](/examples/semantic-classifiers/README.md)

## Conclusion

Building a semantic intent classifier no longer requires training custom models or managing labeled datasets. With pretrained models and embeddings, you can:

- Deploy zero-shot classifiers that work out of the box with 90% accuracy
- Use lightweight embedding models (60–200 MB) that run locally and offline
- Choose the right accuracy/resource trade-off for your use case
- Implement production-ready classifiers in under 20 lines of code

Whether you're building agentic workflows, chatbots, or smart routing systems, these training-free approaches provide the semantic understanding you need without the overhead of maintaining ML pipelines.

Start with the approach that fits your constraints, and remember: you can always combine methods (e.g., FastText for initial filtering, then SentenceTransformers for final classification) to balance speed and accuracy.

<References>
  <Reference 
    number={1}
    author="A. Masood"
    title="The State of Embedding Technologies for Large Language Models: Trends, Taxonomies, Benchmarks and Best Practices"
    publication="Medium"
    year="2025"
    url="https://medium.com/@adnanmasood/the-state-of-embedding-technologies-for-large-language-models-trends-taxonomies-benchmarks-and-95e5ec303f67"
  />
  <Reference 
    number={2}
    author="Hugging Face"
    title="Zero-Shot Classification"
    url="https://huggingface.co/tasks/zero-shot-classification"
  />
  <Reference 
    number={3}
    author="Sentence-Transformers"
    title="Pretrained Models Documentation"
    url="https://www.sbert.net/docs/pretrained_models.html"
  />
  <Reference 
    number={4}
    author="spaCy"
    title="Similarity and Word Vectors"
    url="https://spacy.io/usage/linguistic-features#vectors-similarity"
  />
  <Reference 
    number={5}
    author="Facebook Research"
    title="FastText: Library for Text Classification and Representation"
    url="https://fasttext.cc/"
  />
</References>

