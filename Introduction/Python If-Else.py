if __name__ == '__main__':
    n = int(input())

    # if n is odd, print weird
    # if n is even and [2..5], print not weird
    # if n is even and [6..20], print weird
    # if n is even and >20, print not weird

    if n%2 == 1 or (6 <= n <= 20):
        print("Weird")
    else:
        print("Not Weird")