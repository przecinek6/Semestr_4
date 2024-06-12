def f(x):
    return x**2 + 4.1*x - 6.36

def bisekcja(a, b, e):
    if f(a) * f(b) >= 0:
        return None, "Warunek konieczny nie spełniony"

    i = 0

    while (a + b) / 2 >= 0:
        i += 1
        x_sr = (a + b) / 2

        if f(x_sr) == 0 or abs(f(x_sr)) < e:
            return i, x_sr

        if f(x_sr) * f(a) < 0:
            b = x_sr
        else:
            a = x_sr

a = -4
b = 5
e = 0.01

i, x = bisekcja(a, b, e)

print("Nr iteracji = ", i)
print("Rozwiazanie = ", x)