import json
import subprocess
import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

BASE = Path(__file__).parent

# 1. Datos públicos + datos privados (si existen)
datos = json.loads((BASE / "datos.json").read_text(encoding="utf-8"))
privados = BASE / "datos_privados.json"
if privados.exists():
    datos.update(json.loads(privados.read_text(encoding="utf-8")))

# 2. Generar el HTML del CV
env = Environment(loader=FileSystemLoader(BASE))
html = env.get_template("plantilla_cv.html").render(**datos)
cv_html = BASE / "cv.html"
cv_html.write_text(html, encoding="utf-8")

# 3. Buscar Edge o Chrome
candidatos = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]
navegador = next((c for c in candidatos if Path(c).exists()), None)
if navegador is None:
    sys.exit("No encuentro Edge ni Chrome en las rutas habituales.")

# 4. Imprimir el HTML a PDF
salida = BASE / "salida"
salida.mkdir(exist_ok=True)
pdf = salida / "CV_Salim_Charchaoui.pdf"

subprocess.run([
    navegador,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--user-data-dir={BASE / '.edge-tmp'}",
    f"--print-to-pdf={pdf}",
    cv_html.as_uri(),
], check=True)

print(f"PDF generado: {pdf}")