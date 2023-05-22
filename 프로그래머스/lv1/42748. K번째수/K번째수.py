def solution(array, commands):
    answer = []
    
    for idx in range(len(commands)):
        i, j, k = commands[idx][0], commands[idx][1], commands[idx][2]
        temp = sorted(array[i-1:j])
        answer.append(temp[k-1])
        
    return answer