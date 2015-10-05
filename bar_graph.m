clc;
clear all;
close all;
P= 2;%number of presidents
N=7;%number of days
count=zeros(P,N,3);
for k=1:P
    for j=1:N
        [num, txt, raw] =xlsread(sprintf('day%d%d.xlsx',k,j));
        for i= 1:length(txt(:,2)) -1
            if(strcmp(txt(i+1,2),'positive'))
                count(k,j,1)=count(k,j,1)+1;
            elseif(strcmp(txt(i+1,2),'negative'))
                count(k,j,2)=count(k,j,2)+1;
            elseif(strcmp(txt(i+1,2),'neutral'))
                count(k,j,3)=count(k,j,3)+1;
            end
        end
        
    end
end


count1=0;
for k=1:N
    
    for j=1:P
        count1=count1+1;
        for n=1:3
            
            count_temp(count1,n)=count(j,k,n);
        end
    end
    
end
b = bar(count_temp,'stacked');
mycolor=[0 1 0;1 0 0;0 0 1];% u can change this to change colours
colormap(mycolor)

for i=1:P*N
    if(count_temp(i,1)~=0)
        text(i,round(count_temp(i,1)/2),num2str(count_temp(i,1)),'FontSize',12);%u can change font size
    end
    if(count_temp(i,2)~=0)
        text(i,floor(count_temp(i,1)+count_temp(i,2)/2),num2str(count_temp(i,2)),'FontSize',12);
    end
    if(count_temp(i,3)~=0)
        text(i,floor(count_temp(i,1)+count_temp(i,2)+count_temp(i,3)/2),num2str(count_temp(i,3)),'FontSize',12);
    end
    text(i,count_temp(i,1)+count_temp(i,2)+count_temp(i,3)+5,num2str(sum(count_temp(i,:))),'FontSize',12);
end

set(gca,'XTickLabel',{'day1-pres1','day1-pres2','day2-pres1','day2-pres2','day3-pres1','day3-pres2','day4-pres1','day4-pres2','day5-pres1','day5-pres2','day6-pres1','day6-pres2','day7-pres1','day7-pres2',})

legend('positive', 'negative', 'neutral');%,'Location','NorthEastOutside')
%ylim([0 max(max(count))+20])
zoom on
hold on


fprintf('\t  positive\tnegative\tneutral\n');
for j=1:P
    fprintf('-----------------president%d------------------------\n',j);
    for i =1:N
        fprintf('Day%d\t\t%d\t\t%d\t\t%d\n',i,count(j,i,1),count(j,i,2),count(j,i,3));
    end
end
