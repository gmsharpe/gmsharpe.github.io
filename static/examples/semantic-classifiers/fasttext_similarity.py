"""
FastText Intent Classification
Uses pretrained FastText embeddings for semantic similarity.

Note: Download the pretrained model first from https://fasttext.cc/docs/en/crawl-vectors.html
  wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.en.300.bin.gz
  gunzip cc.en.300.bin.gz

For this example to work, place cc.en.300.bin in the same directory.
"""

import fasttext
import numpy as np

# Load pretrained FastText model
# Download from: https://fasttext.cc/docs/en/crawl-vectors.html
model = fasttext.load_model('cc.en.300.bin')

# Define intents with example phrases
intents = {
    "BookFlight": ["book a flight", "find me tickets", "flight schedule"],
    "WeatherInfo": ["weather today", "is it raining", "temperature forecast"],
    "SmallTalk": ["how are you", "hello there", "good morning"]
}

def get_phrase_vector(phrase):
    """Get averaged word vector for a phrase."""
    words = phrase.split()
    vectors = [model.get_word_vector(word) for word in words]
    return np.mean(vectors, axis=0)

# Precompute intent embeddings
intent_vectors = {
    intent: [get_phrase_vector(ex) for ex in examples]
    for intent, examples in intents.items()
}

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors."""
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def classify(text):
    """Classify text based on similarity to intent examples."""
    text_vec = get_phrase_vector(text)
    
    scores = {}
    for intent, examples in intent_vectors.items():
        # Calculate cosine similarity with each example
        similarities = [
            cosine_similarity(text_vec, ex)
            for ex in examples
        ]
        scores[intent] = max(similarities)
    
    # Return intent with highest score
    best_intent = max(scores, key=scores.get)
    return best_intent, scores

# Test examples
test_inputs = [
    "Book me a flight to Tokyo",
    "What's the weather like today?",
    "How are you doing?",
    "I need tickets to Paris tomorrow",
    "Is it going to rain this weekend?"
]

print("FastText Similarity Classification Results\n" + "="*50)

for text in test_inputs:
    intent, scores = classify(text)
    
    print(f"\nInput: {text}")
    print(f"Predicted: {intent}")
    print(f"Confidence: {scores[intent]:.2%}")
    print("All scores:")
    for label, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"  {label}: {score:.2%}")
