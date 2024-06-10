def var(x, last_x, e):
    counter = 0
    for i in range(len(x)):
        tmp = abs(x[i] - last_x[i])
        if tmp < e:
            counter += 1

    if counter == 3:
        return False
    else:
        return True

def fun(uklad_rownan, e):
    x = [0, 0, 0]
    last_x = [10, 10, 10]
    counter = 0
    tmp = 1

    for i in range(len(uklad_rownan)):
        for j in range(len(uklad_rownan[i])):
            if uklad_rownan[i][i] != 1:
                tmp = uklad_rownan[i][i]
            uklad_rownan[i][j] = uklad_rownan[i][j] / tmp
            if i != j and j != len(uklad_rownan[i]) - 1:
                uklad_rownan[i][j] *= -1


    while var(x, last_x, e):
        counter += 1
        for i in range(len(x)):
            last_x[i] = x[i]

        for i in range(len(uklad_rownan)):
            sum = uklad_rownan[i][len(uklad_rownan)]

            for j in range(len(uklad_rownan)):
                if i != j:
                    sum += uklad_rownan[i][j] * last_x[j]
                x[i] = sum

    return counter, x


uklad_rownan = [[3, 1, 2, 5],
                [1, -4, 1, -7],
                [1, 2, 3, 2]]
e = 0.000001

i, x = fun(uklad_rownan, e)
print("Numer iteracji = ", i)
print("Przybliżenie = ", x)