valDict = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4,
           'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}
deciDict = {'black':1, 'brown':10, 'red':1e2, 'orange':1e3, 'yellow':1e4,
            'green':1e5, 'blue':1e6, 'violet':1e7, 'grey':1e8, 'white':1e9}
val1 = input()
val2 = input()
deci = input()

result = int((valDict[val1] * 10 + valDict[val2]) * deciDict[deci])
print(result)