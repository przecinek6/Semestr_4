def ir_rzedow(x_points, y_points, j):
    new_tab = []
    for i in range(len(y_points) - 1):
        new_tab.append((y_points[i + 1] - y_points[i]) / (x_points[i + j + 1] - x_points[i]))
    return new_tab

def iloraz_roznicowy(x_points, y_points, x):
    sum = y_points[0]
    tmp_tab = y_points
    for i in range(len(x_points) - 1):
        tmp_tab = ir_rzedow(x_points, tmp_tab, i)
        tmp = 1
        for j in range(i + 1):
            tmp *= x - x_points[j]
        sum += tmp_tab[0] * tmp
    return sum

x_points = [-4, -2, 0, 2, 4]
y_points = [1043, 59, 3, 59, 947]
x = 3

print(round(iloraz_roznicowy(x_points, y_points, x), 4))