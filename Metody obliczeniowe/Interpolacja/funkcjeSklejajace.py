def generuj_wiersz(x_points, ktory_wiersz):
    wiersz = []

    for i in range(4):
            wiersz.append(x_points[ktory_wiersz] ** i)

    for i in range(1, ktory_wiersz + 1):
        wiersz.append((x_points[ktory_wiersz] - x_points[i]) ** 3)

    while len(wiersz) < len(x_points) + 2:
        wiersz.append(0)

    return wiersz

def pochodna(x_points, ktory_wiersz):
    wiersz = []
    wiersz.append(0)

    for i in range(3):
        wiersz.append( (i+1) * (x_points[ktory_wiersz] ** (i)))

    for i in range(1, ktory_wiersz + 1):
        wiersz.append(3 * ((x_points[ktory_wiersz] - x_points[i]) ** 2))

    while len(wiersz) < len(x_points) + 2:
        wiersz.append(0)

    return wiersz

def generuj_uklad_rownan(x_points):
    n = len(x_points)
    tablica = []
    for i in range(n):
        tablica.append(generuj_wiersz(x_points, i))

    tablica.append(pochodna(x_points, 0))
    tablica.append(pochodna(x_points, len(x_points) - 1))

    return tablica

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
    #X = [round(x, 3) for x in X]
    return X

def rozwiazanie_funkcje_sklejane(x, a, x_points):
    sum = 0
    for i in range(4):
        sum += a[i] * (x**i)

    for i in range(1, len(x_points) - 1):
        if x >= x_points[i]:
            sum += a[i + 3] * (x - x_points[i])**3

    #sum = round(sum, 3)
    return sum

x_points = [-4, -2, 0, 2, 4]
y_points = [1043, 59, 3, 59, 947]
x = 3
pochodna1 = -1052
pochodna2 = 964

y_points.append(pochodna1)
y_points.append(pochodna2)

macierz = generuj_uklad_rownan(x_points)

a = eliminacja_gaussa(macierz, y_points)

print(rozwiazanie_funkcje_sklejane(x, a, x_points))