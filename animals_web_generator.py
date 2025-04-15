import json


# Paso 1: Función para cargar el archivo JSON
def load_data(file_path):
    """Cargar los datos desde un archivo JSON"""
    with open(file_path, "r") as handle:
        return json.load(handle)


# Paso 2: Leer la plantilla HTML
with open("animals_template.html", "r") as template_file:
    html_template = template_file.read()

# Paso 3: Cargar los datos de los animales desde el archivo JSON
animals_data = load_data('animals_data.json')

# Paso 4: Generar la información HTML con los datos de los animales
animal_info = ""  # String vacío donde vamos a agregar la información de los animales

for fox in animals_data:
    # Comenzamos a crear un bloque HTML para cada animal
    animal_info += f'<div class="animal-card"><h2>{fox["name"]}</h2>\n'

    # Obtener la dieta del animal
    diet = fox["characteristics"]["diet"]
    animal_info += f'<p><strong>Diet:</strong> {diet}</p>\n'

    # Obtener la ubicación del animal
    locations = fox["locations"][0] if fox["locations"] else "Unknown"
    animal_info += f'<p><strong>Location:</strong> {locations}</p>\n'

    # Solo incluir tipo si existe
    if "type" in fox["characteristics"]:
        animal_info += f'<p><strong>Type:</strong> {fox["characteristics"]["type"]}</p>\n'

    # Cerrar el bloque del animal
    animal_info += "</div>\n"

# Paso 5: Reemplazar el marcador __REPLACE_ANIMALS_INFO__ en la plantilla HTML
html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_info)

# Paso 6: Escribir el contenido HTML final en un archivo
with open("animals.html", "w") as output_file:
    output_file.write(html_output)

print("HTML file has been created successfully!")
