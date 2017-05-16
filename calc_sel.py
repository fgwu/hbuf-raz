#!/usr/bin/python

import random

def sim(r1, r2, hbuf, total, sel_func):
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
        if (sel_func(h1,h2)):
            remain = h1
            h1 = 0
        else:
            remain = h2
            h2 = 0
        cost+=1
        if (remain == 0): 
            break
    return cost



#        if (bool(random.getrandbits(1)) & (h1 != 0)):

def sel_greedy(h1, h2):
    return h1 > h2

def sel_rand(h1, h2):
    return bool(random.getrandbits(1)) & (h1 != 0)
       

if __name__ == "__main__":
    print "main"
    r1 = 10
    r2 = 90
    hbuf = 100
    total = 1000000
    print "greedy", sim(r1, r2, hbuf, total, sel_greedy)
    print "rand", sim(r1, r2, hbuf, total, sel_rand)
