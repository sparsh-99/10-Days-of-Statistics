N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))
sum_x = sum([a*b for a,b in zip(X,W)])
print(round((sum_x/sum(W)),1))