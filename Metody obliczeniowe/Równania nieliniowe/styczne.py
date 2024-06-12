def f(x):
    return x**2 + x - 5

def f1(x):
    return 2*x + 1

def f2(x):
    return 2

def styczne(a, b, e):
    if f(a) * f(b) >= 0:
        print("Warunek konieczny nie spełniony")

    if f1(a) * f1(b) < 0 or f2(a) * f2(b) < 0:
        print("Warunki zbieżności nie są spełnione")

    if f2(a) >= 0 and f(a) >= 0:
        xn = a
    else:
        xn = b

    i = 1
    x = xn - (f(xn) / f1(xn))
    while abs(f(x)) >= e or abs(x - xn) >= e:
        i += 1
        xn = x
        x = xn - (f(xn) / f1(xn))

    return i, x


a = 1
b = 2
e = 0.01

i, x = styczne(a, b, e)

print("Nr iteracji = ", i)
print("Rozwiazanie = ", x)