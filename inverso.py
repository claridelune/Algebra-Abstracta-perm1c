from euclides import euclidesExt

def inverso(a, n):
    (mcd, x, y) = euclidesExt(a, n)
    if mcd == 1:
        return x % n
    return None

if __name__ == "__main__":
    a = int(input("Ingrese a (entero): "))
    n = int(input("Ingrese n (entero positivo): "))
    inv = inverso(a, n)
    if inv:
        print(f"El inverso de a (mod n) es : {inv}")
    else:
        print("No se puede calcular el inverso\na no es entero, n no es entero positivo o a y n no son coprimos")
