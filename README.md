# DevGround

## ChatGPT API wrapper

This is a wrapper for the [OpenAI's GPT-4 API](https://openai.com/product/gpt-4) by [DevGround](https://devground.cz/).

### Model

The AI model used in this package is GPT-4

### License

This package is licensed under the MIT license.

### Language

The language used in this package is Python.

### Requirements

requires environment variables:

- OPENAI_API_KEY

### Installation

Package is available on [PyPI](https://pypi.org/project/gpt4api-dg/) and can be installed with pip:

```bash
pip install gpt4api_dg
```

### Usage

Usage sample:

```python
from dotenv import load_dotenv
import os

from gpt4api_dg import API
from gpt4api_dg.models import User, Message, Conversation, Role

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
API.set_api_key(openai_api_key)

test_user = API.add_user("test_id", "test_username")
instruction = Message(
    role = Role.SYSTEM,
    content = "You are a music advisor. You will answer questions about music and help people find new music."
)
test_conversation = API.add_conversation("test_id", instruction)
test_input = input(f"{test_user.username}: ")
message = Message(
    role = Role.USER,
    content = test_input
)
response = API.get_response("test_id", message)
print(response.content)
```
