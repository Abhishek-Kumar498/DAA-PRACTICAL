
V = 5

G = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

selected = [False] * V
selected[0] = True

edges = 0
total_cost = 0

print("Edge : Weight")

while edges < V - 1:
    minimum = None
    x = y = 0

    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and G[i][j] != 0:
                    if minimum is None or G[i][j] < minimum:
                        minimum = G[i][j]
                        x, y = i, j

    if minimum is None:
        print("Graph is disconnected!")
        break

    print(f"{x} - {y} : {G[x][y]}")
    total_cost += G[x][y]
    selected[y] = True
    edges += 1

print("Minimum Cost:", total_cost)
