# OpenRouter Client

A Python client library for the OpenRouter API.

**Currently supported APIs:**
- Chat Completion - `/chat/completions` (streaming / non-streaming)

## Installation

### Requirements
- Python 3.8 or higher

Directly via `pip`:
```bash
pip install openrouter-client
```

If you're using `uv`:
```bash
uv add openrouter-client
```

## Usage
Requires following environment variable to be set:

```bash
export OPENROUTER_API_KEY="<your_api_key>"
```

Optional (with current defaults):

```bash
export OPENROUTER_API_URL="https://openrouter.ai/api/v1"
export OPENROUTER_API_PREFIX="/ai/openrouter"
export OPENROUTER_INTEGRATION_TESTS=False
export OPENROUTER_API_TEST_MODEL=meta-llama/llama-3.2-1b-instruct:free
```

Preferably, put these in an `.env` or `.env.dev` file in project root.

## Usage

For using the api, here's sample codes (most parameters in [OpenRouter REST API](https://openrouter.ai/docs/api-reference/overview) are available)

### Option 1: Use as a client library

```python
from openrouter.client import create_chat_completion
from openrouter.models.request import ChatCompletionRequest

# Example usage
request = ChatCompletionRequest(
    messages=[{"role": "user", "content": "Hello, how are you?"}],
    model="<model_name>"
)
response = create_chat_completion(request)
```

### Option 2: Add to an existing FastAPI app

```python
from fastapi import FastAPI
from openrouter import api_router

app = FastAPI()
app.include_router(api_router)

# Now the OpenRouter endpoints are available at /ai/openrouter/*
# Optionally, you can customize the API prefix with OPENROUTER_API_PREFIX env variable
```

### Option 3: Use as a standalone FastAPI app

```python
from openrouter import create_app

app = create_app()

# Run with uvicorn
# uvicorn main:app --reload
```

## Testing

***Read [integration testing](#integration-testing) section before running tests***

To run the tests:
```bash
# Using requirements file
pip install -r requirements-dev.txt
pytest

# Or using uv
uv sync --extra dev
pytest
```
### Integration Testing
The package includes both unit tests (with mocks) and integration tests (with real API calls).

To run integration tests:
1. Set your OpenRouter API key in the environment or .env file
2. Enable integration tests with an environment variable:
```bash
# Enable integration tests
export OPENROUTER_INTEGRATION_TESTS=True
```

3. **[OPTIONAL]** Set the OpenRouter API test model with an environment variable:
```bash
# Set the OpenRouter API test model
export OPENROUTER_API_TEST_MODEL="meta-llama/llama-3.2-1b-instruct:free"
```

4. Run tests
```bash
# Run all tests including integration tests
pytest

# Run only integration tests
# Strict max tokens set to 5 to be safe
pytest tests/test_integration.py
```

*Integration tests make actual API calls to OpenRouter API. By default, the api uses `meta-llama/llama-3.2-1b-instruct:free` for faster tests with max 30 tokens for output. This model can be changed by setting the `OPENROUTER_API_TEST_MODEL` environment variable.*

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

Copyright (C) 2025 Sudhanshu Aggarwal (@mrcodepanda)
