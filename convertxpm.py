import numpy as np
import matplotlib.pyplot as plt
import pathlib
import os
import re
from scipy.optimize import curve_fit
import string
from itertools import islice
import math

def main():
    filename='file.xpm'
    my_dict = {}
    counter=0
    index=0
    r=0
    with open(filename) as f:
        for line in f:
            if line[0]=='"':
                counter=counter+1
                if counter==1 :
                    line=line.replace('"',' ')
                    x=line.split()
                    row=int(x[0])
                    col=int(x[1])
                    vallen=int(x[2])
                    A=np.zeros((row,col))
                if counter > 1 : 
                    if index < vallen :
                        name=line[1]
                        rline=line.split()
                        val=rline[5].replace('"',' ')
                        index=index+1
                        #print(line)
                        #print(line)
                        my_dict[name]=float(val)
                        #print(my_dict)
                    else:
                        c=0
                        line=line.replace('"','')
                        line=line.replace(',','')
                        #print(line)
                        #print(len(line))
                        for i in line:
                            if c<col:
                                A[r,c]=my_dict.get(i)
                                #print(my_dict.get(i))
                                #print(A[r,c])
                                c=c+1
                        r=r+1
    #prepare image
    fig = plt.figure(figsize=(14, 10))
    im=plt.imshow(A,interpolation='none',cmap=plt.cm.jet_r)
    cbar = plt.colorbar(im)
    cbar.set_label('Distance [nm]',fontsize=20)
    cbar.ax.tick_params(labelsize=20)
    ticks=['1TYR','2GLY','3ARG','4LYS','5LYS','6ARG','7ARG','8GLN','9ARG','10ARG','11ARG','12CSP','13DOXO','14TYR','15GLY','16ARG','17LYS','18LYS','19ARG','20ARG','21GLN','22ARG','23ARG','24ARG','25CSP','26DOXO']
    plt.xticks(np.arange(26), ticks,rotation=90,fontsize=15) 
    plt.yticks(np.arange(26),ticks[::-1],fontsize=15)
    res1t=np.arange(13)
    for i in res1t:
        plt.gca().get_xticklabels()[i].set_color("dimgray")
        plt.gca().get_yticklabels()[i+13].set_color("dimgray")
    plt.show() 
main()
