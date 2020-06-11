from statistics import median

N = int(input())
X = sorted(list(map(int,input().split())))
print(int(median(X[:N//2])))
print(int(median(X)))
print(int(median(X[(N+1)//2:])))