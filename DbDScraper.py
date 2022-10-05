from cgitb import html
import code
import string
import pandas
import requests
from bs4 import BeautifulSoup
from  urllib.request import urlopen
import re
from pprint import pprint


url4="https://progameguides.com/dead-by-daylight/dead-by-daylight-codes/"
changeFlag = False


data = requests.get(url4).text
soup = BeautifulSoup(data,'html.parser')
element = soup.h3
list=[]
r=open('currentBloodPoints.txt','r')
redFile= r.read()
r.close()
codechecklist = redFile.split("\n")
nextSiblings = element.find_next_sibling('ul')
testint=0
for nextSibling in nextSiblings:
    stringlist = str(nextSibling)
    stringlist = re.sub("<.*?>","",stringlist)
    if stringlist != codechecklist[testint]:
        changeFlag=True
        
    testint+=1
    stringlist+= "\n"
    
    

    list.append(stringlist)

if changeFlag != True:
    print("NO NEW")
    yn = input("See List anyways?")
    if yn.capitalize() == "Y":
        for bp in list:
            print(bp)

else:
    f=open("currentBloodpoints.txt","w")

    for bp in list:
        f.write(bp)
        print(bp)
    f.close()







