n=int(input())
slist=list(map(int,input().split()))
c=0

for i in slist:
    for j in range(2,i+1):
        if i%j==0:
            if i==j:
                c+=1
            break

print(c)
