def average(array):
    # your code goes here
    array = set(array)
    average = sum(array)/len(array)

    L = [ {'id': 1, 'name': 'john', 'age': 34},
          {'id': 1, 'name': 'john', 'age': 34},
          {'id': 2, 'name': 'hanna', 'age': 30},]
    print({v['id']: v for v in L})
    average = list({v['id']: v for v in L}.values())

    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)