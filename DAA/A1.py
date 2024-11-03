#  Write a program non-recursive and recursive program to calculate Fibonacci numbers and analyze their time and space complexity.
COUNT = 0

def recur_fibo(n):
    global COUNT
    COUNT += 1  
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

def fib_iterative(n):
    global COUNT
    COUNT = 0
    first, sec = 0, 1
    series = []
    if n <= 0:
        return "Please enter a positive integer.", COUNT
    elif n == 1:
        series = [0]
        COUNT += 1  
        return series, COUNT
    else:
        for _ in range(n):
            series.append(first)
            COUNT += 1  
            nth = first + sec
            first, sec = sec, nth
            COUNT += 3 

    return series, COUNT

def main():
    while True:
        global COUNT
        print("\nMenu:")
        print("1. Fibonacci Series using Iterative approach")
        print("2. Fibonacci Series using Recursive approach")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1 or choice == 2:
            n = int(input("Enter the number of terms (n): "))
            
            if n <= 0:
                print("Please enter a positive integer.")
                continue

            COUNT = 0

            if choice == 1:
                # Iterative Fibonacci
                series, steps = fib_iterative(n)
                print("Fibonacci Series:", series)
                print("Steps required using Counter:", steps)

            elif choice == 2:
                # Recursive Fibonacci
                series = []
                for i in range(n):
                    series.append(recur_fibo(i))
                print("Fibonacci Series:", series)
                print("Steps required using Counter:", COUNT)

        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
