from collections import Counter

if __name__ == "__main__":
    x = int(input())
    stock = Counter(map(int, input().split()))
    n = int(input())

    revenue = 0
    for _ in range(n):
        size, price = map(int,input().split())
        if stock[size] >= 1:
            revenue += price
            stock.subtract({size:1})

    print(revenue)