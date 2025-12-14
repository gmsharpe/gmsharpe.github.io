"""
Zero-Shot Intent Classification
Uses facebook/bart-large-mnli for zero-shot classification without training.
"""

from transformers import pipeline

# Initialize the zero-shot classifier
classifier = pipeline(
    "zero-shot-classification", 
    model="facebook/bart-large-mnli"
)

# Define intent categories
candidate_labels = ["BookFlight", "WeatherInfo", "SmallTalk"]

# Test examples
test_inputs = [
    "Book me a flight to Tokyo",
    "What's the weather like today?",
    "How are you doing?",
    "I need tickets to Paris tomorrow",
    "Is it going to rain this weekend?"
]

print("Zero-Shot Classification Results\n" + "="*50)

for text in test_inputs:
    result = classifier(text, candidate_labels=candidate_labels)
    
    print(f"\nInput: {text}")
    print(f"Predicted: {result['labels'][0]}")
    print(f"Confidence: {result['scores'][0]:.2%}")
    
    # Show all scores
    print("All scores:")
    for label, score in zip(result['labels'], result['scores']):
        print(f"  {label}: {score:.2%}")
