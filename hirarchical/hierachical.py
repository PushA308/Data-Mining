import csv
import math
import sys
import random

def read_csv(file_nm,mode,limiter):
    with open(file_nm,mode) as data:
        tmp=csv.reader(data,delimiter=limiter)
        data=list(tmp);
    return data;

def dis(p1,p2):
    ans=0.0;
    for i in range(len(p1)):
        ans=ans+((p1[i]-p2[i])**2)
    return (ans)
def distance(l1,l2):
    ans=sys.maxint;
    for i in l1:
        for j in l2:
            if(dis(i,j)<ans):
                ans=dis(i,j)
    return math.sqrt(ans);
def str_float(data):
    tmp=[];
    for i in data:
        tmp1=[];
        for j in i:
            try:
                float(j)
                tmp1.append(float(j))
            except ValueError:
                tmp1.append(0.0)
        tmp.append(tmp1)
    return tmp;

def create_matrix(data):
    matrix=[];
    for i in range(len(data)):
        tmp=[];
        for j in range(len(data)):
            tmp.append(distance(data[i],data[j]))
            #print data[i],data[j],distance(data[i],data[j])
        matrix.append(tmp)
    return matrix;

def find_min(matrix):
    minimum=sys.maxint;
    index=[];
    for i in range(len(matrix)):
        for j in range(i):
            if(matrix[i][j]<minimum and i!=j):
                minimum=matrix[i][j];
                index=[i,j]
    return minimum,index;

def merge(x_axis,l):
    tmp=[];
    tmp1=[];
    for i in l:
        for j in range(len(x_axis)):
            for k in range(len(x_axis[j])):
                if(i==j):
                    tmp1.append(x_axis[j][k]);
    tmp.append(tmp1)
    for i in range(len(x_axis)):
        if(i not in l):
            tmp.append(x_axis[i]);
    return tmp;         
   
def main():
    f_nm="/home/it/Desktop/Mk_data_mining/h_data.csv"
    mode='rb'
    delimiter=","
    raw_data=read_csv(f_nm,mode,delimiter);
    print raw_data;
    data=[];
    for i in range(1,len(raw_data)):
        tmp=[];
        for j in range(1,len(raw_data[0])):
            tmp.append(raw_data[i][j]);
        data.append(tmp);
    print data;
    data=str_float(data);    
    print data;
    x_axis=[];
    for i in data:
            x_axis.append([i]);
    print x_axis;
    for xyz in range(len(data)-1):
        matrix=create_matrix(x_axis);
        for i in matrix:
            print i;
        minimum=find_min(matrix)
        print minimum;
        x_axis=merge(x_axis,minimum[1]);
        print x_axis;
main();
