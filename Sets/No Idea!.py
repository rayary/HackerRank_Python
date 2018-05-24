if __name__ == "__main__":
    n, m = (map(int, input().split()))
    arr = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
    happiness = 0

    # for all numbers in set_a in array, happiness++
    # for all numbers in set_b in array, happiness--
    for i in arr:
        if (i in set_a):
            happiness += 1
        if (i in set_b):
            happiness -= 1

    print(happiness)