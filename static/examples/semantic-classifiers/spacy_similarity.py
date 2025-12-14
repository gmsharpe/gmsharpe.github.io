"""
spaCy Word Vector Intent Classification
Uses spaCy's built-in word vectors for semantic similarity.

Note: Requires downloading the model first:
  python -m spacy download en_core_web_md
"""

import spacy

# Load spaCy model with word vectors
nlp = spacy.load("en_core_web_md")

# Define intents with example phrases
intents = {
    "BookFlight": ["book a flight", "flight schedule", "I need to fly"],
    "WeatherInfo": ["weather today", "is it raining", "temperature forecast"],
    "SmallTalk": ["how are you", "hello there", "good morning"]
}

def classify(text):
    """Classify text based on similarity to intent examples."""
    doc = nlp(text)
    
    scores = {}
    for intent, examples in intents.items():
        # Get max similarity across all examples for this intent
        similarities = [doc.similarity(nlp(ex)) for ex in examples]
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

print("spaCy Similarity Classification Results\n" + "="*50)

for text in test_inputs:
    intent, scores = classify(text)
    
    print(f"\nInput: {text}")
    print(f"Predicted: {intent}")
    print(f"Confidence: {scores[intent]:.2%}")
    print("All scores:")
    for label, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"  {label}: {score:.2%}")
