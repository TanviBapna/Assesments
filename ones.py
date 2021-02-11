n=10
m=10
grid=[[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0,0,0],[1,1,1,0,0,0,0,1,1,1],[1,1,0,0,1,0,0,1,1,1],[1,0,1,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1]]
queries=[1,10,20,2,6]
#for i in range(n):
#    l.append(list(map(int,input().split())))
def check(i,j,l):
    if i<0 or j<0 or i>=n or j>=m or l[i][j]==-1 or l[i][j]==0:
        return 0
    else:
        l[i][j]=-1
        return 1+(check(i,j+1,l)+check(i,j-1,l)+check(i+1,j,l)+check(i-1,j+1,l))

res= -1
result=[]
for i in range(n):
    for j in range(m):
        if grid[i][j]==1:
            res=check(i,j,grid)
            print(res)
            result.append(res)
print(result)
queries=[1,10,20,2,6]
dict1={}
for i in result:
    if i not in dict1.keys():
        dict1[i]=1
    else:
        dict1[i] = dict1[i]+1
        
print(dict1)       
res=[]        
for i in queries:
    if i in dict1:
      res.append(dict1[i]) 
    else:
      res.append(0)
print(queries)
print(res)