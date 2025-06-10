# DynaSpark Python Client 🚀

<div align="center">

[![PyPI version](https://badge.fury.io/py/dynaspark.svg)](https://badge.fury.io/py/dynaspark)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful, free Python client for the DynaSpark API - No API key required! 🆓

</div>

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🆓 **Free Usage** | No API key required - uses free key by default |
| 📝 **Text Generation** | Generate text responses with customizable parameters |
| 🎨 **Image Generation** | Create images with various models and options |
| 🔊 **Audio Responses** | Get audio responses with multiple voice options |
| 🛠️ **Easy to Use** | Simple and intuitive Python interface |
| 🔒 **Secure** | Built-in error handling and validation |

## 📦 Installation

```bash
pip install dynaspark
```

## 🚀 Quick Start

```python
from dynaspark import DynaSpark

# Initialize client (no API key needed)
ds = DynaSpark()

# Generate text
response = ds.generate_response("What is artificial intelligence?")
print(response.get('response', ''))

# Generate image
image_url = ds.generate_image("A beautiful sunset over mountains")
print(f"Generated image: {image_url}")

# Generate audio response
audio_data = ds.generate_audio_response("Hello, this is a test!")
ds.save_audio(audio_data, "response.mp3")
```

## 📚 API Reference

### Client Initialization

```python
from dynaspark import DynaSpark

# Initialize with default free API key
ds = DynaSpark()

# Or specify your own API key (optional)
ds = DynaSpark(api_key="your_api_key")
```

### Text Generation

Generate text responses with customizable parameters.

```python
# Basic usage
response = ds.generate_response("What is Python?")
print(response.get('response', ''))

# Advanced usage with parameters
response = ds.generate_response(
    "Write a poem about technology",
    model="mistral",          # Model to use
    temperature=0.8,         # Controls randomness (0.0 to 3.0)
    top_p=0.9,              # Controls diversity (0.0 to 1.0)
    presence_penalty=0.6,    # Penalizes repeated tokens (-2.0 to 2.0)
    frequency_penalty=0.6,   # Penalizes frequent tokens (-2.0 to 2.0)
    json=True,              # Return JSON response
    system="You are a poet", # Custom system prompt
    stream=False,           # Stream the response
    private=False,          # Keep generation private
    seed=42                 # For reproducible results
)
```

#### Available Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `model` | str | Model to use | None |
| `temperature` | float | Controls randomness (0.0-3.0) | None |
| `top_p` | float | Controls diversity (0.0-1.0) | None |
| `presence_penalty` | float | Penalizes repeated tokens (-2.0-2.0) | None |
| `frequency_penalty` | float | Penalizes frequent tokens (-2.0-2.0) | None |
| `json` | bool | Return JSON response | False |
| `system` | str | Custom system prompt | None |
| `stream` | bool | Stream the response | False |
| `private` | bool | Keep generation private | False |
| `seed` | int | Random seed for reproducibility | None |
| `referrer` | str | Referrer information | None |

### Image Generation

Create images from text descriptions with various options.

```python
# Basic usage
image_url = ds.generate_image("A serene mountain landscape")

# Advanced usage
image_url = ds.generate_image(
    "A futuristic city with flying cars",
    width=1024,           # Image width (64-2048)
    height=768,           # Image height (64-2048)
    model="flux",         # Model: flux, turbo, or gptimage
    nologo=True,          # Exclude watermark
    seed=42,              # For reproducible results
    wm="DynaSpark"        # Custom watermark text
)
```

#### Available Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `width` | int | Image width (64-2048) | 768 |
| `height` | int | Image height (64-2048) | 768 |
| `model` | str | Model to use (flux/turbo/gptimage) | None |
| `nologo` | bool | Exclude watermark | False |
| `seed` | int | Random seed | None |
| `wm` | str | Custom watermark | None |

### Audio Response Generation

Generate audio responses with different voices.

```python
# Basic usage
audio_data = ds.generate_audio_response("Hello, this is a test!")

# With different voice
audio_data = ds.generate_audio_response(
    "This is a test with a different voice.",
    voice="nova"  # Available voices: alloy, echo, fable, onyx, nova, shimmer
)

# Save to file
ds.save_audio(audio_data, "response.mp3")
```

#### Available Voices

| Voice | Description |
|-------|-------------|
| `alloy` | Balanced, natural-sounding voice (default) |
| `echo` | Clear, professional voice |
| `fable` | Warm, engaging voice |
| `onyx` | Deep, authoritative voice |
| `nova` | Bright, energetic voice |
| `shimmer` | Soft, melodic voice |

## ⚠️ Error Handling

The package includes comprehensive error handling:

```python
from dynaspark import DynaSpark, DynaSparkError

ds = DynaSpark()

try:
    # Your code here
    response = ds.generate_response("Hello")
    print(response.get('response', ''))
except DynaSparkError as e:
    print(f"API Error: {e}")
except ValueError as e:
    print(f"Invalid Parameter: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ by Th3-C0der

</div>