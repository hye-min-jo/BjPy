n,m=map(int,input().split())
box=list(range(1,n+1))

for _ in range(m):
    i,j=map(int,input().split())
    box[i-1:j]=box[i-1:j][::-1]

for a in range(n):
    print(box[a],end=' ')
