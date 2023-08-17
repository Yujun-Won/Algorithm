words = input()
length = len(words)//10 + 1

for i in range(length):
    print(words[10*i:10*i+10])