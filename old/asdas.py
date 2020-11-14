'''
for i in range(0, 3):
    for x in range(0, 4):
        a = 4 * (x + 1) * 2 * (i + 1)
        print(a, end=' ')
    print('\n', end='')
'''
'''
X = [[70, 140, 210 ],
    [140, 280, 420]]
Y = [[8, 16, 24, 32 ],[16, 32, 48, 64 ],[24, 48, 72, 96 ]]

result = [[0,0,0,0],
         [0,0,0,0]]

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
'''
x = 400
sum = 0
for i in range(0, 20):
    sum += x 
    x+=12
print(sum)