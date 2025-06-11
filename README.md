# DynaSpark API Documentation 🌟

<div align="center">

[![API Status](https://img.shields.io/badge/API-Active-brightgreen)](https://dynaspark.onrender.com/status)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-1.2.2.1-blue.svg)](https://github.com/Th3-AI/DynaSpark)
[![Python Client](https://img.shields.io/badge/Python_Client-Docs-blue)](https://github.com/Th3-AI/DynaSpark/blob/main/README-py.md)

The official documentation for the DynaSpark API - Your free AI generation platform

[Try API](https://th3-ai.github.io/DynaSpark) | [Try DynaSpark AI](https://DynaSpark.onrender.com) | [Documentation](https://th3-ai.github.io/DynaSpark/docs.html) | [Python Client](https://github.com/Th3-AI/DynaSpark/blob/main/README-py.md) | [Report Issues](https://github.com/Th3-AI/DynaSpark/issues)

</div>

## 📋 Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [Text Generation](#text-generation)
  - [Image Generation](#image-generation)
  - [Audio Response Generation](#audio-response-generation)
- [Response Formats](#response-formats)
- [Error Handling](#error-handling)
- [Rate Limits](#rate-limits)
- [Examples](#examples)
- [API Status](#api-status)
- [Support](#support)
- [Python Client](#python-client)

## Overview

DynaSpark is a powerful AI generation platform that provides easy access to various AI models for text, image, and audio generation. The API is designed to be simple to use while offering advanced features for developers.

### Key Features

- 🤖 Multiple AI models for text generation
- 🎨 High-quality image generation with customization options
- 🔊 Natural-sounding audio responses
- 🔒 Simple authentication system
- 📊 Comprehensive rate limiting
- 🚀 Fast and reliable API endpoints

## Quick Start

1. **Base URL**: `https://dynaspark.onrender.com/api`
2. **Authentication**: Currently, no API key is required
3. **Example Request**:
```bash
curl "https://dynaspark.onrender.com/api/generate_response?user_input=Hello%20world"
```

## Authentication

The API uses a simple API key authentication system. Include your API key in the request parameters:

```bash
?api_key=YOUR_API_KEY
```

> **Note**: Currently, no API key is required for testing and development. You can use the API without authentication.

## Endpoints

### Text Generation

Generate text responses using various models and parameters.

**Endpoint**: `/generate_response`  
**Method**: `GET`

#### Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `user_input` | string | The input text to generate a response for | Required |
| `api_key` | string | Your API key | Required |
| `model` | string | Model to use for generation | None |
| `temperature` | float | Controls randomness (0.0-3.0) | None |
| `top_p` | float | Controls diversity (0.0-1.0) | None |
| `presence_penalty` | float | Penalizes repeated tokens (-2.0-2.0) | None |
| `frequency_penalty` | float | Penalizes frequent tokens (-2.0-2.0) | None |
| `json` | boolean | Return JSON response | false |
| `system` | string | Custom system prompt | None |
| `stream` | boolean | Stream the response | false |
| `private` | boolean | Keep generation private | false |
| `seed` | integer | Random seed for reproducibility | None |
| `referrer` | string | Referrer information | None |
| `voice` | string | Voice for audio response | None |

#### Example Request

```bash
curl "https://dynaspark.onrender.com/api/generate_response?user_input=What%20is%20AI%3F&temperature=0.8"
```

#### Example Response

```json
{
    "response": "Artificial Intelligence (AI) is a branch of computer science...",
    "model": "default",
    "usage": {
        "prompt_tokens": 4,
        "completion_tokens": 150,
        "total_tokens": 154
    }
}
```

### Image Generation

Generate images from text descriptions with various customization options.

**Endpoint**: `/generate_image`  
**Method**: `GET`

#### Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `user_input` | string | The prompt to generate an image for | Required |
| `api_key` | string | Your API key | Required |
| `width` | integer | Image width (64-2048) | 768 |
| `height` | integer | Image height (64-2048) | 768 |
| `model` | string | Model to use (flux/turbo/gptimage) | None |
| `nologo` | boolean | Exclude watermark | false |
| `seed` | integer | Random seed | None |
| `wm` | string | Custom watermark | None |

#### Example Request

```bash
curl "https://dynaspark.onrender.com/api/generate_image?user_input=A%20beautiful%20sunset&width=1024&height=768"
```

#### Example Response

```json
{
    "image_url": "https://dynaspark.onrender.com/generated/image_123456.png",
    "model": "flux",
    "seed": 12345
}
```

### Audio Response Generation

Generate natural-sounding audio responses using text generation with audio output.

**Endpoint**: `/generate_response`  
**Method**: `GET`

#### Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `user_input` | string | The input text to generate a response for | Required |
| `api_key` | string | Your API key | Required |
| `model` | string | Must be "openai-audio" | Required |
| `voice` | string | Voice to use | "alloy" |

#### Available Voices

| Voice | Description |
|-------|-------------|
| `alloy` | Balanced, natural-sounding voice (default) |
| `echo` | Clear, professional voice |
| `fable` | Warm, engaging voice |
| `onyx` | Deep, authoritative voice |
| `nova` | Bright, energetic voice |
| `shimmer` | Soft, melodic voice |

#### Example Request

```bash
curl "https://dynaspark.onrender.com/api/generate_response?user_input=Hello%20world&model=openai-audio&voice=nova" \
     --output response.mp3
```

#### Response

- Binary audio data (MP3 format)
- Content-Type: audio/mpeg

## Response Formats

### Text Generation
- Default: JSON object with `response` field
- With `json=true`: Full JSON response with metadata
- With `stream=true`: Server-sent events stream

### Image Generation
- JSON object with `image_url` field
- Image URL is valid for 24 hours

### Audio Response
- Binary MP3 data
- Content-Type: audio/mpeg

## Error Handling

The API uses standard HTTP status codes and returns error messages in JSON format:

```json
{
    "error": "Error message description"
}
```

### Common Error Codes

| Code | Description |
|------|-------------|
| `400` | Bad Request (invalid parameters) |
| `401` | Unauthorized (invalid API key) |
| `429` | Too Many Requests (rate limit exceeded) |
| `500` | Internal Server Error |

## Rate Limits

- Free API Key: 100 requests per hour
- Custom API Keys: Contact for limits

Rate limit headers are included in responses:

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1625097600
```

## Examples

### Text Generation with Parameters

```bash
curl "https://dynaspark.onrender.com/api/generate_response?user_input=Write%20a%20poem&temperature=0.8&top_p=0.9&presence_penalty=0.6&frequency_penalty=0.6"
```

### Image Generation with Custom Size

```bash
curl "https://dynaspark.onrender.com/api/generate_image?user_input=A%20futuristic%20city&width=1024&height=768&model=flux&nologo=true"
```

### Audio Response with Different Voice

```bash
curl "https://dynaspark.onrender.com/api/generate_response?user_input=Hello%20world&model=openai-audio&voice=nova" \
     --output response.mp3
```

### JSON Response

```bash
curl "https://dynaspark.onrender.com/api/generate_response?user_input=List%203%20colors&json=true"
```

## API Status

Check the API status at: [https://dynaspark.onrender.com/status](https://dynaspark.onrender.com/status)

## Support

For API support, feature requests, or bug reports:

- GitHub Issues: [https://github.com/Th3-AI/DynaSpark/issues](https://github.com/Th3-AI/DynaSpark/issues)
- Email: [dvp.ai.ml@gmail.com](mailto:dvp.ai.ml@gmail.com)

## Python Client

For a more convenient way to use the DynaSpark API in Python, check out our official Python client:

[![Python Client](https://img.shields.io/badge/Python_Client-Docs-blue)](https://github.com/Th3-AI/DynaSpark/blob/main/README-py.md)

The Python client provides:
- 🐍 Simple Python interface
- 📦 Easy installation via pip
- 🎯 Full API support
- 🔧 Type hints and IDE integration
- 🛡️ Built-in error handling

Quick example:
```python
from dynaspark import DynaSpark

# Initialize client (no API key required)
client = DynaSpark()

# Generate text
response = client.generate_text("Hello, world!")
print(response.text)
```

[View Python Client Documentation →](https://github.com/Th3-AI/DynaSpark/blob/main/README-py.md)

---

<div align="center">

Made with ❤️ by [Th3-C0der](https://github.com/Th3-C0der)

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Th3-C0der)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@Th3Coder)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/th3_c0der)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/Th3-C0der)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/th3coder)

</div> 
