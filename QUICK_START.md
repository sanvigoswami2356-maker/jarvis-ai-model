# Quick Start Guide

## 🚀 30 Second Setup

```bash
cd jarvis-ai-model
pip install -r requirements.txt
python jarvis_core.py
```

Type: `Hello Jarvis`  
Done! ✅

---

## 💡 5 Minute Usage

### Just Chat
```python
from jarvis_core import JarvisCore

jarvis = JarvisCore()
response = jarvis.process_input("What's your name?")
print(response['response'])
```

### Automate Tasks
```python
jarvis.process_input("Run backup")
jarvis.execute_tasks()
```

### Remember Stuff
```python
jarvis.set_preference("theme", "dark")
jarvis.learn_pattern("morning", {"time": "8am", "task": "check_email"})
```

### Analyze Text
```python
from utils.nlp_processor import NLPProcessor

nlp = NLPProcessor()
sentiment = nlp.sentiment_keywords("I love this!")
print(sentiment)  # {'positive': 1, 'negative': 0, 'sentiment': 'positive'}
```

---

## 🔧 Real Examples

### Send Emails & Tasks
```python
jarvis = JarvisCore()

# Queue tasks
jarvis.process_input("Send email to john@example.com")
jarvis.process_input("Schedule meeting at 3pm")

# Execute
completed = jarvis.execute_tasks()
print(f"Done: {len(completed)} tasks")
```

### Extract Data
```python
nlp = NLPProcessor()

text = "Email: contact@company.com, Phone: 555-1234"
entities = nlp.extract_entities(text)
print(entities['emails'])   # ['contact@company.com']
print(entities['numbers'])  # ['555', '1234']
```

### Compare Texts
```python
nlp = NLPProcessor()

sim = nlp.calculate_similarity(
    "Hello world",
    "Hello there"
)
print(f"{sim:.0%} similar")  # 50% similar
```

---

## ✨ That's It!

Just use these 3 lines for 90% of what you need:

```python
from jarvis_core import JarvisCore
jarvis = JarvisCore()
response = jarvis.process_input("Your message here")
```

Check `QUICK_START.py` for copy-paste code!
