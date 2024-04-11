def lagrange(x_coord, y_coord, x):
    sum = 0
    for i in range ( len(x_points) ):
        tmp = y_coord[i]
        for j in range ( len(x_points) ):
            if j != i:
                tmp *= (x - x_coord[j]) / (x_coord[i] - x_coord[j])
        sum += tmp
    return sum

x_points = [-4, -2, 0, 2, 4]
y_points = [1043, 59, 3, 59, 947]
x = 3

print(round(lagrange(x_points, y_points, x), 2))