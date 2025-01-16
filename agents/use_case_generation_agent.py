from tavily import TavilyClient

class UseCaseGenerationAgent:
    def __init__(self, api_key):
        self.client = TavilyClient(api_key)

    def assess_feasibility(self, description):
        # Basic rule-based feasibility assessment using keywords
        low_keywords = ["manual effort", "limited data", "high cost", "custom data collection"]
        moderate_keywords = ["predictive modeling", "machine learning", "advanced algorithms", "moderate data"]
        high_keywords = ["deep learning", "large-scale data", "AI-driven", "high performance"]

        # Default to moderate
        feasibility = "Moderate"
        
        # Check for keywords in the description and set feasibility accordingly
        for keyword in low_keywords:
            if keyword.lower() in description.lower():
                return "Low"
        
        for keyword in moderate_keywords:
            if keyword.lower() in description.lower():
                feasibility = "Moderate"
                
        for keyword in high_keywords:
            if keyword.lower() in description.lower():
                feasibility = "High"
                
        return feasibility

    def generate_use_cases(self, industry):
        try:
            # Make a query to the Tavily API (search for use cases related to the industry)
            response = self.client.search(f"AI use cases in {industry}")
            if response.get('results'):
                use_cases = []
                for result in response['results']:
                    description = result.get('content', 'No description found')
                    
                    # Assess feasibility based on description
                    feasibility = self.assess_feasibility(description)
                    
                    use_case = {
                        "title": result.get('title', 'No title found'),
                        "description": description,
                        "feasibility": feasibility
                    }
                    use_cases.append(use_case)
                return use_cases
            else:
                return [{"title": "No use cases found", "description": "No relevant use cases were found for this industry.", "feasibility": "Unknown"}]

        except Exception as e:
            return [{"title": "unable to fetch use cases", "description": str(e), "feasibility": "Unknown"}]
    