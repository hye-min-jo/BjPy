test=int(input())

for i in range(1,test+1):
        h,w,n=map(int,input().split())
        
        hi=n%h
        wi=n//h+1

        if hi ==0:
            hi=h
            wi-=1

        print(hi*100+wi)
