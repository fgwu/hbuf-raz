clear

load ampli_1.csv
load space_1.csv
load rr_1.csv
load all_1.csv
load rand_1.csv
figure(1)
plot(ampli_1(:,3),  ampli_1(:,2), '-x',  ...
space_1(:,3),  space_1(:,2), '-o', ...
    rr_1(:,3), rr_1(:,2), '-^',  ...
all_1(:,3),all_1(:,2), '-.', ...
rand_1(:,3),rand_1(:,2), '->');
    title('Injection Rate 20:80, Migr. Cost 0.5,0.9 (zones)');
legend('efficency', 'space', 'rr', 'all', 'random');
legend('Location', 'southeast')
xlabel('hbuffer space reclaimed: accumlated (# zones)');
ylabel('zone migration cost: accumlated (# zones)');
axis([0,10000, 0, 120]);
set(1, 'units', 'centimeters', 'pos', [0 0 12 9])
savefig('two_zone_1.fig');
saveas(gcf,'two_zone_1.png')
saveas(gcf,'two_zone_1','epsc')


load ampli_2.csv
load space_2.csv
load rr_2.csv
load all_2.csv
load rand_2.csv
figure(2)

plot(ampli_2(:,3),  ampli_2(:,2), '-x',  ...
space_2(:,3),  space_2(:,2), '-o', ...
    rr_2(:,3), rr_2(:,2), '-^',  ...
all_2(:,3),all_2(:,2), '-.', ...
rand_2(:,3),rand_2(:,2), '->');
    title('Injection Rate 20:80, Migr. Cost 0.9,0.5 (zones)');
legend('efficency', 'space', 'rr', 'all', 'random');
legend('Location', 'southeast')
xlabel('hbuffer space reclaimed: accumlated (# zones)');
ylabel('zone migration cost: accumlated (# zones)');
axis([0,10000, 0, 120]);
set(2, 'units', 'centimeters', 'pos', [0 0 12 9])
savefig('two_zone_2.fig');
saveas(gcf,'two_zone_2.png')
saveas(gcf,'two_zone_2','epsc')




% load ampli_1.csv
% load space_1.csv
% compare_plot(ampli_1, 'ampli', space_1, 'space', 'rlist [10, 90], clist [0.1, 0.9]');
% 
% 
% load ampli_2.csv
% load space_2.csv
% compare_plot(ampli_2, 'ampli', space_2, 'space', 'rlist [10, 90], clist [0.9, 0.1]');
% 
% load ampli_3.csv
% load space_3.csv
% compare_plot(ampli_3, 'ampli', space_3, 'space', 'rlist [10, 90], clist [0.9, 0.1]');
% 
% 
% 
% load ampli_1_5.csv
% load space_1_5.csv
% compare_plot(ampli_1_5, 'ampli', space_1_5, 'space', 'rlist [10, 90], clist [0.1, 0.5]');
% 
% 
% load ampli_2_5.csv
% load space_2_5.csv
% compare_plot(ampli_2_5, 'ampli', space_2_5, 'space', 'rlist [10, 90], clist [0.5, 0.1]');
% 
% 
% load ampli_1_20.csv
% load space_1_20.csv
% compare_plot(ampli_1_20, 'ampli', space_1_20, 'space', 'rlist [10, 90], clist [0.1, 2]');
% 
% 
% load ampli_2_20.csv
% load space_2_20.csv
% compare_plot(ampli_2_20, 'ampli', space_2_20, 'space', 'rlist [10, 90], clist [2, 0.1]');


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
