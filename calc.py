#!/usr/bin/python

import random

def sim(rlist, clist, hbuf, total, sel_func, logfile):
    hbuf_left = hbuf
    total_left = total
    slist = [0 for r in rlist] # space list
    rsum = sum(rlist)
    rlist_norm = [1.0*r/rsum for r in rlist] # normalized injection rate list
    cost = 0
    with open(logfile+".csv", "a+") as f:
        f.write(str(total - total_left) +  ", "+ str(cost) + ", " + "-1" + ", " +  "-1" + "\n")
        output_str = "{},{},{},{},{}\n".format(
            str(total - total_left),
            str(cost),
            -1,
            -1,
            -1)
        f.write(output_str)

        while (total_left > hbuf_left):

#            f.write(str(total - total_left) +  ", "+ str(cost) + "\n")
        #        print cost, total - total_left
            slist_new = [1.0* hbuf_left *  r for r in rlist_norm]
            slist = map(sum, zip(slist, slist_new))
            total_left -= hbuf_left

            cand_idx = sel_func(rlist_norm, slist, clist)
            if (cand_idx == -1): # clean all space
                hbuf_left = hbuf
                slist = [0 for r in rlist] # reset slist
                cost += sum(clist)
                continue

            hbuf_left = slist[cand_idx]
            cost+=clist[cand_idx] # costlist
#            f.write(str(total - total_left) +  ", "+ str(cost) + ", " + str(cand_idx) + ", " +  str(clist[cand_idx]) + ", " + str(slist[cand_idx]) +  "\n")
            output_str = "{},{},{},{},{}\n".format(
                str(total - total_left),
                str(cost),
                str(cand_idx),
                str(clist[cand_idx]),
                str(slist[cand_idx]))
            f.write(output_str)

            slist[cand_idx] = 0
    return cost

class SelPolicy:
    last = -1
    quiet = True
    def sel_greedy_space(self, rlist, slist, clist):
        val, idx = max((val, idx) for (idx, val) in enumerate(slist))
        self.prn_sel("sel_space", idx, rlist[idx], slist[idx], clist[idx])
        self.last = idx
        return idx

    def sel_greedy_amp(self, rlist, slist, clist):
        val, idx = max((val/clist[idx], idx) for (idx, val) in enumerate(slist))
        self.prn_sel("sel_ampli", idx, rlist[idx], slist[idx], clist[idx])
        self.last = idx
        return idx

    def sel_rand(self, rlist, slist, clist):
        idx =  random.randrange(len(slist))
        self.prn_sel("sel_randm", idx, rlist[idx], slist[idx], clist[idx])
        self.last = idx
        return idx

    def sel_all(self, rlist, slist, clist):
        self.prn_sel("sel_alll", -1, -1, -1, -1)
        self.last = -1
        return -1 # -1 means this time to clean all the zones

    def sel_rr(self, rlist, slist, clist): # round robin
        if (self.last < 0 or self.last == len(rlist) - 1):
            self.last = 0
        else:
            self.last += 1
        self.prn_sel("sel_rrbn", self.last, rlist[self.last], slist[self.last], clist[self.last])
        return self.last

    def prn_sel(self, str, idx, r, s, c):
        if (self.quiet):
            return
        print '{s} {0:2} {1:3} {2:5.3f} {3:3} {4:6.3f}'.format( idx, r, s, c, s/c, s = str)



if __name__ == "__main__":
#    rlist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    rlist = [10.0, 90.0] # injection rate list
    clist = [0.1, 0.9] # cost list
    hbuf = 100
    total = 10000
    sp = SelPolicy()
    print "rlist =",rlist, "clist =", clist, "hbuf =", hbuf, "total =",total
    print "greedy space", sim(rlist, clist, hbuf, total, sp.sel_greedy_space, "space_2")
    print "greedy ampli", sim(rlist, clist, hbuf, total, sp.sel_greedy_amp, "ampli_2")
#    print "      random", sim(rlist, clist,  hbuf, total, sp.sel_rand, "randm")
#    print "         all", sim(rlist, clist,  hbuf, total, sp.sel_all, "all")
#    print "          rr", sim(rlist, clist,  hbuf, total, sp.sel_rr, "rr")
