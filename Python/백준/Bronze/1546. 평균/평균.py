n=int(input())

subjects=list(map(int,input().split()))


m=max(subjects)

for i in range(0,n):
    subjects[i]=subjects[i]/m*100

print(sum(subjects)/n)


