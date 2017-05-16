load ampli_1.csv
load space_1.csv
figure(1)
plot(ampli_1(:,1), ampli_1(:,2), '-o', space_1(:,1), space_1(:,2), '-x');
grid on
legend('ampli', 'space')
title('rlist [10, 90], clist [0.1, 0.9]')
load ampli_2.csv
load space_2.csv
figure(2)
plot(ampli_2(:,1), ampli_2(:,2), '-o', space_2(:,1), space_2(:,2), '-x');
grid on
legend('ampli', 'space')
title('rlist [10, 90], clist [0.9, 0.1]')
