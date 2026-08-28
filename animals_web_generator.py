import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def serialize_animal(animal):
    output = ""
    output += '<li class="cards__item">'
    if name := animal.get("name"):
        output += f'<div class="card__title"> {name}</div>'
    output += '<div class="card__text">'
    output += '<ul class="list">'

    characteristics = animal.get("characteristics", {})
    if diet := characteristics.get("diet"):
        output += f"<li><strong>Diet:</strong> {diet}</li>"

    locations = animal.get("locations", [])
    if locations:
        output += f"<li><strong>Location:</strong> {locations[0]}</li>"

    if animal_type := characteristics.get("type"):
        output += f"<li><strong>Type:</strong> {animal_type}</li>"
    output += '</ul>'
    output += '</div>'
    output += '</li>'
    return output


def animals_output(data):
    output = ''
    for animal in data:
        output += serialize_animal(animal)
    return output


animals_data = load_data("animals_data.json")


with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()


animals_info = animals_output(animals_data)
new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)


with open("animals.html", "w", encoding="utf-8") as file:
    file.write(new_html)

