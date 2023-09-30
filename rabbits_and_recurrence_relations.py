

def rabbits(N, k, n, a_n_2, a_n_1):
    if n >= N:
        return a_n_1 + k * a_n_2

    return rabbits(N, k, n + 1, a_n_1, a_n_1 + k * a_n_2)


N = 5
k = 3
a_1 = 1
a_2 = 1
print(rabbits(N, k, 3, a_1, a_2))
