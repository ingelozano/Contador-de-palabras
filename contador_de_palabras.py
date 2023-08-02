#Importamos re (expresiones regulares de python)
import re

# Solicitamos al usuario ingresar el texto
texto = input("Ingresa el texto: ")

# Quitamos los caracteres que no contamos como palabras
quitar = ",;.:!\"'"
for caracter in quitar:
    texto = texto.replace(caracter, "")  # Remplazarlo por "nada"; es decir lo removemos

# Convertimos el texto a palabras minúsculas, pues una palabra mayúscula y minúscula cuenta como una sola
texto = texto.lower()

# Dividimos el texto en palabras utilizando expresiones regulares
palabras = re.findall(r'\b\w+\b', texto)

# Creamos un diccionario (estructura de datos) para contar las palabras. En este caso la clave del diccionario será la palabra, y el valor será el conteo
diccionario_frecuencias = {}
for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
    else:
        diccionario_frecuencias[palabra] = 1

for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    print(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia}")
