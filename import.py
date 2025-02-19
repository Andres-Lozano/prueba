import requests
import re
from collections import Counter

def obtenerDato():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("fact", "No se pudo obtener el dato")
    return "Error al consultar la API"

def procesar_texto(texto):

    palabras = re.findall(r'\b\w+\b', texto.lower())

    contador = Counter(palabras)

    palabrasOrdenadas = sorted(contador.items(), key=lambda x: (len(x[0]), x[0]))
    return palabrasOrdenadas

def main():
    fact = obtenerDato()
    print("Dato curioso:", fact, "\n")
    palabrasProcesadas = procesar_texto(fact)
    for i, (palabra, cantidad) in enumerate(palabrasProcesadas, 1):
        print(f"{i}. {palabra} {cantidad}")

if __name__ == "main":
    main()