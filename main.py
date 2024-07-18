import numpy as np


# Función para convertir texto en una lista de números
def texto_a_numeros(texto):
    numeros = []
    for letra in texto.replace(' ', '').upper():
        numeros.append(ord(letra) - ord('A'))
    return numeros


# Función para convertir una lista de números en texto
def numeros_a_texto(numeros):
    texto = ''
    for numero in numeros:
        texto += chr((numero % 26) + ord('A'))
    return texto


# Función para multiplicar un bloque por la matriz de clave
def multiplicar_matriz_bloque(clave, bloque):
    resultado = np.dot(clave, bloque) % 26
    return resultado


# Función para cifrar el texto
def cifrar(texto, clave):
    n = clave.shape[0]
    texto_numeros = texto_a_numeros(texto)

    # Añadir ceros al final del texto si no es divisible por n
    while len(texto_numeros) % n != 0:
        texto_numeros.append(0)

    texto_cifrado = []
    for i in range(0, len(texto_numeros), n):
        bloque = np.array(texto_numeros[i:i + n])
        bloque_cifrado = multiplicar_matriz_bloque(clave, bloque)
        texto_cifrado.extend(bloque_cifrado)

    return numeros_a_texto(texto_cifrado)


# Función para descifrar el texto
def descifrar(texto_cifrado, clave):
    n = clave.shape[0]
    texto_cifrado_numeros = texto_a_numeros(texto_cifrado)

    # Calcular la inversa de la clave en módulo 26
    clave_inversa = np.linalg.inv(clave)
    clave_inversa = np.round(clave_inversa).astype(int) % 26

    texto_descifrado = []
    for i in range(0, len(texto_cifrado_numeros), n):
        bloque = np.array(texto_cifrado_numeros[i:i + n])
        bloque_descifrado = multiplicar_matriz_bloque(clave_inversa, bloque)
        texto_descifrado.extend(bloque_descifrado)

    return numeros_a_texto(texto_descifrado)


# Matriz de clave (3x3)
clave = np.array([[6, 24, 1],
                  [13, 16, 10],
                  [20, 17, 15]])

texto = 'BIENVENIDOS A ALGEBRA LINEAL'

# Cifrar y descifrar el texto
texto_cifrado = cifrar(texto, clave)
texto_descifrado = descifrar(texto_cifrado, clave)

# Mostrar resultados
print("Texto original:", texto)
print("Texto cifrado:", texto_cifrado)
print("Texto descifrado:", texto_descifrado)
