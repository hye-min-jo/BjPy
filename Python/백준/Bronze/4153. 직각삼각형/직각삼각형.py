while True:
    a,b,c=map(int,input().split())

    a*=a
    b*=b
    c*=c

    if a==0 and b==0 and c==0:
        break

    if a+b==c or a+c==b or b+c==a:
        print("right")

    else:
        print("wrong")
    
    
