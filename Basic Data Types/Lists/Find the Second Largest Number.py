if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # note, map returns a iterator object
    #set([iterable])

    print(sorted(set(arr))[-2])