s=list(input())

alist='abcdefghijklmnopqrstuvwxyz'

for i in alist:
    if i in s:
        print(s.index(i), end=" ")
    else:
        print(-1,end=" ")
