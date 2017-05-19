#!/usr/bin/python

import random

def sim(rlist, clist, hbuf, total, sel_policy, sel_func_str, logfile_suffix):
    hbuf_left = hbuf
    total_left = total
    slist = [0 for r in rlist] # space list
    rsum = sum(rlist)
    rlist_norm = [1.0*r/rsum for r in rlist] # normalized injection rate list
    cost = 0
    reclaim_accu = 0
    with open(sel_func_str+logfile_suffix+".csv", "w+") as f:
        format_str = "{:10.2f},{:8.2f},{:8.2f},{:3},{:8.2f},{:8.2f}\n"
        output_str = format_str.format(
            total - total_left,
            cost,
            reclaim_accu,
            -1,
            -1,
            -1)
        f.write(output_str)

        while (total_left > hbuf_left):
            slist_new = [1.0* hbuf_left *  r for r in rlist_norm]
            slist = map(sum, zip(slist, slist_new))
            total_left -= hbuf_left

            sel_func = sel_policy.policy_dict[sel_func_str]
            cand_idx = sel_func(rlist_norm, slist, clist)

            if (cand_idx == -1): # clean all space
                hbuf_left = hbuf
                slist = [0 for r in rlist] # reset slist
                cost += sum(clist)
                continue

            hbuf_left = slist[cand_idx]
            cost += clist[cand_idx] # costlist
            reclaim_accu += slist[cand_idx]

            output_str = format_str.format(
                total - total_left,
                cost,
                reclaim_accu,
                cand_idx,
                clist[cand_idx],
                slist[cand_idx])
            f.write(output_str)

            slist[cand_idx] = 0
    print "{:>6}:{:10.1f}".format(sel_func_str, cost)
    return cost

class SelPolicy:
    last = -1
    quiet = True
    policy_dict = dict()
    def __init__(self, q):
        self.quiet = q
        self.policy_dict['space'] = self.sel_greedy_space
        self.policy_dict['ampli'] = self.sel_greedy_amp
        self.policy_dict['hybrid'] = self.sel_greedy_hybrid
        self.policy_dict['adapt'] = self.sel_greedy_adaptive
        self.policy_dict['rand'] = self.sel_rand
        self.policy_dict['all'] = self.sel_all
        self.policy_dict['rr'] = self.sel_rr

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

    def sel_greedy_hybrid(self, rlist, slist, clist):
        clist_alt = [2.3333,1]
        val, idx = max((val/clist_alt[idx], idx) for (idx, val) in enumerate(slist))
        self.prn_sel("sel_ampli", idx, rlist[idx], slist[idx], clist[idx])
        self.last = idx
        return idx

    def sel_greedy_adaptive(self, rlist, slist, clist):
        clist_alt = [2.3333,1]
        val, idx = max((val/clist_alt[idx], idx) for (idx, val) in enumerate(slist))
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
    rlist = [10.0, 20.0, 40.0, 80.0] # injection rate list
#    suffix = "_1_20"
#    clist = [0.1, 2] # cost list
    suffix = "_3"
    clist = [0.9, 0.5, 0.7, 0.9] # cost list
    hbuf = 100
    total = 100000
    sp = SelPolicy(True)
    print "rlist =",rlist, "clist =", clist, "hbuf =", hbuf, "total =",total

    sim(rlist, clist, hbuf, total, sp, "space", suffix)
    sim(rlist, clist, hbuf, total, sp, "ampli", suffix)
#    sim(rlist, clist, hbuf, total, sp, "hybrid", suffix)
    sim(rlist, clist, hbuf, total, sp, "rand", suffix)
    sim(rlist, clist, hbuf, total, sp, "all", suffix)
    sim(rlist, clist, hbuf, total, sp, "rr", suffix)
