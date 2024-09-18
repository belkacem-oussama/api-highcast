import os
from dotenv import load_dotenv
import requests
from fastapi import HTTPException

load_dotenv()

CARBON_INTERFACE_URL = os.getenv("API_URL")
CARBON_INTERFACE_API_KEY = os.getenv("API_KEY")

class CarbonService:
    def __init__(self, data) -> None:
        self.data = data
        self.headers = {
            "Authorization": f"Bearer {CARBON_INTERFACE_API_KEY}",
            "Content-Type": "application/json"
        }

    def get_emission(self) -> float | int:
        url = f"{CARBON_INTERFACE_URL}/estimates"

        try:
            response = requests.post(url, json=self.data, headers=self.headers)
            response.raise_for_status()
        except requests.RequestException as e:
            raise HTTPException(status_code=502, detail=f"Erreur lors de l'appel à CarbonInterface: {str(e)}")

        return response.json()
