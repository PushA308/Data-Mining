#from data_mining_function import *;
import sys;
import copy;
import csv;
import math;
import random;
from itertools import permutations

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
       

def generate_rule(whole_freqent_set,data,min_confidence):
    for i in range(len(whole_freqent_set)):
        tmp=whole_freqent_set[i][0];
        #print whole_freqent_set[i][0];
        #print tmp;
        all_permutaion=list(permutations(whole_freqent_set[i][0]))
        #print all_permutaion;
        for j in all_permutaion:
            for k in range(len(j)-1): 
                x = j[0:k+1]
                y = j[k+1:]
                if(len(x)<1 and len(y)<1):
                    continue;
                #print "hi"
                #print x;
                #print y;
                #print j;
                freq_x = find_freq_items_list([x],data)
                #print freq_x; 
                c = whole_freqent_set[i][1]/freq_x[0]
                if c >= min_confidence and c!=1:
                    print(x,' -> ',y,'confidence is ',c)
def main():
    file_nm=r"/home/it/Desktop/Mk_data_mining/Dataset/association rule/groceries.csv";
    #file_nm=r"/home/it/Desktop/Mk_data_mining/feq_data.csv";
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
    l=[];
    for i in range(level):
                print i;
                frq=find_freq_items_list(new_items,data);
                for j in range(len(new_items)):
                    if(frq[j]>=support):
                        if( [new_items[j],frq[j]] not in l):
                            l.append([new_items[j],frq[j]])
                tmp=[];
                for j in range(len(l)):
                    #print l[j][0],l[j][1];
                    tmp.append(l[j][0]);
                if i==0:
                    items=tmp;
                c=combination(tmp,items,1);
                new_items=c;
    for i in l:
        print i;
    confidence=float(input("Enter confidance to form Rules"));
    generate_rule(l,data,confidence)
main();
