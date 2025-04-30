import os
from dotenv import load_dotenv
import data_fetcher  # Import the data_fetcher module

# Load environment variables (if you have them in a .env file)
load_dotenv()

API_KEY = os.getenv('API_KEY')

def serialize_animal(animal_obj):
    """Convert a single animal object to an HTML string"""
    output = ""
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'    <strong>Diet:</strong> {animal_obj["characteristics"]["diet"].capitalize()}<br/>\n'
    output += f'    <strong>Location:</strong> {animal_obj["locations"][0].capitalize()}<br/>\n'

    if "type" in animal_obj["characteristics"]:
        output += f'    <strong>Type:</strong> {animal_obj["characteristics"]["type"].capitalize()}<br/>\n'

    if "slogan" in animal_obj["characteristics"]:
        output += f'    <strong>Slogan:</strong> {animal_obj["characteristics"]["slogan"].capitalize()}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output

def main():
    # Load the HTML template
    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        html_template = template_file.read()

    # Ask the user for the animal name
    animal_name = input("Please enter an animal: ")

    # Fetch the animal data using data_fetcher
    data = data_fetcher.fetch_data(animal_name)

    if not data:
        # If no animals are found, display a message
        output = f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"
    else:
        # Generate HTML for each animal
        output = ""
        for animal in data:
            output += serialize_animal(animal)

    # Replace the placeholder with the generated animal HTML
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

    # Save the result to a file
    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(html_output)

    print("✅ HTML file has been created successfully!")

# Run main only if the script is executed directly
if __name__ == "__main__":
    main()
