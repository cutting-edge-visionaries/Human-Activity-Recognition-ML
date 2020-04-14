import numpy as np
import pandas as pd


for i in range (0,62):#creating 61 files
    a='kc'+str(i)+'.txt'
    file=open(a,'w')
j=1
for i in range (1,62):#concating acc n gyro readings of 61 files
    c='kc'+str(i)+'.txt'
    if (i<19):
        if i<10:
            if i%2!=0:
                a='acc_exp0'+str(i)+'_user0'+str(j)+'.txt'
                b='gyro_exp0'+str(i)+'_user0'+str(j)+'.txt'
            else:
                a='acc_exp0'+str(i)+'_user0'+str(j)+'.txt'
                b='gyro_exp0'+str(i)+'_user0'+str(j)+'.txt'
                j=j+1;
        else:
            if i%2!=0:
                a='acc_exp'+str(i)+'_user0'+str(j)+'.txt'
                b='gyro_exp'+str(i)+'_user0'+str(j)+'.txt'
            else:
                a='acc_exp'+str(i)+'_user0'+str(j)+'.txt'
                b='gyro_exp'+str(i)+'_user0'+str(j)+'.txt'
                j=j+1;
    else:
        if i%2!=0:
            a='acc_exp'+str(i)+'_user'+str(j)+'.txt'
            b='gyro_exp'+str(i)+'_user'+str(j)+'.txt'
            if (i!=19):
                j=j+1
        else:
            a='acc_exp'+str(i)+'_user'+str(j)+'.txt'
            b='gyro_exp'+str(i)+'_user'+str(j)+'.txt'
            
    with open(a,'r') as f1,open(b,'r') as f2,open(c,'w') as f3:
        for x,y in zip(f1,f2):
            f3.write(x.strip()+' '+y.strip()+'\n')
a=pd.read_csv('kc1.txt',delimiter=' ',header=None)
a=np.array(a)

y=np.loadtxt('labels.txt',delimiter=' ',dtype='int64')
#x=pd.read_csv('acc_01.csv',header=None)
#x=np.array(x)
i=0
s=[]
p=[]
#while (y[i][0]==1):
 #   for j in range (y[i][3],y[i][4]):
  #      s.append(x[j-1])
   # i=i+1
#np.savetxt("foo.csv",s,delimiter=',')
#i=1194
while (y[i][0]<=61):
    if(y[i][0]==1):
        for j in range (y[i][3],y[i][4]):
            s.append(a[j-1])
            p.append(y[i][2])
    elif(y[i][0]!=y[i-1][0]):
        b='kc'+str(y[i][0])+'.txt'
        a=pd.read_csv(b,delimiter=' ',header=None)
        a=np.array(a)
        for j in range (y[i][3],y[i][4]):
            s.append(a[j-1])
            p.append(y[i][2])
    else:
        for j in range (y[i][3],y[i][4]):
            s.append(a[j-1])
            p.append(y[i][2])
    i=i+1
np.savetxt("x.csv",s,delimiter=',')
np.savetxt("y.csv",p,delimiter=',')+
