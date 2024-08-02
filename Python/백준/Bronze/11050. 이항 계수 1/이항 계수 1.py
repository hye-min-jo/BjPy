N,K=map(int,input().split())

Np=1
Kp=1
NmK=1

for i in range(1,N+1):
    Np*=i
    
for j in range(1,K+1):
    Kp*=j

for a in range(1,N-K+1):
    NmK*=a

print(Np//(Kp*NmK))
