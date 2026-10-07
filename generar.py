import json
from jinja2 import Environment, FileSystemLoader

# 1. Leer los datos
with open("datos.json", encoding="utf-8") as f:
    datos = json.load(f)

# 2. Cargar la plantilla
env = Environment(loader=FileSystemLoader("."))
plantilla = env.get_template("plantilla.html")

# 3. Rellenar la plantilla con los datos
html = plantilla.render(**datos)

# 4. Guardar el resultado
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html generado")