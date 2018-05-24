from itertools import permutations

if __name__ == "__main__":
    arg = input().split()
    word = sorted(arg[0])
    k = int(arg[1])

    print(*[''.join(i) for i in permutations(word,k)], sep='\n')

