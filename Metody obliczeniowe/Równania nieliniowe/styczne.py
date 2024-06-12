def f(x):
    return x**2 + 4.1*x - 6.36

def f1(x):
    return 2*x + 4.1

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
    while abs(f(x)) >= e and abs(x - xn) >= e:
        i += 1
        xn = x
        x = xn - (f(xn) / f1(xn))

    return i, x


a = -4
b = 5
e = 0.01

i, x = styczne(a, b, e)

print("Nr iteracji = ", i)
print("Rozwiazanie = ", x)