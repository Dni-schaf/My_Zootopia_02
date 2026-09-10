import requests

from data_fetcher import fetch_data


def serialize_animal(animal):
    output = ""
    output += '<li class="cards__item">'
    if name := animal.get("name"):
        output += f'<div class="card__title">{name}</div>'
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


def create_html(animals_data):
    with open("animals_template.html", "r", encoding="utf-8") as file:
        html_template = file.read()

    animals_info = animals_output(animals_data)
    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(new_html)


def main():

    print("\nProgram to create animal website")
    #user_animal = input("Enter a name of an animal: ").strip()

    #if not user_animal:
    #    print("Input cannot be empty.")
    #    return

    try:
        animals_data = fetch_data('hedgehog')
    except requests.RequestException as e:
        print(f"There was an error requesting the data: {e}")
    else:
        if not animals_data:
            print("wrong input")
        else:
            create_html(animals_data)
            print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()