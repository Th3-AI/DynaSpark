import requests
from urllib.parse import quote

class DynaSparkError(Exception):
    """Custom exception for DynaSpark API errors."""
    pass

class DynaSpark:
    """A client for interacting with the DynaSpark API."""
    
    BASE_URL = "https://dynaspark.onrender.com/api/"
    VALID_MODELS = ['flux', 'turbo', 'gptimage']
    VALID_VOICES = ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']
    
    def __init__(self, api_key="TH3_API_KEY"):
        """Initialize the DynaSpark client.
        
        Args:
            api_key (str, optional): API key for authentication. Defaults to free API key.
        """
        self.api_key = api_key
        self.headers = {
            "User-Agent": "DynaSpark-Python-Client",
            "Accept": "application/json"
        }

    def _make_request(self, endpoint, params):
        """Make an API request and handle the response.
        
        Args:
            endpoint (str): API endpoint to call
            params (dict): Request parameters
            
        Returns:
            dict: Response data
            
        Raises:
            DynaSparkError: If the request fails
        """
        try:
            params['api_key'] = self.api_key
            response = requests.get(f"{self.BASE_URL}{endpoint}", params=params, headers=self.headers)
            response.raise_for_status()
            
            try:
                data = response.json()
                if "error" in data:
                    raise DynaSparkError(data["error"])
                return data
            except requests.exceptions.JSONDecodeError:
                if response.headers.get('content-type', '').startswith('audio/'):
                    return {"audio_data": response.content}
                return {"response": response.text}
                
        except requests.exceptions.RequestException as e:
            raise DynaSparkError(f"API request failed: {str(e)}")

    def generate_response(self, user_input, **kwargs):
        """Generate a text response using DynaSpark's text generation API.
        
        Args:
            user_input (str): The input text to generate a response for.
            **kwargs: Optional parameters for text generation or text-to-speech.
                - model (str): Model to use for generation
                - seed (int): Random seed for reproducibility
                - temperature (float): Controls randomness (0.0 to 3.0)
                - top_p (float): Controls diversity (0.0 to 1.0)
                - presence_penalty (float): Penalizes repeated tokens (-2.0 to 2.0)
                - frequency_penalty (float): Penalizes frequent tokens (-2.0 to 2.0)
                - json (bool): Whether to return JSON response
                - system (str): Custom system prompt
                - stream (bool): Whether to stream the response
                - private (bool): Whether to keep the generation private
                - referrer (str): Referrer information
                - voice (str): Voice for text-to-speech (alloy, echo, fable, onyx, nova, shimmer)
        
        Returns:
            dict: A dictionary containing the response data.
                - For text responses: {"response": "generated text"}
                - For errors: {"error": "error message"}
        """
        params = {"user_input": user_input}
        params.update(kwargs)
        return self._make_request("generate_response", params)

    def generate_image(self, prompt, **kwargs):
        """Generate an image using DynaSpark's image generation API.
        
        Args:
            prompt (str): The prompt to generate an image for
            **kwargs: Optional parameters
                - width (int): Image width (64-2048, default: 768)
                - height (int): Image height (64-2048, default: 768)
                - model (str): Model to use (flux, turbo, gptimage)
                - nologo (bool): Whether to exclude the watermark
                - seed (int): Random seed for reproducibility
                - wm (str): Custom watermark text
            
        Returns:
            str: URL to the generated image
            
        Raises:
            ValueError: If parameters are invalid
        """
        # Validate parameters
        if 'model' in kwargs and kwargs['model'] not in self.VALID_MODELS:
            raise ValueError(f"Model must be one of: {', '.join(self.VALID_MODELS)}")
            
        if 'width' in kwargs and not 64 <= kwargs['width'] <= 2048:
            raise ValueError("Width must be between 64 and 2048")
            
        if 'height' in kwargs and not 64 <= kwargs['height'] <= 2048:
            raise ValueError("Height must be between 64 and 2048")
        
        # Convert boolean nologo to string
        if 'nologo' in kwargs:
            kwargs['nologo'] = str(kwargs['nologo']).lower()
        
        params = {"user_input": prompt}
        params.update(kwargs)
        
        data = self._make_request("generate_image", params)
        return data.get("image_url")

    def generate_audio_response(self, text, voice='alloy'):
        """Generate an audio response using DynaSpark's text generation API with audio output.
        
        Args:
            text (str): The input text to generate an audio response for
            voice (str, optional): Voice to use for the response (alloy, echo, fable, onyx, nova, shimmer)
            
        Returns:
            bytes: The generated audio response in MP3 format
            
        Raises:
            ValueError: If voice is invalid
            DynaSparkError: If the API request fails
        """
        if voice not in self.VALID_VOICES:
            raise ValueError(f"Voice must be one of: {', '.join(self.VALID_VOICES)}")
            
        response = self.generate_response(text, model="openai-audio", voice=voice)
        if "audio_data" in response:
            return response["audio_data"]
        raise DynaSparkError("No audio response received from the API")

    def save_audio(self, audio_data, filename):
        """Save audio response data to a file.
        
        Args:
            audio_data (bytes): The audio response data to save
            filename (str): The name of the file to save to
            
        Returns:
            str: The path to the saved file
        """
        if not filename.endswith('.mp3'):
            filename += '.mp3'
            
        with open(filename, 'wb') as f:
            f.write(audio_data)
        return filename 