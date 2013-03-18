#!/usr/bin/python2.7
from scipy.stats import f 
import pylab as P

def dragon_kings(data_list, n, r):
    data = data_list
    data.sort()
    data.reverse()

    y = [(data[k] - data[k + 1]) for k in range(n)]
    z = [(k+1)*y[k] for k in range(n)]

    chi1 = 0.0
    for i in range(r):
        chi1 += z[i]
    chi1 /= r 

    chi2 = 0.0
    for i in range(r, n):
        chi2 += z[i]
    chi2 /= (n - r)

    T = chi1 / chi2
    
    p = 1 - f.cdf(T, 2*r, 2*(n - r))

    return p

file = open("data/great_britain-2008.csv")
#file = open("data/usa2010.csv")
lines = file.readlines()
file.close()
data = []
for value in lines:
    data.append(int(value))

r = 1

serie = [(n, dragon_kings(data, n, r)) for n in range(r + 1, 36)]   
for i in range(0, len(serie)):
    print serie[i][0], serie[i][1]

for i in range(10):
    print "# ", data[i]
#P.plot([i[0] for i in serie],[i[1] for i in serie], '-o')
#P.show()
