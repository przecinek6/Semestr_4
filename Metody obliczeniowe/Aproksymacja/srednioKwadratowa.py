import math
import numpy

def funkcja(x):
    return math.sqrt(x**3 + 2)

# zmodyfikowana metoda kwadratury Gaussa Legendrea z sprawozdania Całkowanie numeryczne
def kwadratura1(a, b, n, cord_i, cord_j):
    waga, wezel = numpy.polynomial.legendre.leggauss(n)
    suma = 0

    for i in range(n):
        x = ((b - a)/2) * waga[i] + ((b + a)/2)
        suma += wezel[i] * (x**cord_i * x**cord_j)

    return suma * (b - a) / 2

def kwadratura2(a, b, n, cord_i):
    waga, wezel = numpy.polynomial.legendre.leggauss(n)
    suma = 0

    for i in range(n):
        x = ((b - a)/2) * waga[i] + ((b + a)/2)
        suma += wezel[i] * (x**cord_i * funkcja(x))

    return suma * (b - a) / 2

# eliminacja z sprawozdania Interpolacja
def eliminacja_gaussa(macierz, y_points):
    for i in range(len(macierz)):
        pivot_row = i
        for j in range(i+1, len(macierz)):
            if abs(macierz[j][i]) > abs(macierz[pivot_row][i]):
                pivot_row = j
        macierz[i], macierz[pivot_row] = macierz[pivot_row], macierz[i]
        y_points[i], y_points[pivot_row] = y_points[pivot_row], y_points[i]

        for j in range(i+1, len(macierz)):
            factor = macierz[j][i] / macierz[i][i]
            for k in range(i, len(macierz)):
                macierz[j][k] -= factor * macierz[i][k]
            y_points[j] -= factor * y_points[i]

    X = [0] * len(macierz)
    for i in range(len(macierz) - 1, -1, -1):
        X[i] = y_points[i] / macierz[i][i]
        for j in range(i - 1, -1, -1):
            y_points[j] -= macierz[j][i] * X[i]
    return X

def sredniokwadratowa(a, b, x, n):
    uklad_rownan = []

    for i in range(n + 1):
        wiersz = []
        for j in range(n + 1):
            wiersz.append(kwadratura1(a, b, 20, i, j))
        uklad_rownan.append(wiersz)

    rozwiazania_ukladu_rownan = []

    for i in range(n + 1):
        rozwiazania_ukladu_rownan.append(kwadratura2(a, b, 20, i))

    wspolczynniki = eliminacja_gaussa(uklad_rownan, rozwiazania_ukladu_rownan)

    suma = 0
    for i in range(n + 1):
        suma += wspolczynniki[i] * x**i

    return suma

a = -1
b = 1
x = 0.25
n = 16

print(sredniokwadratowa(a, b, x, n))