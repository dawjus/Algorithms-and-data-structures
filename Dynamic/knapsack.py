def knapsack(P, W, maxW):
    n = len(P)    #P- przedmioty , W- wagi
    F = [[0] * (maxW + 1) for _ in range(n)]
    for w in range(W[0], maxW + 1):
        F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, maxW + 1):
            F[i][w] = F[i - 1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i])
    res = F[n-1][maxW]
    w = maxW
    sol = []
    for i in range(n-1, -1, -1):
        if res <= 0:
            break
        if res == F[i - 1][w]:
            continue
        else:
            sol.append(i)
            res = res - P[i]
            w = w - W[i]

    return sol, F[n - 1][maxW], F