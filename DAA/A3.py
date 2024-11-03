# Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy. 

def knapsack_dp(weights, values, capacity):
    n = len(values)
    
    dp = [[0 for w in range(capacity + 1)] for i in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp, dp[n][capacity]

def print_selected_items(dp, weights, values, capacity):
    n = len(values)
    w = capacity
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weights[i - 1]

    print(f"Selected items : {selected_items[::-1]}")
    return selected_items

def main():
    n = int(input("Enter number of items: "))
    weights = []
    values = []
    
    for i in range(n):
        weight = int(input(f"Enter weight of item {i+1}: "))
        value = int(input(f"Enter value of item {i+1}: "))
        weights.append(weight)
        values.append(value)

    capacity = int(input("Enter capacity of knapsack: "))

    dp, max_value = knapsack_dp(weights, values, capacity)
    print(f"Maximum value in Knapsack: {max_value}")

    print_selected_items(dp, weights, values, capacity)

if __name__ == "__main__":
    main()
