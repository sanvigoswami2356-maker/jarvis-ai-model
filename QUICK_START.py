"""
QUICK START - Copy & Paste Ready Code Examples
"""

# ============================================================================
# EXAMPLE 1: Simple Chat (Copy & Paste This)
# ============================================================================

from jarvis_core import JarvisCore
from utils.nlp_processor import NLPProcessor

# Create Jarvis
jarvis = JarvisCore(name="Jarvis")

# Chat with it
response = jarvis.process_input("Hello Jarvis, what can you do?")
print(response['response'])


# ============================================================================
# EXAMPLE 2: Task Automation
# ============================================================================

jarvis2 = JarvisCore()

# Run a task
jarvis2.process_input("Execute backup now")
results = jarvis2.execute_tasks()
print(f"Tasks completed: {len(results)}")


# ============================================================================
# EXAMPLE 3: Learn & Remember
# ============================================================================

jarvis3 = JarvisCore()

# Remember user info
jarvis3.set_preference("name", "John")
jarvis3.set_preference("email", "john@example.com")

# Use it later
prefs = jarvis3.user_preferences
print(f"User: {prefs['name']['value']}")


# ============================================================================
# EXAMPLE 4: Text Analysis
# ============================================================================

nlp = NLPProcessor()

text = "I love this amazing product!"

# Get sentiment
sentiment = nlp.sentiment_keywords(text)
print(f"Feeling: {sentiment['sentiment']}")

# Get keywords
keywords = nlp.get_keywords(text)
print(f"Keywords: {keywords}")

# Extract emails/URLs
entities = nlp.extract_entities("Contact: john@example.com or visit example.com")
print(f"Emails found: {entities['emails']}")


# ============================================================================
# EXAMPLE 5: Full Workflow (Real-World)
# ============================================================================

jarvis4 = JarvisCore(name="MyAssistant")

# 1. Start conversation
msg1 = jarvis4.process_input("Hi, I'm starting a Python project")
print(f"AI: {msg1['response']}")

# 2. Learn something
jarvis4.learn_pattern("project_python", {
    "language": "Python",
    "type": "web_app"
})

# 3. Set preferences
jarvis4.set_preference("project_path", "/home/user/projects")

# 4. Get history
history = jarvis4.get_conversation_history()
print(f"\nTotal messages: {len(history)}")

# 5. Check learned patterns
print(f"Patterns learned: {list(jarvis4.learned_patterns.keys())}")


# ============================================================================
# COPY THESE SNIPPETS & RUN THEM!
# ============================================================================
