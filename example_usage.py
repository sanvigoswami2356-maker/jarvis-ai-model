"""
Example usage scenarios for Jarvis AI Model
"""

from jarvis_core import JarvisCore
from utils.nlp_processor import NLPProcessor, ContextManager


def example_basic_conversation():
    """Example: Basic conversation with Jarvis"""
    print("\n" + "="*60)
    print("EXAMPLE 1: Basic Conversation")
    print("="*60 + "\n")
    
    jarvis = JarvisCore(name="Jarvis", version="1.0.0")
    
    # Simulate user inputs
    inputs = [
        "Hello Jarvis",
        "How can you help me?",
        "What's your status?"
    ]
    
    for user_input in inputs:
        print(f"User: {user_input}")
        response = jarvis.process_input(user_input)
        print(f"Jarvis: {response['response']}")
        print(f"Status: {response['status']}\n")


def example_learning_preferences():
    """Example: Learning user preferences"""
    print("\n" + "="*60)
    print("EXAMPLE 2: Learning Preferences")
    print("="*60 + "\n")
    
    jarvis = JarvisCore(name="Jarvis", version="1.0.0")
    
    # Set user preferences
    preferences = {
        "language": "English",
        "timezone": "UTC",
        "communication_style": "formal",
        "response_detail": "brief"
    }
    
    print("Setting user preferences:")
    for key, value in preferences.items():
        jarvis.set_preference(key, value)
        print(f"  ✓ {key}: {value}")
    
    print("\nStored preferences:")
    for key, pref in jarvis.user_preferences.items():
        print(f"  • {key}: {pref['value']}")


def example_pattern_learning():
    """Example: Learning patterns"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Pattern Learning")
    print("="*60 + "\n")
    
    jarvis = JarvisCore(name="Jarvis", version="1.0.0")
    
    # Learn various patterns
    patterns = {
        "morning_greeting": {
            "time": "morning",
            "greeting": "Good morning",
            "suggested_action": "review_schedule"
        },
        "work_mode": {
            "time": "weekday_morning",
            "focus": "high",
            "notifications": "minimal"
        },
        "break_time": {
            "time": "afternoon",
            "duration": 15,
            "activity": "rest"
        }
    }
    
    print("Learning patterns:")
    for pattern_name, pattern_data in patterns.items():
        jarvis.learn_pattern(pattern_name, pattern_data)
        print(f"  ✓ Learned: {pattern_name}")
    
    print("\nStored patterns:")
    for pattern_name, pattern_info in jarvis.learned_patterns.items():
        print(f"  • {pattern_name}")
        print(f"    Data: {pattern_info['data']}")
        print(f"    Confidence: {pattern_info['confidence']}")


def example_nlp_processing():
    """Example: NLP processing capabilities"""
    print("\n" + "="*60)
    print("EXAMPLE 4: NLP Processing")
    print("="*60 + "\n")
    
    nlp = NLPProcessor()
    
    test_texts = {
        "Simple greeting": "Hello, how are you today?",
        "With emotion": "I am really happy and excited about this!",
        "With entities": "Email me at john@example.com or visit www.example.com",
        "Complex": "Machine learning and deep learning are powerful AI techniques"
    }
    
    for label, text in test_texts.items():
        print(f"\n{label}:")
        print(f"  Input: {text}")
        
        # Tokenization
        tokens = nlp.tokenize(text)
        print(f"  Tokens: {tokens[:5]}...")
        
        # Keywords
        keywords = nlp.get_keywords(text, top_n=3)
        print(f"  Keywords: {keywords}")
        
        # Sentiment
        sentiment = nlp.sentiment_keywords(text)
        print(f"  Sentiment: {sentiment['sentiment']}")
        
        # Entities
        entities = nlp.extract_entities(text)
        if entities['emails']:
            print(f"  Emails: {entities['emails']}")
        if entities['urls']:
            print(f"  URLs: {entities['urls']}")


def example_context_management():
    """Example: Context management"""
    print("\n" + "="*60)
    print("EXAMPLE 5: Context Management")
    print("="*60 + "\n")
    
    context = ContextManager(max_context_size=5)
    
    # Simulate conversation
    messages = [
        ("User", "Hi, I need help with Python"),
        ("Jarvis", "I'd be happy to help with Python!"),
        ("User", "How do I work with lists?"),
        ("Jarvis", "Lists are ordered collections..."),
        ("User", "Can you show an example?")
    ]
    
    print("Building conversation context:")
    for role, message in messages:
        context.add_context(message, role.lower())
        print(f"  {role}: {message}")
    
    print("\nContext history (last 5):")
    for i, msg in enumerate(context.get_context(), 1):
        print(f"  {i}. [{msg['role'].upper()}] {msg['message']}")
    
    last_user_msg = context.get_last_user_message()
    print(f"\nLast user message: {last_user_msg}")


def example_task_management():
    """Example: Task management"""
    print("\n" + "="*60)
    print("EXAMPLE 6: Task Management")
    print("="*60 + "\n")
    
    jarvis = JarvisCore(name="Jarvis", version="1.0.0")
    
    # Simulate inputs that create tasks
    print("Processing task-related inputs:")
    task_inputs = [
        "Execute a data analysis script",
        "Run automated backups",
        "Schedule a meeting reminder"
    ]
    
    for task_input in task_inputs:
        print(f"  User: {task_input}")
        response = jarvis.process_input(task_input)
        print(f"  Status: {response['status']}")
    
    print(f"\nQueued tasks: {len(jarvis.task_queue)}")
    
    # Execute tasks
    print("\nExecuting tasks...")
    executed = jarvis.execute_tasks()
    print(f"Completed tasks: {len(executed)}")
    
    for task in executed:
        print(f"  ✓ Task {task['id']}: {task['status']}")


def example_similarity_analysis():
    """Example: Text similarity analysis"""
    print("\n" + "="*60)
    print("EXAMPLE 7: Similarity Analysis")
    print("="*60 + "\n")
    
    nlp = NLPProcessor()
    
    text_pairs = [
        ("I love programming", "I enjoy coding"),
        ("Machine learning is powerful", "Deep learning is amazing"),
        ("Python is great", "I hate Java"),
        ("Hello world", "Goodbye moon")
    ]
    
    print("Text similarity scores:")
    for text1, text2 in text_pairs:
        similarity = nlp.calculate_similarity(text1, text2)
        print(f"  '{text1}'")
        print(f"  '{text2}'")
        print(f"  Similarity: {similarity:.2%}\n")


def main():
    """Run all examples"""
    print("\n" + "🤖 JARVIS AI MODEL - USAGE EXAMPLES 🤖")
    print("=" * 60)
    
    example_basic_conversation()
    example_learning_preferences()
    example_pattern_learning()
    example_nlp_processing()
    example_context_management()
    example_task_management()
    example_similarity_analysis()
    
    print("\n" + "="*60)
    print("✓ All examples completed!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
