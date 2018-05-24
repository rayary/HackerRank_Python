from itertools import groupby

if __name__ == "__main__":
    arg = input()
    # square bracket needed below due to LIST comprehension use
    print(*[(len(list(g)), int(k)) for k, g in groupby(arg)])
    # for k, g in groupby(arg):
    #   print((len(list(g)), int(k)), end=' ')
