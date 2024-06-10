import math
import numpy

def funkcja(x):
    return math.sqrt(x**3 + 2)

def wyznaczanie_punktow(a, b, n):
    x_points = numpy.linspace(a, b, n)
    y_points = []

    for i in range(len(x_points)):
        y_points.append(funkcja(x_points[i]))

    return x_points, y_points

def tworzenie_ukladu_rownan(m, x_points, y_points):
    S = []
    for k in range(m + 1):
        wiersz = []
        for j in range(m + 1):
            sum = 0
            for i in range(len(x_points)):
                sum += x_points[i] ** (k + j)
            wiersz.append(sum)
        S.append(wiersz)

    T = []
    for k in range(m + 1):
        sum = 0
        for i in range(len(x_points)):
            sum += x_points[i] ** k * y_points[i]
        T.append(sum)

    return S, T

# motoda eliminacji gaussa z sprawozdania Interpolacja funkcje sklejające
def eliminacja_gaussa(macierz, rozwiazania):
    for i in range(len(macierz)):
        pivot_row = i
        for j in range(i+1, len(macierz)):
            if abs(macierz[j][i]) > abs(macierz[pivot_row][i]):
                pivot_row = j
        macierz[i], macierz[pivot_row] = macierz[pivot_row], macierz[i]
        rozwiazania[i], rozwiazania[pivot_row] = rozwiazania[pivot_row], rozwiazania[i]

        for j in range(i+1, len(macierz)):
            factor = macierz[j][i] / macierz[i][i]
            for k in range(i, len(macierz)):
                macierz[j][k] -= factor * macierz[i][k]
            rozwiazania[j] -= factor * rozwiazania[i]

    X = [0] * len(macierz)
    for i in range(len(macierz) - 1, -1, -1):
        X[i] = rozwiazania[i] / macierz[i][i]
        for j in range(i - 1, -1, -1):
            rozwiazania[j] -= macierz[j][i] * X[i]
    return X

def metoda_najmniejszych_kwadratow(a, b, x, n, m):
    x_points, y_points = wyznaczanie_punktow(a, b, n)
    S, T = tworzenie_ukladu_rownan(m, x_points, y_points)
    a = eliminacja_gaussa(S, T)

    wielomian = 0
    for i in range(m + 1):
        wielomian += a[i] * x**i

    return wielomian

a = -1
b = 1
x = 0.25
n = 3
m = 2

print(metoda_najmniejszych_kwadratow(a, b, x, n, m))