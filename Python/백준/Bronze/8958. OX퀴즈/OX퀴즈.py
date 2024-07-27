tc=int(input())

for i in range(tc):
    ox=input()
    
    s=0
    sus=0

    for j in ox:
        if j=='O':
            s+=1
        else:
            s=0
        sus+=s
    print(sus)
    
