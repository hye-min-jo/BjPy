n=int(input())
ts=list(map(int,input().split()))

t,p=map(int,input().split())

tm=0

for i in range(len(ts)):
    if ts[i]%t==0:
        tm+=int(ts[i]/t)

    else:
        tm+=int(ts[i]/t+1)
print(tm)
print(n//p,n%p)
        
    
