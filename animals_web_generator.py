import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

# Call the function and store the loaded data in a variable
animals_data = load_data('animals_data.json')

# Loop through the list and print the data
for fox in animals_data:

    # Get the first location if it exists
    if fox["locations"]:
        locations = fox["locations"][0]
    else:
        print("Unknown")

    # Get the diet from the characteristics
    diet = fox["characteristics"]["diet"]


    print(f"Name: {fox['name']}\nDiet: {diet}\nLocation: {locations}")

    # Only print type if it exists
    if "type" in fox["characteristics"]:
        print(f"Type: {fox['characteristics']['type']}")


    print()
