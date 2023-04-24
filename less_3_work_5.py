import numpy as np

N = 5
M = 4
a = np.zeros((N, M))

for i in range(1, N+1):
    for j in range(1, M+1):
        a[i-1, j-1] = np.sin(N*1 + M*j)


a[a < 0] = 0

# меняю столбцы местами
a[:, [0,1]] = a[:, [1, 0]]

print(a)