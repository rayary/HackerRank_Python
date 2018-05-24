from collections import OrderedDict

if __name__ == "__main__":
    sales = OrderedDict()

    for _ in range(int(input())):
        args = (input().split())
        item, quantity = ' '.join(args[:-1]), int(args[-1])
        if item in sales:
            sales[item] += quantity
        else:
            sales[item] = quantity

    for v, k in sales.items():
        print(v, k)