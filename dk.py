#!/usr/bin/python2.7
from scipy.stats import f

def dragon_kings(data, n, r):
    data.sort()
    data.reverse()

    N = len(data)
    #Spacings y_k
    y = []
    for k in range(1, N-1):
        y.append(data[k] - data[k-1])
    y.append(N-1)

    z = []
    for k in range(1, N-1):
        z.append(k*y[k])

    #Test Statistics
    numerator = 0
    for i in range(0, r):
        numerator += z[i]
    numerator /= r

    denominator = 0
    for i in range(r, n):
        denominator += z[i]
    denominator /= (n - r)

    T = numerator / float(denominator)
    F = f.cdf(T, 2*r, 2*(n - r));
    p = 1 - F

    return p

file = open("data/great_britain-2008.csv")
lines = file.readlines()
file.close()
data = []
for value in lines:
    data.append(int(value))

r = 1
for n in range(2, 35):
    print n, dragon_kings(data, n, r)   
