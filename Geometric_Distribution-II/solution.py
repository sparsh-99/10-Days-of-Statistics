def g(n, p):
    return ((1-p)**(n-1))*p

nu, de = list(map(int,input().split()))
p = nu/de
n = int(input())
print(round(sum([g(i,p) for i in range(1,n+1)]),3))
