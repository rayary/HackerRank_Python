def sort_order(x):
    return x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(), x


if __name__ == "__main__":
    # lowercase < uppercase < odd digits < even digits
    s = list(input())
    list.sort(s, key=sort_order)
    print(*s, sep='')
