from kaggle.api.kaggle_api_extended import KaggleApi

class ResourceAssetCollectionAgent:
    def fetch_datasets(self, use_case_title):
        try:
            api = KaggleApi()
            api.authenticate()

            # Search for datasets based on the use case title
            datasets = api.dataset_list(search=use_case_title)
            
            dataset_links = []
            for dataset in datasets:
                dataset_links.append({
                    "title": dataset.title,
                    "link": f"https://www.kaggle.com/datasets/{dataset.ref}",
                    "description": dataset.description,
                    "last_updated": dataset.last_updated
                })
            return dataset_links
        except Exception as e:
            return [{"title": "Unable to retrieve datasets at the moment. Please try again later.", "link": "#", "description": str(e)}]
