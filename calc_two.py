#!/usr/bin/python

import random

def f_greedy(r1, r2, hbuf, total):
    remain = hbuf
    h1 = 0
    h2 = 0
    cost = 0
#    print "total, remain, h1, h2, cost"
    while (total > remain):
        h1_new = 1.0 * remain * r1 / (r1 + r2)
        h2_new = remain  - h1_new
#* r2 / (r1 + r2)
        total -= remain
        h1 += h1_new
        h2 += h2_new
 #       print total, remain, h1, h2, cost
        if (h1 > h2):
            remain = h1
            h1 = 0
        else:
            remain = h2
            h2 = 0
        cost+=1
        if (remain == 0): 
            break
    return cost

def f_rand(r1, r2, hbuf, total):
    remain = hbuf
    h1 = 0
    h2 = 0
    cost = 0
#    print "total, remain, h1, h2, cost"
    while (total > remain):
        h1_new = 1.0 * remain * r1 / (r1 + r2)
        h2_new = remain  - h1_new
#* r2 / (r1 + r2)
        total -= remain
        h1 += h1_new
        h2 += h2_new
 #       print total, remain, h1, h2, cost
        if (bool(random.getrandbits(1)) & (h1 != 0)):
            remain = h1
            h1 = 0
        else:
            remain = h2
            h2 = 0
        cost+=1
        if (remain == 0): 
            break
    return cost

        

if __name__ == "__main__":
    print "main"
    r1 = 10
    r2 = 90
    hbuf = 100
    total = 5000
    print "greedy", f_greedy(r1, r2, hbuf, total)
    print "rand", f_rand(r1, r2, hbuf, total)
