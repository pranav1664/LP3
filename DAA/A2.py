# Write a program to implement Huffman Encoding using a greedy strategy.

import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printNodes(node, val=''):
    newVal = val + str(node.huff)

    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)

    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")

  
def huffman_encoding(chars, freq):
    nodes = []

    for x in range(len(chars)):
        heapq.heappush(nodes, Node(freq[x], chars[x]))

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1

        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newNode)

    print("Huffman Codes for the given characters:")
    printNodes(nodes[0])


def main():
    num = int(input("Enter the number of characters: "))
    
    chars = []
    freq = []
    
    for i in range(num):
        char = input(f"Enter character {i+1}: ")
        frequency = int(input(f"Enter frequency of '{char}': "))
        chars.append(char)
        freq.append(frequency)
    
    huffman_encoding(chars, freq)

if __name__ == "__main__":
    main()