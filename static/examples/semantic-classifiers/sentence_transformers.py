"""
Sentence Transformers Intent Classification
Uses semantic similarity with transformer-based embeddings.
"""

from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Define intents with example phrases
intents = {
    "BookFlight": ["book a flight", "find me tickets", "I need to fly"],
    "WeatherInfo": ["what's the weather", "is it raining", "temperature today"],
    "SmallTalk": ["how are you", "hello", "good morning"]
}

# Encode all example phrases
intent_embeddings = {
    intent: model.encode(examples) 
    for intent, examples in intents.items()
}

def classify(text):
    """Classify text based on highest similarity to intent examples."""
    text_embedding = model.encode(text)
    
    scores = {}
    for intent, embeddings in intent_embeddings.items():
        # Get max similarity across all examples for this intent
        similarities = util.cos_sim(text_embedding, embeddings)
        scores[intent] = float(similarities.max())
    
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

print("Sentence Transformers Classification Results\n" + "="*50)

for text in test_inputs:
    intent, scores = classify(text)
    
    print(f"\nInput: {text}")
    print(f"Predicted: {intent}")
    print(f"Confidence: {scores[intent]:.2%}")
    print("All scores:")
    for label, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"  {label}: {score:.2%}")
