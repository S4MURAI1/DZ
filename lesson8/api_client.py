import os
import requests

class YouGileAPI:
    def __init__(self):
        self.base_url = os.getenv("YOUGILE_BASE_URL")
        self.api_key = os.getenv("YOUGILE_API_KEY")

        if not self.base_url or not self.api_key:
            raise ValueError("Не настроены переменные окружения YouGile")

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def create_project(self, data):
        return requests.post(
            f"{self.base_url}/projects",
            headers=self.headers,
            json=data
        )

    def update_project(self, project_id, data):
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
            json=data
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
