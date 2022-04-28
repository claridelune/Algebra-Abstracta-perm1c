from inverso import inverso

ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrarAfin(mensaje, llave):
    if not inverso(llave[0], 27):
        return None
    newMensaje = ""
    for char in mensaje:
        newIndex = (llave[0] * ABC.find(char) + llave[1]) % 27
        newMensaje += ABC[newIndex]
    return newMensaje

def descifrarAfin(mensaje, llave):
    inv = inverso(llave[0], 27)
    if not inv:
        return None
    newMensaje = ""    
    for char in mensaje:
        newIndex = (inv * (ABC.find(char) - llave[1])) % 27
        newMensaje += ABC[newIndex]
    return newMensaje

if __name__ == "__main__":
    llave = [4, 7]
    print("Cifrado Afin de ELEMENTALMIQUERIDOWATSON:")
    print(cifrarAfin("ELEMENTALMIQUERIDOWATSON", llave))
    print()
    print("Descifrado Afin de OKHFSNKFNWFCWJHSNCHQYWFSWF:")
    print(descifrarAfin("OKHFSNKFNWFCWJHSNCHQYWFSWF", llave))
    print()
    """ Para hallar la clave [23, 17] que decifra el mensaje se uso:
    for i in range(27):
        for j in range(27):
            print(descifrarAfin("SLBCMVRBSHZBTÑSRQVVMSZBVHÑBVRQVLALHZBTÑSRQVWQAXLZWÑAQFQV", [i, j]), i, j)
    print()
    """
    print("Descifrado Afin de SLBCMVRBSHZBTÑSRQVVMSZBVHÑBVRQVLALHZBTÑSRQVWQAXLZWÑAQFQV:")
    print(descifrarAfin("SLBCMVRBSHZBTÑSRQVVMSZBVHÑBVRQVLALHZBTÑSRQVWQAXLZWÑAQFQV", [23, 17]))
