# Singapore Tour Guide Chatbot

A simple chatbot powered by OpenAI's GPT-4o-mini model that provides information about tourist attractions and activities in Singapore.

## Features

- Provides information about famous landmarks in Singapore
- Suggests popular places to visit
- Recommends activities for tourists

## Requirements

- Python 3.x
- OpenAI API key
- `openai` Python package

## Setup

⚠️ **Important**: This project does not include an API key. You must provide your own OpenAI API key to use this chatbot.

1. Install the required package:
   ```bash
   pip install openai
   ```

2. **Get your OpenAI API key**:
   - Sign up at [OpenAI](https://platform.openai.com/)
   - Create an API key in your account settings
   - Set your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY="your-actual-api-key-here"
   ```

3. Run the chatbot:
   ```bash
   python main.py
   ```

## Usage

The chatbot will automatically ask predefined questions about Singapore and provide responses based on the OpenAI model.

## Customization

### Changing Questions
You can customize the questions that the chatbot asks by modifying the `users_qn` list in `main.py`:

```python
users_qn=["what are some popular places in Singapore", "What should i be doing in Singapore"]
```

Simply replace the questions in this list with your own questions about Singapore tourism.
