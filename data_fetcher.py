import requests
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
    """Fetch animal data from the API based on the animal name"""
    url = "https://api.api-ninjas.com/v1/animals"
    headers = {
        'X-Api-Key': API_KEY  # Header with your API key
    }

    try:
        # Make the GET request to the API
        response = requests.get(f"{url}?name={animal_name}", headers=headers)

        # Check if the response was successful
        if response.status_code == 200:
            # If the response is valid, return the JSON data
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        # Catch any error during the request
        print(f"Request failed: {e}")
        return None
