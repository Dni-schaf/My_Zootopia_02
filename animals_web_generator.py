"""App to parse JSON data an create a html website out of it."""


import json


def load_data(file_path: str) -> Any:
    """Loads a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as handle:
        return json.load(handle)


def serialize_animal(animal: dict) -> str:
    """Serialize an animal into HTML representation."""
    output = ''
    output += '<li class="cards__item">'
    if name := animal.get('name'):
        output += f'<div class="card__title"> {name}</div>'
    output += '<div class="card__text">'
    output += '<ul class="list">'

    characteristics = animal.get('characteristics', {})
    if diet := characteristics.get('diet'):
        output += f'<li><strong>Diet:</strong> {diet}</li>'

    locations = animal.get('locations', [])
    if locations:
        output += f'<li><strong>Location:</strong> {locations[0]}</li>'

    if animal_type := characteristics.get('type'):
        output += f'<li><strong>Type:</strong> {animal_type}</li>'
    output += '</ul>'
    output += '</div>'
    output += '</li>'
    return output


def animals_output(data: list) -> str:
    """Convert every animal into a HTML representation."""
    output = ''
    for animal in data:
        output += serialize_animal(animal)
    return output


def main():
    """Orchestrate the animals web generator."""
    animals_data = load_data('animals_data.json')

    with open('animals_template.html', 'r', encoding='utf-8') as file:
        html_template = file.read()

    animals_info = animals_output(animals_data)
    new_html = html_template.replace('__REPLACE_ANIMALS_INFO__', animals_info)

    with open('animals.html', 'w', encoding='utf-8') as file:
        file.write(new_html)


if __name__ == '__main__':
    main()
