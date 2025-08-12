n1=int(input())
p1=list(map(int,input().split()))
n2=int(input())
p2=list(map(int,input().split()))
res=[0]*(n1+n2-1)
for i in range(n1):
    for j in range(n2):
        res[i+j]+=p1[i]*p2[j]
print(*res)
