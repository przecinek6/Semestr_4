def IlorazRoznicowy(*x):
    if len(x) > 1:
        return (IlorazRoznicowy(*x[1:]) - IlorazRoznicowy(*x[:-1])) / (x[len(x) - 1] - x[0])
    else:
        return x[0]

print(IlorazRoznicowy(0, 1))