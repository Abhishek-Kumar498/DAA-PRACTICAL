from itertools import permutations

n = int(input("Enter number of cities: "))

print("Enter the cost matrix:")
cost = []

for i in range(n):
    cost.append(list(map(int, input().split())))

start = 0

cities = [i for i in range(n) if i != start]

min_cost = float('inf')
best_path = []

for path in permutations(cities):
    current_cost = 0
    k = start

    for city in path:
        current_cost += cost[k][city]
        k = city

    current_cost += cost[k][start]

    if current_cost < min_cost:
        min_cost = current_cost
        best_path = [start] + list(path) + [start]

print("\nMinimum travelling cost:", min_cost)
print(" ")
print("Optimal path:", end=" ")

for city in best_path:
    print(city, end=" ")
print(" ")
