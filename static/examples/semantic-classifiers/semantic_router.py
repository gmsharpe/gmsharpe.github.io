"""
Semantic Router: Declarative intent routing for agentic workflows

Semantic Router abstracts away embedding selection, similarity computation,
and fallback handling. You declaratively define routes and let the library
handle the routing logic.

This example shows both local (free) and API-based encoder options.

Install: pip install semantic-router
"""

from semantic_router import Route, RouteLayer
from semantic_router.encoders import HuggingFaceEncoder

# Define routes declaratively with example utterances
routes = [
    Route(
        name="book_flight",
        utterances=[
            "Book me a flight",
            "I need to book a flight",
            "Can you find me a flight to Paris",
            "Schedule a flight for tomorrow",
            "Flights to Tokyo",
            "Flight booking",
            "Reserve airline tickets"
        ]
    ),
    Route(
        name="weather_info",
        utterances=[
            "What's the weather like",
            "Is it raining today",
            "Tell me the forecast",
            "How hot is it",
            "Weather in Berlin",
            "Will it snow tomorrow",
            "Temperature today"
        ]
    ),
    Route(
        name="small_talk",
        utterances=[
            "Hello",
            "How are you",
            "What's up",
            "Good morning",
            "Hi there",
            "Hey",
            "Greetings"
        ]
    )
]

print("=" * 60)
print("Semantic Router with Local HuggingFace Encoder (FREE)")
print("=" * 60)
print()

# Option 1: Local HuggingFace encoder (uses sentence-transformers)
# Downloads ~90MB model on first run, then cached locally
# No API keys required, completely free
print("Initializing local encoder (sentence-transformers/all-MiniLM-L6-v2)...")
encoder = HuggingFaceEncoder(name="sentence-transformers/all-MiniLM-L6-v2")
router = RouteLayer(encoder=encoder, routes=routes)
print("✓ Router ready!\n")

# Test routing with local encoder
test_inputs = [
    "Book me a flight to Tokyo",
    "Is it going to rain in Berlin?",
    "Hey, how are you?",
    "I need flights to Madrid",
    "What's the temperature forecast?",
    "This is completely unrelated nonsense text"
]

print("Testing routes with local encoder:")
print("-" * 60)

for user_input in test_inputs:
    result = router(user_input)
    route_name = result.name if result.name else "NO_MATCH"
    
    # Show similarity score if available
    score_info = ""
    if hasattr(result, 'similarity_score') and result.similarity_score is not None:
        score_info = f" (confidence: {result.similarity_score:.3f})"
    
    print(f"Input: {user_input}")
    print(f"Route: {route_name}{score_info}")
    print()

print()
print("=" * 60)
print("Option 2: OpenAI Encoder (API-based, requires key)")
print("=" * 60)
print()

# Uncomment to use OpenAI encoder instead:
"""
from semantic_router.encoders import OpenAIEncoder

encoder = OpenAIEncoder(api_key="your-api-key-here")
router = RouteLayer(encoder=encoder, routes=routes)

result = router("Book me a flight to Tokyo")
print(f"Route: {result.name}")
"""

print("To use OpenAI encoder:")
print("1. pip install openai")
print("2. Get API key from https://platform.openai.com/")
print("3. Uncomment the code block above")
print("4. Replace 'your-api-key-here' with your actual key")
print()
print("Note: OpenAI encoder costs ~$0.0001 per classification")
print("      HuggingFace encoder is completely free")
print()

# Example: Using routes with actual handlers
print("=" * 60)
print("Example: Routing to Handler Functions")
print("=" * 60)
print()

def handle_booking(user_input: str) -> str:
    return f"✈️  Flight booking agent: Processing '{user_input}'"

def handle_weather(user_input: str) -> str:
    return f"🌤️  Weather service: Getting forecast for '{user_input}'"

def handle_small_talk(user_input: str) -> str:
    return f"💬 Chat agent: Responding to '{user_input}'"

def handle_unknown(user_input: str) -> str:
    return f"❓ No matching route. Escalating to human: '{user_input}'"

# Map routes to handlers
handlers = {
    "book_flight": handle_booking,
    "weather_info": handle_weather,
    "small_talk": handle_small_talk,
}

# Route and dispatch
sample_inputs = [
    "Book me a flight to Paris",
    "What's the weather in London?",
    "Hello there!"
]

for user_input in sample_inputs:
    result = router(user_input)
    route_name = result.name if result.name else "unknown"
    
    # Get handler for this route
    handler = handlers.get(route_name, handle_unknown)
    response = handler(user_input)
    
    print(f"User: {user_input}")
    print(f"Response: {response}")
    print()

print()
print("=" * 60)
print("Key Takeaways")
print("=" * 60)
print()
print("✓ Semantic Router provides declarative routing")
print("✓ Works completely locally with HuggingFaceEncoder (no costs)")
print("✓ Can use OpenAI encoder for potentially better accuracy")
print("✓ Handles confidence thresholds and fallbacks automatically")
print("✓ Perfect for agentic systems with multiple tools/agents")
print()
