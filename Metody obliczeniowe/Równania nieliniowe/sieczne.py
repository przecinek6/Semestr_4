def f(x):
    return x**2 + 4.1*x - 6.36

def f1(x):
    return 2*x + 4.1

def f2(x):
    return 2

def sieczne(a, b, e):
    if f(a) * f(b) >= 0:
        return None, "Warunek konieczny nie spełniony"

    if f2(a) >= 0 and f(a) >= 0:
        xn = b
        pom = True
    else:
        xn = a
        pom = False

    i = 1
    if pom:
        x = xn - ((f(xn) / (f(xn) - f(a))) * (xn - a))
    else:
        x = xn - ((f(xn) / (f(b) - f(xn))) * (b - xn))

    while abs(f(x)) >= e and abs(x - xn) >= e:
        i += 1
        xn = x
        if pom:
            x = xn - ((f(xn) / (f(xn) - f(a))) * (xn - a))
        else:
            x = xn - ((f(xn) / (f(b) - f(xn))) * (b - xn))

    return i, x

a = -4
b = 5
e = 0.01

i, x = sieczne(a, b, e)

print("Nr iteracji = ", i)
print("Rozwiazanie = ", x)