clear

load ampli_1.csv
load space_1.csv
compare_plot(ampli_1, 'ampli', space_1, 'space', 'rlist [10, 90], clist [0.1, 0.9]');


load ampli_2.csv
load space_2.csv
compare_plot(ampli_2, 'ampli', space_2, 'space', 'rlist [10, 90], clist [0.9, 0.1]');

load ampli_3.csv
load space_3.csv
compare_plot(ampli_3, 'ampli', space_3, 'space', 'rlist [10, 90], clist [0.9, 0.1]');



load ampli_1_5.csv
load space_1_5.csv
compare_plot(ampli_1_5, 'ampli', space_1_5, 'space', 'rlist [10, 90], clist [0.1, 0.5]');


load ampli_2_5.csv
load space_2_5.csv
compare_plot(ampli_2_5, 'ampli', space_2_5, 'space', 'rlist [10, 90], clist [0.5, 0.1]');


load ampli_1_20.csv
load space_1_20.csv
compare_plot(ampli_1_20, 'ampli', space_1_20, 'space', 'rlist [10, 90], clist [0.1, 2]');


load ampli_2_20.csv
load space_2_20.csv
compare_plot(ampli_2_20, 'ampli', space_2_20, 'space', 'rlist [10, 90], clist [2, 0.1]');


% figure(1)
% plot(ampli_1(:,1), ampli_1(:,2), '-o', space_1(:,1), space_1(:,2), '-x');
% grid on
% legend('ampli', 'space')
% title('rlist [10, 90], clist [0.1, 0.9]')
% load ampli_2.csv
% load space_2.csv
% figure(2)
% plot(ampli_2(:,1), ampli_2(:,2), '-o', space_2(:,1), space_2(:,2), '-x');
% grid on
% legend('ampli', 'space')
% title('rlist [10, 90], clist [0.9, 0.1]')
