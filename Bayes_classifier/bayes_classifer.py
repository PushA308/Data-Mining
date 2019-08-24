import csv;
import math;
import random;
import copy
def read_csv(f_nm,mode,limiter):
    with open(f_nm,mode) as data:
        reader=csv.reader(data,delimiter=limiter);
        data=list(reader);
    return data
def display(data):
    for i in data:
        print i;
def yes_no_count(data):
    y_count=0.0;
    n_count=0.0
    for i  in range(1,len(data)):
        if(data[i][-1]=='yes'):
            y_count+=1;
        else:
            n_count+=1;
    return y_count,n_count;

def get_yes_no(l,data):
    tmp=copy.deepcopy(l);        
    for i in range(len(l)):
        y=[];
        n=[];
        for j in range(len(l[i][1])):
            y_c=0.0;
            n_c=0.0;
            for k in range(1,len(data)):
                if(data[k][i]==l[i][1][j] and data[k][-1]=='yes'):
                    y_c+=1;
                if(data[k][i]==l[i][1][j] and data[k][-1]=='no'):
                    n_c+=1;
            y.append(y_c);
            n.append(n_c);
        tmp[i].append(y)
        tmp[i].append(n)
    return tmp;           

def get_output(condition,a):
    _y=1.0
    _n=1.0
    for i in range(len(condition)):
        for j in range(len(a[i][0])):
            if(condition[i]==a[i][0][j]):
                _y=_y*(a[i][1][j]/a[-1][1][0])
                _n=_n*(a[i][1][j]/a[-1][2][1])
    print _y,_n
    
def get_output(condition,a):
    _y=1.0
    _n=1.0
    for i in range(len(condition)):
        for j in range(len(a[i][0])):
            #print condition[i],a[i][1][j]
            if(condition[i]==a[i][1][j]):
                print a[i][2][j],a[-1][2][0]
                _y=_y*(a[i][2][j]/a[-1][2][0])
                _n=_n*(a[i][3][j]/a[-1][3][1])
                break;
    print _y,_n;
    _y=_y*(a[-1][2][0]/(len(data)-1.0));
    _n=_n*(a[-1][3][1]/(len(data)-1.0));
    return _y,_n;
                          
f_nm=r'C:\Users\PushA\Desktop\Dataset\data.csv'
mode='rb'
delimiter=','
data=read_csv(f_nm,mode,delimiter)
display(data);
y_n_count=yes_no_count(data)
print y_n_count;
l=[]
for j in range(len(data[0])):
    tmp=set();
    for i in range(1,len(data)):
            tmp.add(data[i][j])
    l.append([data[0][j],list(tmp)])
print l;
a=get_yes_no(l,data)
display(a)
print "Enter Condition to be chacked:"
condition=[];
for i in range(len(data[0])-1):
    print "Eneter "+data[0][i]+" -->"
    tmp=raw_input("---->")
    condition.append(tmp)
print condition
output=get_output(condition,a)
if(output[0]>output[1]):
    print "YES"
else:
    print "NO"
