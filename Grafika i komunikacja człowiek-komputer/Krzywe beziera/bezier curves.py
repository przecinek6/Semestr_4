import matplotlib.pyplot as plt
import numpy as np

def krzywa_bezier(punkty, t):
    if len(punkty) == 1:
        return punkty[0]
    else:
        return (1 - t) * np.array(krzywa_bezier(punkty[:-1], t)) + t * np.array(krzywa_bezier(punkty[1:], t))

punkty = [
    [(4, 0), (4, 2), (4, 4), (4, 6)],
    [(4, 6), (5, 4)],
    [(5, 4), (6, 6)],
    [(6, 6), (6, 4), (6, 2), (6, 0)],
    [(6, 0), (5.5, 0)],
    [(5.5, 0), (5.5, 2), (5.5, 4)],
    [(5.5, 4), (5, 3)],
    [(5, 3), (4.5, 4)],
    [(4.5, 4), (4.5, 2), (4.5, 0)],
    [(4.5, 0), (4, 0)],
    [(7, 0), (7, 2), (7, 4), (7, 6)],
    [(7, 6), (8, 4)],
    [(8, 4), (9, 6)],
    [(9, 6), (9, 4), (9, 2), (9, 0)],
    [(9, 0), (8.5, 0)],
    [(8.5, 0), (8.5, 2), (8.5, 4)],
    [(8.5, 4), (8, 3)],
    [(8, 3), (7.5, 4)],
    [(7.5, 4), (7.5, 2), (7.5, 0)],
    [(7.5, 0), (7, 0)]
]

punkty2 = [
    [(4.25, 0.5), (4.25, 2.5), (4.25, 5)],
    [(4.25, 5), (5, 3.5)],
    [(5, 3.5), (5.75, 5)],
    [(5.75, 5), (5.75, 2.5), (5.75, 0.5)],
    [(7.25, 0.5), (7.25, 2.5), (7.25, 5)],
    [(7.25, 5), (8, 3.5)],
    [(8, 3.5), (8.75, 5)],
    [(8.75, 5), (8.75, 2.5), (8.75, 0.5)]
]

t_values = np.linspace(0, 1)

for point_set in punkty:
    punkty_krzywej = [krzywa_bezier(point_set, t) for t in t_values]
    plt.plot(*zip(*punkty_krzywej), color='red')

for point_set in punkty2:
    punkty_krzywej = [krzywa_bezier(point_set, t) for t in t_values]
    plt.plot(*zip(*punkty_krzywej), color='darkred')

plt.show()