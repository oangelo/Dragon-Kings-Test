#!/usr/bin/python2.7
from scipy.stats import f 
from scipy.stats import distributions
import pylab as P

def dragon_kings(data_list, n, r):
    data = list(set(data_list))
    data.sort()
    data.reverse()

    N = len(data)
    #Spacings y_k
    y = []
    for k in range(0, N-1):
        y.append(data[k] - data[k+1])
    y.append(N-1)

    z = []
    for k in range(1, N-1):
        z.append(k*y[k])

    #Test Statistics
    numerator = 0
    for i in range(0, r):
        numerator += z[i]
    numerator = numerator / float(r)

    denominator = 0.
    for i in range(r, n):
        denominator += z[i]
    denominator = denominator / float(n - r)

    T = numerator / float(denominator)
    F = distributions.f.cdf(T, 2*r, 2*(n - r));
    print "T", T, 2*r, 2*(n-r)
    p = 1 - F

    return p

file = open("data/great_britain-2008.csv")
#file = open("data/usa2010.csv")
lines = file.readlines()
file.close()
data = []
for value in lines:
    data.append(int(value))

r = 1

serie = [(n, dragon_kings(data, n, r)) for n in range(2,36)]   
for i in range(0, len(serie)):
    print serie[i][0], serie[i][1]
#P.plot([i[0] for i in serie],[i[1] for i in serie], '-o')
#P.show()
