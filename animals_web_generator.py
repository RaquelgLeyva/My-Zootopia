import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

# Create a variable then we call the function and save the data.
animals_data = load_data('animals_data.json')

# Recorremos e imprimimos los datos
for fox in animals_data:

    if fox["locations"]:
        locations = fox["locations"][0]
    else:
        print("Unknown")
    diet = fox["characteristics"]["diet"]

    print(f"Name: {fox['name']}\nDiet: {diet}\nLocation: {locations}")

    # Solo imprimir type si existe
    if "type" in fox["characteristics"]:
        print(f"Type: {fox['characteristics']['type']}")

    print()



