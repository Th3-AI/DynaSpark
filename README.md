# DynaSpark API

Currently only Python package is available.

A Python client for interacting with the DynaSpark API.

## Installation

You can install the package via pip:

```bash
pip install dynaspark
```

## Usage

```python
#Example Code
from dynaspark import DynaSpark

# Initialize the DynaSpark API client
client = DynaSpark(api_key="your_api_key_here")

# Generate a response
response = client.generate_response(user_input="Hello!")
print(response)

# Generate an image
image_url = client.generate_image(prompt="A majestic lion with a flowing mane, standing on a rocky cliff overlooking a sunset.")
print(image_url)
```

## Free API KEY

```
TH3_API_KEY
```