INF = 99999
n = int(input("Enter number of vertices: "))

print("Enter the adjacency matrix (use 99999 for INF):")
graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j],
                              graph[i][k] + graph[k][j])

print("\nShortest Distance Matrix:")

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print("INF", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
