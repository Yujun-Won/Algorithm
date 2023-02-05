aeiou = ['A', 'E', 'I', 'O', 'U',
         'a', 'e', 'i', 'o', 'u']

while True:
  cnt = 0
  sentence = input()
  
  if sentence == '#':
    break
  else:
    for i in sentence:
      if i in aeiou:
        cnt += 1
  print(cnt)