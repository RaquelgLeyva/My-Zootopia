import json

# Step 1: Load the JSON data
def load_data(file_path):
    """Load animal data from JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

# Step 2: Read the HTML template
with open("animals_template.html", "r", encoding="utf-8") as template_file:
    html_template = template_file.read()

# Step 3: Load animal data
animals_data = load_data("animals_data.json")

# Step 4: Generate animal info HTML
output = ""

for fox in animals_data:
    output += '<li class="cards__item">\n'
    output += f"Name: {fox['name']}<br/>\n"
    output += f"Diet: {fox['characteristics']['diet']}<br/>\n"

    if fox["locations"]:
        output += f"Location: {fox['locations'][0]}<br/>\n"
    else:
        output += "Location: Unknown<br/>\n"

    if "type" in fox["characteristics"]:
        output += f"Type: {fox['characteristics']['type']}<br/>\n"

    output += '</li>\n'

# Step 5: Replace placeholder in template
html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 6: Write final HTML to file
with open("animals.html", "w", encoding="utf-8") as output_file:
    output_file.write(html_output)

print("✅ HTML file has been created successfully!")
