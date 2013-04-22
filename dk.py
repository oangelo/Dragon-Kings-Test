#!/usr/bin/python2.7
from scipy.stats import f 
import pylab as P
from math import log
from sys import argv
from sys import exit 

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

if __name__ == '__main__':
    if len(argv) < 4:
        print "Please enter the following arguments:"
        print argv[0],"<file name> <number of DK [r]> <number of data [n]>"
        print """Case the data is a power law, add "pl" to the list of arguments"""
        exit()
    r = int(argv[2]) 
    N = int(argv[3])

    file = open(argv[1])
    lines = file.readlines()
    file.close()
    data = []
    if "pl" in argv:
        for value in lines:
            data.append(log(float(value)))
    else:
        for value in lines:
            data.append(log(float(value)))


    serie = [(n, dragon_kings(data, n, r)) for n in range(r + 1, N)]   
    for i in range(0, len(serie)):
        print serie[i][0], serie[i][1]
