import math

def calka(x):
    return math.sin((0.7 * x) + 0.1) / 1.3 + math.cos(x**2 + 0.2)

def metoda_trapezow(a, b, n):
    h = (b - a) / n
    xi = [a + (i/n) * (b-a) for i in range(1, n)]
    suma = (calka(a) + calka(b)) / 2

    for i in range(1, n):
        suma += calka(xi[i - 1])

    return suma * h

a = 0.3
b = 1.1
n = int(input("Liczba przedzialow: "))

print(metoda_trapezow(a, b, n))