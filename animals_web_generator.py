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
    output += f'  <div class="card__title">{fox["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'    <strong>Diet:</strong> {fox["characteristics"]["diet"]}<br/>\n'

    if fox["locations"]:
        output += f'    <strong>Location:</strong> {fox["locations"][0]}<br/>\n'
    else:
        output += '    <strong>Location:</strong> Unknown<br/>\n'

    if "type" in fox["characteristics"]:
        output += f'    <strong>Type:</strong> {fox["characteristics"]["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'



# Step 5: Replace placeholder in template
html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 6: Write final HTML to file
with open("animals.html", "w", encoding="utf-8") as output_file:
    output_file.write(html_output)

print("✅ HTML file has been created successfully!")
print(html_output)  # Para ver cómo está quedando el HTML generado

