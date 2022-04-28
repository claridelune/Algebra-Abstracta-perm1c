from inverso import inverso

ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrarAfin(mensaje, llave):
    newMensaje = ""
    for char in mensaje:
        newIndex = (llave[0] * ABC.find(char) + llave[1]) % 27
        newMensaje += ABC[newIndex]
    return newMensaje

def descifrarAfin(mensaje, llave):
    newMensaje = ""
    for char in mensaje:
        inv = inverso(llave[0], 27)
        if not inv:
            return None
        newIndex = (inv * (ABC.find(char) - llave[1])) % 27
        newMensaje += ABC[newIndex]
    return newMensaje

if __name__ == "__main__":
    llave = [4, 7]
    print(cifrarAfin("ELEMENTALMIQUERIDOWATSON", llave))
    print(descifrarAfin("OKHFSNKFNWFCWJHSNCHQYWFSWF", llave))
    print()

    for i in range(27):
        for j in range(27):
            print(descifrarAfin("SLBCMVRBSHZBTÑSRQVVMSZBVHÑBVRQVLALHZBTÑSRQVWQAXLZWÑAQFQV", [i, j]), i, j)
    print()

    print(descifrarAfin("SLBCMVRBSHZBTÑSRQVVMSZBVHÑBVRQVLALHZBTÑSRQVWQAXLZWÑAQFQV", [23, 17]))
