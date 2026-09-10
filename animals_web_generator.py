"""App to request Animal-Data from API to create an HTML-website."""

import requests
from typing import Any
from data_fetcher import fetch_data


def serialize_animal(animal: dict) -> str:
    """Serialize an animal into HTML representation."""
    output = ''
    output += '<li class="cards__item">'
    if name := animal.get('name'):
        output += f'<div class="card__title">{name}</div>'
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
    """Convert every animal into HTML representation."""
    output = ''
    for animal in data:
        output += serialize_animal(animal)
    return output


def read_html():
    with open('animals_template.html', 'r', encoding='utf-8') as file:
        html_template = file.read()
        return html_template


def save_html(new_html):
    with open('animals.html', 'w', encoding='utf-8') as file:
        file.write(new_html)


def create_html(data: Any) -> None:
    """Replace placeholder in html with data."""
    html_template = read_html()
    if type(data) is str:
        content = data
    else:
        content = animals_output(data)
    new_html = html_template.replace('__REPLACE_ANIMALS_INFO__', content)
    save_html(new_html)


def main():
    """Orchestrate the animals web generator."""
    print('\nProgram to create animal website\n')
    user_animal = ''

    while not user_animal:
        user_animal = input('Enter a name of an animal: ').strip().lower()

    try:
        animals_data = fetch_data(user_animal)
    except requests.RequestException as e:
        print(f'There was an error requesting the data: {e}')
    else:
        if not animals_data:
            website_string = f'<h2>The animal "{user_animal}" does not exist.</h2>'
            create_html(website_string)
            print(f'Website generated but the animal "{user_animal}" does not exist.')
        else:
            create_html(animals_data)
            print('Website was successfully generated to the file animals.html.')


if __name__ == '__main__':
    main()