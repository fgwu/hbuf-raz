function [  ] = compare_plot( data1, legend1, data2, legend2, parameter_str )
%COMP_PLOT Summary of this function goes here
%   Detailed explanation goes here
    figure
    plot(data1(:,3), data1(:,2), '-o', data2(:,3), data2(:,2), '-x');
    grid on
    legend(legend1, legend2)
    title(parameter_str)

end

