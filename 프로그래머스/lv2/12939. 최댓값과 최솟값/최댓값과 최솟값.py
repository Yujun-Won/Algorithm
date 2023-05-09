def solution(s):
    numList = [int(i) for i in s.split()]

    return "{} {}".format(min(numList), max(numList))
