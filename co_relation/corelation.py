import math;
import random;
import sys;
import csv;
def read_csv(file_nm,limit):
    with open(file_nm,'rb') as data:
        tmp=csv.reader(data,delimiter=limit)
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
def z_mean(data,mean):
    z=[];
    for i in range(len(data)):
            z.append(data[i]-mean);
    return (z);

def z_mean_sqr(data,mean):
    z=[];
    for i in range(len(data)):
            z.append((data[i]-mean)**2)
    return z;
def x_xbar_y_ybar(x_x,y_y):
    z=[];
    for i in range(len(x_x)):
        z.append((x_x[i]*y_y[i]))
    return z;
raw_data=read_csv(r"C:\Users\Mahesh\Desktop\co.csv",',');
print raw_data
data=[];
for i in range(1,len(raw_data)):
    tmp=[];
    for j in range(len(raw_data[0])):
            tmp.append(raw_data[i][j])
    data.append(tmp)
data=str_float(data)
print data
x=[];
for i in range(len(data)):
    x.append(data[i][0]);
y=[];
for i in range(len(data)):
    y.append(data[i][1]);
print x,y
x_mean=sum(x)/len(x)
y_mean=sum(y)/len(y)
print x_mean,y_mean
x_xbar=z_mean(x,x_mean)
y_ybar=z_mean(y,y_mean)
print x_xbar,y_ybar
x_xbar_sqr=z_mean_sqr(x,x_mean)
print x_xbar_sqr
y_ybar_sqr=z_mean_sqr(y,y_mean)
print y_ybar_sqr
x_x_y_y=x_xbar_y_ybar(x_xbar,y_ybar)
c=sum(x_x_y_y)/math.sqrt((sum(x_xbar_sqr)*sum(y_ybar_sqr)))
print c

