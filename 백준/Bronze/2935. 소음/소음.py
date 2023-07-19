import sys

A = int(sys.stdin.readline())
oper = input()
B = int(sys.stdin.readline())

if oper == '+':
  print(A+B)
elif oper == '*':
  print(A*B)