function [effi, space, cost ] = effi_space( hbuf, r1, r2, c1, c2 ) 
%   effi: efficient estimate: the slope, the space reclaimed percost
%   space: in one cycle, the slope
%   cost: in one cycle, the cost
%   Detailed explanation goes here
%   r1 > r2; c1 < c2
c1_norm = 0.5;
c2_norm = 0.5;

r1_norm = r1/(r1+r2);
r2_norm = r2/(r1+r2);
space = c2_norm * hbuf /r2_norm; 

k = (log(c1_norm) - log(1-c2_norm*r2_norm))/log(r1_norm);
cost = c2 + c1 * k;
effi = space/cost;

end

