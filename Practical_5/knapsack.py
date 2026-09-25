def knapsack(capacity, weights, values, n):


    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]


    for i in range(1, n + 1):
        for w in range(capacity + 1):


            dp[i][w] = dp[i - 1][w]

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    values[i - 1] +
                    dp[i - 1][w - weights[i - 1]]
                )

    return dp[n][capacity]


# Input
n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))

capacity = int(input("Enter knapsack capacity: "))

result = knapsack(capacity, weights, values, n)

print("Maximum value =", result)