# DynaSpark API Documentation 🌟

<div align="center">

[![API Status](https://img.shields.io/badge/API-Active-brightgreen)](https://dynaspark.onrender.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The official documentation for the DynaSpark API - Your free AI generation platform

</div>

## 📋 Table of Contents

- [Base URL](#base-url)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [Text Generation](#text-generation)
  - [Image Generation](#image-generation)
  - [Audio Response Generation](#audio-response-generation)
- [Response Formats](#response-formats)
- [Error Handling](#error-handling)
- [Rate Limits](#rate-limits)
- [Examples](#examples)

## 🔗 Base URL

```
https://dynaspark.onrender.com/api
```

## 🔐 Authentication

The API uses a simple API key authentication system. Include your API key in the request parameters:

```
?api_key=YOUR_API_KEY
```

> Note: Currently, no API key is required for testing and development. You can use the API without authentication.

## 📡 Endpoints

### Text Generation

Generate text responses using various models and parameters.

**Endpoint:** `/generate_response`

**Method:** `GET`

**Parameters:**

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

**Example Request:**
```bash
curl "https://dynaspark.onrender.com/api/generate_response?user_input=What%20is%20AI%3F&api_key=YOUR_API_KEY&temperature=0.8"
```

**Example Response:**
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

Generate images from text descriptions.

**Endpoint:** `/generate_image`

**Method:** `GET`

**Parameters:**

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

**Example Request:**
```bash
curl "https://dynaspark.onrender.com/api/generate_image?user_input=A%20beautiful%20sunset&api_key=YOUR_API_KEY&width=1024&height=768"
```

**Example Response:**
```json
{
    "image_url": "https://dynaspark.onrender.com/generated/image_123456.png",
    "model": "flux",
    "seed": 12345
}
```

### Audio Response Generation

Generate audio responses using text generation with audio output.

**Endpoint:** `/generate_response`

**Method:** `GET`

**Parameters:**

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `user_input` | string | The input text to generate a response for | Required |
| `api_key` | string | Your API key | Required |
| `model` | string | Must be "openai-audio" | Required |
| `voice` | string | Voice to use | "alloy" |

**Available Voices:**

| Voice | Description |
|-------|-------------|
| `alloy` | Balanced, natural-sounding voice (default) |
| `echo` | Clear, professional voice |
| `fable` | Warm, engaging voice |
| `onyx` | Deep, authoritative voice |
| `nova` | Bright, energetic voice |
| `shimmer` | Soft, melodic voice |

**Example Request:**
```bash
curl "https://dynaspark.onrender.com/api/generate_response?user_input=Hello%20world&api_key=YOUR_API_KEY&model=openai-audio&voice=nova" \
     --output response.mp3
```

**Response:**
- Binary audio data (MP3 format)
- Content-Type: audio/mpeg

## 📦 Response Formats

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

## ⚠️ Error Handling

The API uses standard HTTP status codes and returns error messages in JSON format:

```json
{
    "error": "Error message description"
}
```

Common Error Codes:
- `400`: Bad Request (invalid parameters)
- `401`: Unauthorized (invalid API key)
- `429`: Too Many Requests (rate limit exceeded)
- `500`: Internal Server Error

## 🚦 Rate Limits

- Free API Key: 100 requests per hour
- Custom API Keys: Contact for limits

Rate limit headers are included in responses:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1625097600
```

## 📝 Examples

### Text Generation with Parameters
```bash
curl "https://dynaspark.onrender.com/api/generate_response?user_input=Write%20a%20poem&api_key=YOUR_API_KEY&temperature=0.8&top_p=0.9&presence_penalty=0.6&frequency_penalty=0.6"
```

### Image Generation with Custom Size
```bash
curl "https://dynaspark.onrender.com/api/generate_image?user_input=A%20futuristic%20city&api_key=YOUR_API_KEY&width=1024&height=768&model=flux&nologo=true"
```

### Audio Response with Different Voice
```bash
curl "https://dynaspark.onrender.com/api/generate_response?user_input=Hello%20world&api_key=YOUR_API_KEY&model=openai-audio&voice=nova" \
     --output response.mp3
```

### JSON Response
```bash
curl "https://dynaspark.onrender.com/api/generate_response?user_input=List%203%20colors&api_key=YOUR_API_KEY&json=true"
```

## 🔄 API Status

Check the API status at: https://dynaspark.onrender.com/status

## 📞 Support

For API support, feature requests, or bug reports:
- GitHub Issues: https://github.com/Th3-AI/DynaSpark/issues
- Email: dvp.ai.ml@gmail.com

---

<div align="center">

Made with ❤️ by [Th3-C0der](https://github.com/Th3-C0der)

</div> 