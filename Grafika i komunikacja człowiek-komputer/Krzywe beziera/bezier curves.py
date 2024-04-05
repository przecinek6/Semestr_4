import matplotlib.pyplot as plt
import numpy as np

def krzywa_bezier(punkty, t):
    if len(punkty) == 1:
        return punkty[0]
    else:
        return (1 - t) * np.array(krzywa_bezier(punkty[:-1], t)) + t * np.array(krzywa_bezier(punkty[1:], t))

punkty = [
    [(4, 0), (4, 2), (4, 4), (4, 6)],
    [(4, 6), (5, 3.75)],
    [(5, 3.75), (6, 6)],
    [(6, 6), (6, 4), (6, 2), (6, 0)],
    [(6, 0), (5.75, 0)],
    [(5.75, 0), (5.75, 2), (5.75, 3.75)],
    [(5.75, 3.75), (5, 2.25)],
    [(5, 2.25), (4.25, 3.75)],
    [(4.25, 3.75), (4.25, 2), (4.25, 0)],
    [(4.25, 0), (4, 0)],

    [(7, 0), (7, 2), (7, 4), (7, 6)],
    [(7, 6), (8, 3.75)],
    [(8, 3.75), (9, 6)],
    [(9, 6), (9, 4), (9, 2), (9, 0)],
    [(9, 0), (8.75, 0)],
    [(8.75, 0), (8.75, 2), (8.75, 3.75)],
    [(8.75, 3.75), (8, 2.25)],
    [(8, 2.25), (7.25, 3.75)],
    [(7.25, 3.75), (7.25, 2), (7.25, 0)],
    [(7.25, 0), (7, 0)]
]

t_values = np.linspace(0, 1)

plt.figure(figsize=(6, 4))

for point_set in punkty:
    punkty_krzywej = [krzywa_bezier(point_set, t) for t in t_values]
    plt.plot(*zip(*punkty_krzywej), color='blue')
    plt.scatter(*zip(*point_set), color='red')


plt.title("Inicjały z Krzywych Béziera")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
