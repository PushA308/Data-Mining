#from data_mining_function import *;
import sys;
import copy;
import csv;
import math;
import random;

def find_freq_items_list(items,data):
	frq=[];
	for i in range(len(items)):
		count=0.0;
		for j in range(len(data)):
			for k in range(len(items[i])):
				flg=1;
				if(items[i][k] not in data[j]):
					flg=0;
					break;
			if(flg==1):
				count=count+1;
		frq.append(count);
	return frq;	 
def combination(previous,items,level):
	set_items=previous;
	combination_set=[];
	for j in range(len(items)):
		for k in range(len(set_items)):
			tmp=copy.deepcopy(set_items[k]);
			#print tmp;
			if(items[j][0] not in set_items[k]):
				tmp.append(items[j][0])
				tmp.sort();
				if tmp not in combination_set:
					combination_set.append(tmp);
	return combination_set;
			
def read_csv(file_name,limiter):
    with open(file_name,'rb') as raw_data:
        tmp=csv.reader(raw_data,delimiter=limiter)
        data=list(tmp)
    return data;
def main():
    #file_nm=r"C:\Users\Mahesh\Desktop\Dataset\association rule\groceries.csv";
    file_nm=r"/home/it/Desktop/Mk_data_mining/feq_data.csv";
    data=read_csv(file_nm,",")
    #print data;
    for i in data:
        i.sort();
    #print data;
    level=int(input("Enter levels:--> "))
    support=float(input("Enter Support:--> "))
    items=set();
    for i in data:
        for j in i:
            items.add(j);
    #print items;
    tmp=[];
    for i in items:
        tmp.append([i]);
    items=tmp;
    new_items=items;
    #print items;
    for i in range(level):
                print i;
                l=[];
                frq=find_freq_items_list(new_items,data);
                for j in range(len(new_items)):
                    if(frq[j]>=support):
                        l.append([new_items[j],frq[j]])
                tmp=[];
                for j in range(len(l)):
                    print l[j][0],l[j][1];
                    tmp.append(l[j][0]);
                if i==0:
                    items=tmp;
                c=combination(tmp,items,1);
                new_items=c;
main();
