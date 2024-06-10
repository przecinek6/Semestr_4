import math

def funkcja(x):
    return math.sqrt(x**3 + 2)

def wielomiany_legendrea(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * wielomiany_legendrea(n - 1, x) - (n - 1) * wielomiany_legendrea(n - 2, x)) / n

# zmodyfikowana metoda kwadratury Gaussa Legendrea z sprawozdania Całkowanie numeryczne
def metoda_trapezow(a, b, n, n2):
    h = (b - a) / n
    xi = [a + (i/n) * (b-a) for i in range(1, n)]
    suma = ((wielomiany_legendrea(n2, a) ** 2) * + wielomiany_legendrea(n2, b) ** 2) / 2

    for i in range(1, n):
        suma += wielomiany_legendrea(n2, xi[i - 1]) ** 2

    return suma * h

def metoda_trapezow2(a, b, n, n2):
    h = (b - a) / n
    xi = [a + (i/n) * (b-a) for i in range(1, n)]
    suma = (wielomiany_legendrea(n2, a)*funkcja(a) + wielomiany_legendrea(n2, b)*funkcja(b)) / 2

    for i in range(1, n):
        suma += wielomiany_legendrea(n2, xi[i - 1])*funkcja(xi[i - 1])

    return suma * h

def wielomiany_ortagonalne(a, b, n, x, dokladnosc_trapezow):
    lambda_tab = []
    c_tab = []

    for i in range(n + 1):
        lambda_tab.append(metoda_trapezow(a, b, dokladnosc_trapezow, i))
        c_tab.append((1 / lambda_tab[i]) * metoda_trapezow2(a, b, dokladnosc_trapezow, i))

    sum = 0
    for i in range(len(c_tab)):
        sum += c_tab[i] * wielomiany_legendrea(i, x)

    return sum

a = -1
b = 1
x = 0.25
n = 16
dokladnosc_trapezow = 1000

print(wielomiany_ortagonalne(a, b, n, x, dokladnosc_trapezow))