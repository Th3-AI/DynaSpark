import requests

class dsai:
    BASE_URL = "https://dynaspark.onrender.com/api/generate_response"

    def __init__(self, api_key):
        self.api_key = api_key

    def generate_response(self, user_input):
        params = {
            'user_input': user_input,
            'api_key': self.api_key
        }
        response = requests.get(self.BASE_URL, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
