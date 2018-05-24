if __name__ == '__main__':
    m = int(input())
    set_m = set(map(int, input().split()))
    n = int(input())
    set_n = set(map(int, input().split()))

    print(*sorted(set_m.difference(set_n).union(set_n.difference(set_m))), sep='\n')