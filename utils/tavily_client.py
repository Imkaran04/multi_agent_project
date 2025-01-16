import requests

class TavilyClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.tavily.io/v1"

    def search(self, query):
        url = f"{self.base_url}/search"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"query": query}
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
