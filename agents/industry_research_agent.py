from tavily import TavilyClient

class IndustryResearchAgent:
    def __init__(self, api_key):
        # Instantiate the Tavily client with the provided API key
        self.client = TavilyClient(api_key=api_key)

    def fetch_industry_info(self, industry, focus_area=None):
        query = f"{industry} industry trends"
        if focus_area:
            query += f" and {focus_area}"

        try:
            # Make a request to the Tavily API using the search method
            response = self.client.search(query)
            results = response.get('results', [])
            
            if not results:
                return "No results found for the given industry or focus area."
            
            industry_info = []
            for result in results:
                # Only include title and URL, exclude summary
                industry_info.append({
                    "title": result.get('title', 'No Title'),
                    "url": result.get('url', '#')
                })
            return industry_info
        except Exception as e:
            return f"An error occurred: {e}"
