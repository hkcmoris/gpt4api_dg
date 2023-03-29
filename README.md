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

Package will be available on PyPI soon.

--install the package with pip:--

```bash
pip install gpt4api_dg
```

### Usage

Usage sample is copied from earlier gpt-3.5-turbo project and is subject to change. It is not yet tested with gpt-4.

```python
from dg_chatgpt_api import ChatGPTAPI as api

api.reconnect()
api.add_user("user_id", "username")
api.add_conversation("user_id")
message = {
    "role": "user",
    "content": "message"
}
response = api.get_response("user_id", message)
```
