def rp_rzedow(y_points):
    new_tab = []
    for i in range(len(y_points) - 1):
        new_tab.append(y_points[i+1] - y_points[i])
    return new_tab

def silnia(n): return n*silnia(n-1) if n > 1 else 1
def roznice_progresywne(x_points, y_points, x):
    sum = y_points[0]
    h = x_points[1] - x_points[0]
    tmp_tab = y_points
    for i in range(1, len(y_points)):
        tmp_tab = rp_rzedow(tmp_tab)
        tmp = tmp_tab[0] / (silnia(i) * (h**i))
        tmp2 = 1
        for j in range(i):
            tmp2 *= (x - x_points[j])
        sum += tmp * tmp2
    return sum

x_points = [-4, -2, 0, 2, 4]
y_points = [1043, 59, 3, 59, 947]
x = 3

print(roznice_progresywne(x_points, y_points, x))