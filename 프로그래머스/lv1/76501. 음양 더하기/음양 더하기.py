def solution(absolutes, signs):
    sum = 0
    for i in range(len(signs)):
        if signs[i] is True:
            sum += absolutes[i]
        elif signs[i] is False:
            sum += -absolutes[i]
    return sum