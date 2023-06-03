def solution(arr):
    if len(arr) == 1:
        arr.pop()
        arr.append(-1)
    else:
        minVal = min(arr)
        arr.remove(minVal)
        
    return arr