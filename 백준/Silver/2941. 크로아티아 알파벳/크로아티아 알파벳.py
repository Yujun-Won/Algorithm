import sys

alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

words = sys.stdin.readline().rstrip()
cnt = 0
i = 0

while i < len(words):
    if words[i:i+2] in alphabets:
        i += 2
        cnt += 1
    elif words[i:i+3] in alphabets:
        i += 3
        cnt += 1
    else:
        i += 1
        cnt += 1

print(cnt)
