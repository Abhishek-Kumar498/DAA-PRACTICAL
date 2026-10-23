V = 5

edges = [
    (2, 0, 1),
    (3, 1, 2),
    (6, 0, 3),
    (8, 1, 3),
    (5, 1, 4),
    (7, 2, 4),
    (9, 3, 4)
]

edges.sort()

parent = list(range(V))

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(u, v):
    root_u = find(u)
    root_v = find(v)

    if root_u != root_v:
        parent[root_v] = root_u
        return True
    return False

mst_cost = 0
count = 0

print("Edge : Weight")

for weight, u, v in edges:
    if union(u, v):
        print(f"{u} - {v} : {weight}")
        mst_cost += weight
        count += 1

        if count == V - 1:
            break

print("Minimum Cost:", mst_cost)
