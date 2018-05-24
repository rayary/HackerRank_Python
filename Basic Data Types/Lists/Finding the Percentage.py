from functools import reduce

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    total = reduce((lambda x , y: x + y), student_marks[query_name])
    print("{0:.2f}".format(total / len(student_marks[query_name])))