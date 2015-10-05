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

figure(1)
%colours =['g','r','b'];

markers = ['o','*','+','.','x','s','d'];

m=1;
for j=1:P
    
    h(m)=plot(count(j,:,1),sprintf('-%sg',markers(j)));
    hold on
    h(m+1)=plot(count(j,:,2),sprintf('-%sr',markers(j)));
    h(m+2)=plot(count(j,:,3),sprintf('-%sb',markers(j)));
    
    xlabel('days');
    ylabel('count');
    
    for i=1:N
        text (i,count(j,i,1),num2str(count(j,i,1)),'FontSize',6);
        text (i,count(j,i,2),num2str(count(j,i,2)),'FontSize',6);
        text (i,count(j,i,3),num2str(count(j,i,3)),'FontSize',6);
    end
    set(gca,'XTick',[1:1:N])
    for i=1:N
        temp(i,:) = sprintf('day%d',i);
    end
    %set(gca,'XTickLabel',['day1';'day2';'day3';'day4';'day5'])
    set(gca,'XTickLabel',temp)
    
    m=m+3;
    
end
ylim([0 max(max(max(count)))+100])
legend(h,'positive1', 'negative1', 'neutral1','positive2', 'negative2', 'neutral2');


fprintf('\t  positive\tnegative\tneutral\n');
for j=1:P
    fprintf('-----------------president%d------------------------\n',j);
    for i =1:N
        fprintf('Day%d\t\t%d\t\t%d\t\t%d\n',i,count(j,i,1),count(j,i,2),count(j,i,3));
    end
end

