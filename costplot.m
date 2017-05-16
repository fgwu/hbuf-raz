load ampli.csv
load space.csv
figure
plot(ampli(:,1), ampli(:,2), '-o', space(:,1), space(:,2), '-x');
grid on
legend('ampli', 'space')
title('rlist [10, 90], clist [0.3, 0.1]')
load ampli_2.csv
load space_2.csv
figure
plot(ampli_2(:,1), ampli_2(:,2), '-o', space_2(:,1), space_2(:,2), '-x');
grid on
legend('ampli', 'space')
title('rlist [10, 90], clist [0.1, 0.3]')
