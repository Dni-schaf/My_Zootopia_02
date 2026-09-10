import requests
from config import API_KEY, BASE_URL


def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  headers = {'X-Api-Key': API_KEY}
  params = {"name": animal_name}
  requests = do_api_request(params, headers, BASE_URL)
  print(requests)
  return requests


def do_api_request(params, headers, url):
  try:
      response = requests.get(url, headers=headers, params=params, timeout=100)
      response.raise_for_status()

      data = response.json()
      return data

  except requests.exceptions.HTTPError as http_err:
      print("HTTP error occurred:", http_err)
  except requests.exceptions.ConnectionError:
      print("No internet connection")
  except requests.exceptions.Timeout:
      print("Timeout error")
  except requests.exceptions.RequestException as err:
      print(f"An unexpected error occurred: {err}")
