import math
import numpy as np

def calka(x):
    return math.sin(0.7 * x + 0.1) / (1.3 + math.cos(x**2 + 0.2))

def kwadratura(a, b, n):
    waga, wezel = np.polynomial.legendre.leggauss(n)
    suma = 0

    for i in range(n):
        t = ((b - a)/2) * waga[i] + ((b + a)/2)
        suma += wezel[i] * calka(t)

    return suma * (b - a) / 2

a = 0.3
b = 1.1
n = int(input("Liczba przedzialow: "))

print(kwadratura(a, b, n))