if __name__ == "__main__":
    n, m = map(int, input().split())
    attribute = []
    for _ in range(n):
        attribute.append(list(map(int, input().split())))
    k = int(input())

    attribute = sorted(attribute, key=lambda a: a[k])

    for arg in attribute:
        print(*arg)
