import math

def calka(x):
    return math.sin(0.7 * x + 0.1) / (1.3 + math.cos(x**2 + 0.2))

def metoda_simpsona(a, b, n):
    xi = [a + (i/n) * (b-a) for i in range(0, n + 1)]
    ti = [(xi[i + 1] + xi[i]) / 2 for i in range(0, n)]
    h = (xi[1] - xi[0]) / 2
    suma = calka(a) + calka(b)

    for i in range(0, len(ti)):
        suma += 4 * calka(ti[i])

    for i in range(1, len(xi) - 1):
        suma += 2 * calka(xi[i])

    return (h/3) * suma

a = 0.3
b = 1.1
n = int(input("Liczba przedzialow: "))

print(metoda_simpsona(a, b, n))