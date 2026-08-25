import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

def print_animals(data):
    for animal in animals_data:
        if name := animal.get('name'):
            print(f"Name: {name}")
        if diet := animal.get('characteristics').get('diet'):
            print(f"Diet: {diet}")
        if location := animal.get('locations')[0]:
            print(f"Location: {location}")
        if animal_type := animal.get('characteristics').get('type'):
            print(f"Type: {animal_type}")
        print()


print_animals(animals_data)