import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def animals_output(data):
    output = ""
    for animal in data:
        if name := animal.get("name"):
            output += f"Name: {name}\n"

        # Sicheres Auslesen verschachtelter Dictionaries:
        characteristics = animal.get("characteristics", {})
        if diet := characteristics.get("diet"):
            output += f"Diet: {diet}\n"

        locations = animal.get("locations", [])
        if locations:
            output += f"Location: {locations[0]}\n"

        if animal_type := characteristics.get("type"):
            output += f"Type: {animal_type}\n"

        output += "\n"
    return output


# Hauptprogramm
animals_data = load_data("animals_data.json")

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_template = file.read()

# Erzeugen und Ersetzen
animals_info = animals_output(animals_data)
new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

# Ausgabe des finalen HTML-Codes
print(new_html)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(new_html)