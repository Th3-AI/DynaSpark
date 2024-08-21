# DynaSpark API

A Python client for interacting with the DynaSpark API.

## Installation

You can install the package via pip:

```bash
pip install dynaspark
```

```python
#Example Code
from dynaspark import dsai

# Initialize the client with your API key
client = dsai(api_key='your_api_key')

# Generate a text response
user_input = "Tell me a joke."
response = client.generate_response(user_input)

print("Response:", response['response'])
```
