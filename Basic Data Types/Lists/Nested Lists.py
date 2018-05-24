if __name__ == '__main__':
    lowest = secondlowest = float('inf')
    studentlist = []
    namelist = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < secondlowest:
            if score < lowest:
                lowest, secondlowest = score, lowest
            elif (score != lowest):  # incase the there are multiple lowest number
                secondlowest = score

        studentlist.append([name, score])

    for name in sorted(x[0] for x in studentlist if x[1] == secondlowest):
        print(name)


    # for student in studentlist:
    #     if student[1] == secondlowest:
    #         namelist.append(student[0])
    #
    # print(*sorted(namelist), sep='\n')
