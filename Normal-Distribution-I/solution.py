import math

meu,std = list(map(int, input().split()))
h1_1 = float(input())
h2_1, h2_2 = list(map(float, input().split()))

def norm_cdf(x):
    erf_parameter = (x - meu) / (std * math.sqrt(2))
    return 0.5 * (1 + math.erf(erf_parameter))

result_1 = norm_cdf(h1_1)
print(round(result_1, 3))
result_2 = norm_cdf(h2_2) - norm_cdf(h2_1)
print(round(result_2, 3))