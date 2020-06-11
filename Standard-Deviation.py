N = int(input())
X = list(map(int, input().split()))
mean = sum(X)/N
variance = sum([((x-mean)**2) for x in X]) / N
stddev = variance**0.5
print("{0:0.1f}".format(stddev))
