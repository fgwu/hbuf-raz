function [effi_m, space_m, cost_m, p_m, q_m, qp_ratio] = effi_hybrid( hbuf, r1, r2, c1, c2 ) 
%   effi: efficient estimate: the slope, the space reclaimed percost
%   space: in one cycle, the slope
%   cost: in one cycle, the cost
%   Detailed explanation goes here
%   r1 > r2; p <= q; c1< c2
p = 0.1:0.0001:0.5;
q = 0.9:-0.0001:0.5;

r1_norm = r1/(r1+r2);
r2_norm = r2/(r1+r2);


space = q * hbuf /r2_norm; 

k = (log(p) - log(1-q*r2_norm))/log(r1_norm);
cost = c2 + c1 * k;
effi = space./cost;
[effi_m, idx] = max(effi);
space_m = space(idx);
cost_m = cost(idx);
p_m = p(idx);
q_m = q(idx);
qp_ratio = q_m/p_m;
end

