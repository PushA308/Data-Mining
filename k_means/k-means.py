import math
import random
import csv
import sys

def read_csv(file_nm,mode,limit):
    with open(file_nm,mode) as data:
        tmp=csv.reader(data,delimiter=limit);
        data=list(tmp);
    return data;

def str_float(data):
    ans=[];
    for i in data:
        tmp=[];
        for j in i:
            try:
                float(j)
                tmp.append(float(j));
            except ValueError:
                tmp.append(0.0);
        ans.append(tmp);   
    return ans;


def distance(p1,p2):
    ans=0.0;
    for i in range(len(p1)):
        ans=ans+((p1[i]-p2[i])**2);
    return math.sqrt(ans);


def centroid(l):
    cen=[];
    for j in range(len(l[0])):
        tmp=0.0;
        for i in range(len(l)):
            tmp=tmp+l[i][j];
        cen.append(tmp/len(l));
    return cen;

def update_centroid(dic):
    cen=[];
    for i in dic:   
        cen.append(centroid(i));
    return cen;
def main():
    #f_nm="/home/it/Desktop/Make-up Data Mining /Dataset/clustering/Data_Cortex_Nuclear.csv";
    f_nm="/home/it/Desktop/a.csv"
    mode='rb';
    delimiter=',';
    raw_data= read_csv(f_nm,mode,delimiter);
    print raw_data;
    pt_nm=[];
    data=[];
    no_points=len(raw_data)
    no_atr=len(raw_data[0]);
    for i in range(1,no_points):
        pt_nm.append(raw_data[i][0])
    #print pt_nm;
    for i in range(1,no_points):
        tmp=[];
        for j in range(1,no_atr):
            #print i,j
            tmp.append(raw_data[i][j]);
        #print tmp;
        data.append(tmp);
    data=str_float(data);
    print data;
    no_centroid=int(input("Enter no of cluster:- "))
    centroid=[];
    level=input("Enter no of leavel:--> ");
    cen=random.sample(range(no_points-1),no_centroid)
    print cen;
    for i in cen:
        centroid.append(data[i]);
    print centroid;      
    for i in range(level):
        dic=[];
        for k in range(len(centroid)):
            dic.append([]);
        for k in range(len(data)):
            minimum=sys.maxint;
            index=0;
            for l in range(len(centroid)):
                #print k,l;
                #print minimum,distance(data[k],centroid[l]);
                if(distance(data[k],centroid[l])<minimum):
                    minimum=distance(data[k],centroid[l]);
                    index=l;
            dic[index].append(data[k]);
        print dic;
        centroid=update_centroid(dic);    
        print centroid;
main();

