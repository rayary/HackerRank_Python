def swap_case(s):
    s = str(s)
    new_s = ""
    for i in s:
        if 'a' <= i <= 'z':
            new_s += i.upper()
        elif 'A' <= i <= 'Z':
            new_s += i.lower()
        else:
            new_s += i

    return new_s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)