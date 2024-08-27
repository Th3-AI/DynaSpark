import requests

class DynaSpark:
    BASE_URL = "https://dynaspark.onrender.com/api/"

    def __init__(self, api_key):
        self.api_key = api_key

    def generate_response(self, user_input):
        endpoint = f"{self.BASE_URL}generate_response"
        params = {
            'user_input': user_input,
            'api_key': self.api_key
        }
        response = requests.get(endpoint, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def generate_image(self, prompt):
        endpoint = f"{self.BASE_URL}generate_image"
        params = {
            'user_input': prompt,
            'api_key': self.api_key
        }
        response = requests.get(endpoint, params=params)
        
        if response.status_code == 200:
            return response.json().get('image_url')
        else:
            response.raise_for_status()