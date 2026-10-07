# Portfolio de Salim Charchaoui Oilad Ali

Web personal de Ingeniero Informático, generada con Python.

**Ver la web:** https://ualsco569.github.io

## Cómo funciona

Los datos se escriben una sola vez en `datos.json`. El script `generar.py`
los combina con `plantilla.html` (Jinja2) y produce el `index.html` estático
que se publica con GitHub Pages.

```
datos.json  +  plantilla.html  →  generar.py  →  index.html
```

## Estructura

| Archivo | Función |
|---|---|
| `datos.json` | Contenido del CV (formación, experiencia, proyectos, habilidades) |
| `plantilla.html` | Diseño de la página con huecos para los datos |
| `style.css` | Estilos, responsive y modo oscuro automático |
| `generar.py` | Genera `index.html` a partir de los dos anteriores |

## Ejecutarlo en local

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install jinja2
python generar.py
```

## Tecnologías

Python · Jinja2 · HTML · CSS · GitHub Pages