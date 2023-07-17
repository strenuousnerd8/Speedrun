def countingSort(arr):
    # Write your code here
    res = [0] * 100
    for i in arr:
        res[i] += 1
    return res


if __name__ == "__main__":

    arr = [1, 1, 3, 2, 1]

    result = countingSort(arr)

    print(result)
