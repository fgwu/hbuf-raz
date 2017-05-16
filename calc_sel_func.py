#!/usr/bin/python

import random

def sim(rlist, hbuf, total, sel_func):
    remain = hbuf
    hlist = [0 for r in rlist]
    rsum = sum(rlist)
    rlist_norm = [1.0*r/rsum for r in rlist]
#    print 'rlist_norm', rlist_norm
    cost = 0
    while (total > remain):
        hlist_new = [1.0* remain *  r for r in rlist_norm]
#        print "remain, hlist_new", remain, hlist_new
        hlist = map(sum, zip(hlist, hlist_new))
#        print "hlist", hlist
        total -= remain

        cand_idx = sel_func(hlist)
        remain = hlist[cand_idx]
        hlist[cand_idx] = 0

        cost+=1

    return cost



#        if (bool(random.getrandbits(1)) & (h1 != 0)):


def sel_greedy(hlist):
    val, idx = max((val, idx) for (idx, val) in enumerate(hlist))
#    print "selected", idx, val
    return idx

def sel_rand(hlist):
    idx =  random.randrange(len(hlist))
 #   print "selected", idx, hlist[idx]
    return idx
       

if __name__ == "__main__":
    print "main"
#    rlist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    rlist = [1,1,1,1,1,1,1,1,1,1,1,1,1]
    hbuf = 100
    total = 1000000
    print "greedy", sim(rlist, hbuf, total, sel_greedy)
    print "rand", sim(rlist, hbuf, total, sel_rand)
