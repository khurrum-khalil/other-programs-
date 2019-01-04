

  
x = [[4,5,6],
     [8,4,9],
     [6,2,1]]
y = [[1,1,1],
     [1,1,1],
     [1,1,1]]
res = [[0,0,0],
       [0,0,0],
       [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
       res[i][j] = x[i][j]+y[i][j]
       
for r in res:
    print(r)
