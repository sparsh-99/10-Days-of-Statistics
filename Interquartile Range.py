from statistics import median

N = int(input())
X = list(map(int, input().split()))
F = list(map(int, input().split()))
S = []

for i in range(N):
    for f in range(F[i]):
        S.append(X[i])

S.sort()

m = len(S)//2 

L_half = S[:m]
U_half = S[-m:]

q1 = int(median(L_half))
q3 = int(median(U_half))

print("{0:0.1f}".format(q3-q1))
