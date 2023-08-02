def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        temp = [arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))]
        result.append(temp)

    return result