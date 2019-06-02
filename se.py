#This program gives the error bar plot of lateral pressure profile data for 251-500, 501-750 and 751-1000 calculating the standard error 
#The syntax is "python sd.py file1.xvg file2.xvg file3.xvg"

import sys
import re
import math

li1=[] #The li1, li2 and li3 are created to take up the lateral pressure profile values from 251-500, 501-750 and
li2=[] #751-1000 ns respectively
li3=[]
li4=[] #The list for the first column (X-axis) i.e. distance from bilayer center

fo1=open(sys.argv[1])
fo2=open(sys.argv[2])
fo3=open(sys.argv[3])

for line1 in fo1:
    search=re.search('^(.*?)\s+(.*?)$', line1)
    li1.append(search.group(2))
    li4.append(search.group(1))

for line2 in fo2:
    search=re.search('^(.*?)\s+(.*?)$', line2)
    li2.append(search.group(2))

for line3 in fo3:
    search=re.search('^(.*?)\s+(.*?)$', line3)
    li3.append(search.group(2))

#print li1[1]+li2[1]+li3[1]
for index in range(len(li1)):
    mean=(sum([float(li1[index]),float(li2[index]),float(li3[index])]))/3
    variance = (sum([(mean-float(li1[index]))**2, (mean-float(li2[index]))**2, (mean-float(li3[index]))**2]))/3
    sd = float(variance**(1/float(2)))
    se = sd/math.sqrt(3)
    print(li4[index], mean, se)

