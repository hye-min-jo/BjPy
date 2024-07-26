x=int(input())
n=int(input())
sum1=0

for i in range(1,n+1):
    a,b=map(int,input().split())
    sum1+=a*b

if x==sum1:
    print("Yes")
else:
    print("No")
