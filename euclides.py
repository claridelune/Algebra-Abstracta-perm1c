def euclides(a, b):
    if b == 0:
        return a
    else:
        return euclides(b, a%b)

def euclidesExt(a, b): #retorna el mcd, x & y
    if b == 0:
        return (a, 1, 0)
    else:
        (d, dx, dy) = euclidesExt(b, a % b)
        (x, y) = (dy, dx - a//b * dy)
        return (d, x, y)
