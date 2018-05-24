def split_and_join(line):
    # string default split to list of characters, so split them into list of word
    line = line.split(" ")
    line = "-".join(line)
    return line


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)