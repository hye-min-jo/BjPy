h,m=map(int,input().split())
et=int(input())

h+=et//60
m+=et%60

if m>=60:
    h+=1
    m-=60
if h>=24:
    h-=24

print(h,m)
