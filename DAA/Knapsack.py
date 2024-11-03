from queue import PriorityQueue

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

class Node:
    def __init__(self, level, profit, weight):
        self.level = level      # Level of the node in the decision tree
        self.profit = profit    # Profit of nodes on the path from root to this node
        self.weight = weight    # Total weight at the node

    def __lt__(self, other):
        return other.weight < self.weight  # Compare nodes based on weight in descending order

def bound(u, n, W, arr):
    # Calculate upper bound of profit in subtree rooted with 'u'
    if u.weight >= W:
        return 0

    profit_bound = u.profit
    j = u.level + 1
    total_weight = u.weight

    # Greedily add items to the knapsack until the weight limit is reached
    while j < n and total_weight + arr[j].weight <= W:
        total_weight += arr[j].weight
        profit_bound += arr[j].value
        j += 1

    # If there's still room, add the fractional part of the next item
    if j < n:
        profit_bound += int((W - total_weight) * arr[j].value / arr[j].weight)

    return profit_bound

def knapsack(W, arr, n):
    # Sort items by value/weight ratio in decreasing order
    arr.sort(key=lambda x: x.value / x.weight, reverse=True)
    
    priority_queue = PriorityQueue()
    u = Node(-1, 0, 0)  # Dummy node at the root
    priority_queue.put(u)

    max_profit = 0

    while not priority_queue.empty():
        u = priority_queue.get()

        if u.level == -1:
            v = Node(0, 0, 0)  # Starting node
        elif u.level == n - 1:
            continue
        else:
            v = Node(u.level + 1, u.profit, u.weight)  # Node without considering the next item

        # Consider adding the next item
        v.weight += arr[v.level].weight
        v.profit += arr[v.level].value

        if v.weight <= W and v.profit > max_profit:
            max_profit = v.profit

        v_bound = bound(v, n, W, arr)
        if v_bound > max_profit:
            priority_queue.put(v)

        # Consider the node without adding the next item
        v = Node(u.level + 1, u.profit, u.weight)
        v_bound = bound(v, n, W, arr)
        if v_bound > max_profit:
            priority_queue.put(v)

    return max_profit

# Get user input for items and capacity
def get_user_input():
    W = float(input("Enter the capacity of the knapsack: "))
    n = int(input("Enter the number of items: "))
    
    items = []
    for i in range(n):
        weight = float(input(f"Enter the weight of item {i+1}: "))
        value = float(input(f"Enter the value of item {i+1}: "))
        items.append(Item(weight, value))
    
    return W, items, n

# Driver code
W, arr, n = get_user_input()
max_profit = knapsack(W, arr, n)
print("Maximum possible profit =", max_profit)
