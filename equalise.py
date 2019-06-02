#Program to symmetrise the data

import re
import sys

#if len(sys.argv) != 2:
#    print "Syntax Example: python center.py file.xvg > newfile.xvg"
#    if __name__=='__main__':
#        main()
#    sys.exit()

def main():

    li1=[]
    li2=[]
    li3=[]
    dict1={}
    dict2={}
    dict3={}
    #print "Hello"
    f=open('mod_average.xvg')

    for line in f:
        search=re.search('^(.*?)\s+(.*?)$', line)

        if search:
            li1.append(search.group(1)) 
            li2.append(search.group(2))
        
    for index in range(len(li1)):
        dict1[li1[index]] = li2[index] #create a dictionary of x and y points

#    print dict1
#    print len(dict1)
#    print range(len(li1)) 

    midvalue = len(dict1)/2

    x=1
    for key, value in sorted(dict1.items()):
        if x <= midvalue:
            dict2[key] = value

        elif x > midvalue:
            dict3[key] = value
            
        x=x+1
        
    li3.append(dict2.values())

#    print li3
#    i=0
    for key, value in sorted(dict2.items(), reverse=True):
        print key, value

#    li3.append(dict3.keys())
#    print li3    

    y=0
    for key, value in sorted(dict2.items()):
        print float(key)*-1, value
        y=y+1

if __name__=='__main__':
    main()



