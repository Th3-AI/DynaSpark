# 🐍 DynaSpark Python Client

[![PyPI version](https://badge.fury.io/py/dynaspark.svg)](https://badge.fury.io/py/dynaspark)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![API Status](https://img.shields.io/website?url=https%3A%2F%2Fdynaspark.onrender.com%2Fstatus)](https://dynaspark.onrender.com/status)
[![API Documentation](https://img.shields.io/badge/API_Docs-DynaSpark-blue)](https://github.com/Th3-AI/DynaSpark/blob/main/README.md)

A powerful Python client for the DynaSpark API - Your free AI generation platform. Generate text, images, and audio with ease using Python!

<div align="center">

[API Documentation](https://github.com/Th3-AI/DynaSpark/blob/main/README.md) | [Try API](https://th3-ai.github.io/DynaSpark) | [Report Issues](https://github.com/Th3-AI/DynaSpark/issues) | [Try DynaSpark AI](https://DynaSpark.onrender.com)

</div>

## ✨ Features

- 🆓 **Free to Use**: No API key required for testing and development
- 🚀 **Easy Integration**: Simple, intuitive Python interface
- 🎯 **Multiple Models**: Support for various text, image, and audio models
- 🔧 **Customizable**: Fine-tune generation parameters
- 🛡️ **Error Handling**: Robust error handling and rate limit management
- 📦 **Type Hints**: Full type support for better IDE integration

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [API Reference](#api-reference)
  - [Client Initialization](#client-initialization)
  - [Text Generation](#text-generation)
  - [Image Generation](#image-generation)
  - [Audio Generation](#audio-generation)
- [Examples](#examples)
- [Error Handling](#error-handling)
- [Rate Limits](#rate-limits)
- [Contributing](#contributing)
- [License](#license)
- [API Documentation](#api-documentation)

## 🚀 Installation

Install the package using pip:

```bash
pip install dynaspark
```

## ⚡ Quick Start

```python
from dynaspark import DynaSpark

# Initialize the client (no API key required)
client = DynaSpark()

# Generate text
response = client.generate_text(
    prompt="Explain quantum computing in simple terms",
    model="mistral",
    temperature=0.7
)
print(response.text)

# Generate an image
image = client.generate_image(
    prompt="A serene mountain landscape",
    width=1024,
    height=768,
    model="flux",
    nologo=True
)
image.save("landscape.png")

# Generate audio
audio = client.generate_audio(
    text="Welcome to DynaSpark!",
    voice="nova"
)
audio.save("welcome.mp3")
```

## 📚 API Reference

### Client Initialization

```python
from dynaspark import DynaSpark

# Basic initialization (no API key required)
client = DynaSpark()

# With custom API key (optional)
client = DynaSpark(api_key="your_api_key")

# With custom base URL
client = DynaSpark(base_url="https://custom-url.com/api")
```

### Text Generation

```python
response = client.generate_text(
    prompt="Your prompt here",
    model="mistral",  # Optional: model to use
    temperature=0.8,  # Optional: controls randomness (0.0-3.0)
    top_p=0.9,       # Optional: controls diversity (0.0-1.0)
    presence_penalty=0.0,  # Optional: penalizes repeated tokens (-2.0-2.0)
    frequency_penalty=0.0  # Optional: penalizes frequent tokens (-2.0-2.0)
)

# Access the generated text
print(response.text)

# Access metadata
print(f"Model used: {response.model}")
print(f"Token usage: {response.usage}")
```

### Image Generation

```python
image = client.generate_image(
    prompt="Your image description",
    width=768,        # Optional: image width (64-2048)
    height=768,       # Optional: image height (64-2048)
    model="flux",     # Optional: model to use (flux/turbo/gptimage)
    nologo=False,     # Optional: exclude watermark
    watermark=None    # Optional: custom watermark text
)

# Save the image
image.save("output.png")

# Get image URL
print(f"Image URL: {image.url}")

# Get image metadata
print(f"Dimensions: {image.width}x{image.height}")
print(f"Model used: {image.model}")
```

### Audio Generation

```python
audio = client.generate_audio(
    text="Text to convert to speech",
    voice="alloy"  # Optional: voice to use
)

# Save the audio
audio.save("output.mp3")

# Get audio metadata
print(f"Duration: {audio.duration} seconds")
print(f"Format: {audio.format}")
```

Available voices:
- `alloy`: Balanced, natural-sounding voice (default)
- `echo`: Clear, professional voice
- `fable`: Warm, engaging voice
- `onyx`: Deep, authoritative voice
- `nova`: Bright, energetic voice
- `shimmer`: Soft, melodic voice

## 📝 Examples

### Text Generation Examples

```python
# Basic text generation
response = client.generate_text("What is artificial intelligence?")

# Code generation with specific model
response = client.generate_text(
    prompt="Write a Python function to sort a list of dictionaries by a key",
    model="qwen-coder",
    temperature=0.2
)

# Creative writing with custom parameters
response = client.generate_text(
    prompt="Write a short story about a robot learning to paint",
    temperature=0.9,
    top_p=0.95,
    presence_penalty=0.6
)
```

### Image Generation Examples

```python
# Basic image generation
image = client.generate_image("A cute cat playing with yarn")

# High-resolution landscape
image = client.generate_image(
    prompt="A detailed landscape of mountains at sunset",
    width=1024,
    height=768,
    model="turbo",
    nologo=True
)

# Image with custom watermark
image = client.generate_image(
    prompt="A futuristic cityscape",
    watermark="Created with DynaSpark"
)
```

### Audio Generation Examples

```python
# Basic audio generation
audio = client.generate_audio("Welcome to DynaSpark!")

# Multiple voices
for voice in ["alloy", "echo", "nova"]:
    audio = client.generate_audio(
        text=f"This is voice {voice}",
        voice=voice
    )
    audio.save(f"voice_{voice}.mp3")
```

## ⚠️ Error Handling

The client includes robust error handling:

```python
from dynaspark import DynaSparkError, RateLimitError

try:
    response = client.generate_text("Hello, world!")
except RateLimitError as e:
    print(f"Rate limit exceeded. Try again in {e.reset_time} seconds")
except DynaSparkError as e:
    print(f"Error: {e.message}")
```

Common error types:
- `RateLimitError`: Rate limit exceeded
- `AuthenticationError`: Invalid API key
- `ValidationError`: Invalid parameters
- `ServerError`: API server error

## ⏱️ Rate Limits

The API implements rate limiting to ensure fair usage:

- Free tier: 100 requests per hour
- Maximum 10 concurrent requests
- Rate limit headers included in responses

```python
# Check rate limit status
limits = client.get_rate_limits()
print(f"Remaining requests: {limits.remaining}")
print(f"Reset time: {limits.reset_time}")
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [API Documentation](https://dynaspark.onrender.com/docs)
- [GitHub Repository](https://github.com/Th3-AI/DynaSpark)
- [PyPI Package](https://pypi.org/project/dynaspark)

## 👥 Social

- [YouTube](https://youtube.com/@Th3Coder)
- [Instagram](https://instagram.com/th3_c0der)
- [LinkedIn](https://www.linkedin.com/in/Th3-C0der)
- [Support on Ko-fi](https://ko-fi.com/th3coder)

## 🔗 API Documentation

This Python client is built on top of the DynaSpark API. For detailed information about the API endpoints, parameters, and features, please refer to the main API documentation:

[![API Documentation](https://img.shields.io/badge/API_Docs-DynaSpark-blue)](https://github.com/Th3-AI/DynaSpark/blob/main/README.md)

The API documentation includes:
- 📡 Complete endpoint reference
- 🔑 Authentication details
- 📊 Response formats
- ⚠️ Error handling
- ⏱️ Rate limits
- 📝 Example requests

[View API Documentation →](https://github.com/Th3-AI/DynaSpark/blob/main/README.md)

---

Made with ❤️ by [Th3-C0der](https://github.com/Th3-C0der) 