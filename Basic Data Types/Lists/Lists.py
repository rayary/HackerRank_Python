def insert(l, i, n):
    l.insert(i, n)


def printlist(l):
    print(l)


def remove(l, n):
    l.remove(n)


def append(l, n):
    l.append(n)


def sort(l):
    l.sort()


def pop(l):
    l.pop()


def reverse(l):
    l.reverse()


if __name__ == '__main__':
    n = int(input())
    l = []

    options = {
        "insert": insert,
        "print": printlist,
        "remove": remove,
        "append": append,
        "sort": sort,
        "pop": pop,
        "reverse": reverse,
    }

    for _ in range(0,n):
        # read in command
        args = input().split()
        args[1:] = map(int, args[1:])
        try:
            options[args[0]](l, *args[1:])
        except:
            print("operation not allowed")


