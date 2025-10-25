import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def get_data(place, forecast_days):
    """Fetch weather data from OpenWeatherMap API with error handling"""
    try:
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}'
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Check if 'list' key exists (it won't if city is not found)
            if 'list' in data:
                filtered_data = data['list']
                nr_values = 8 * forecast_days
                filtered_data = filtered_data[:nr_values]
                return filtered_data
            else:
                # City not found or API error
                print(f"Error: {data.get('message', 'Unknown error')}")
                return None
        else:
            # HTTP error (404, 401, etc.)
            error_data = response.json()
            print(f"API Error {response.status_code}: {error_data.get('message', 'Unknown error')}")
            return None

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return None


if __name__ == "__main__":
    print("Run in main.py")