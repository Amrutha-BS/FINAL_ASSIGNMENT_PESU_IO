import bs4 as bs
import lxml
import urllib.request
import requests
import csv
import random
#initializing the lists
l=[]
m=[]
z=[]
si=[]
x=[]
train_data=[]
test_data=[]
#INITIALIZING ALL THE FUNCTIONS
#function to shuffle  the data set    
def shuffle(si):
    random.shuffle(si)
#function to create train_set
def train_set(si):
   le=len(si)
   perc=int(0.8*le)
   for i in range(perc):
       train_data.append(si[i])
#function to create test_set   
def test_set(si):
    le=len(si)
    perc=int(0.2*le)
    for i in range(perc):
            test_data.append(si[le-1-i])
#
#WEB-SCRAPING CODE 
#
#OPENING assignment.html
sauce=urllib.request.urlopen('https://karki23.github.io/Weather-Data/assignment.html').read() 
srccode=bs.BeautifulSoup(sauce,'lxml')
#RETREIVING WEATHER DATA OF EACH CITY
for i in srccode.find_all('a'):
    l.append(i.text)
for i in l:
    pauce=requests.get('https://karki23.github.io/Weather-Data/'+i+'.html').text
    code=bs.BeautifulSoup(pauce,'lxml')
    tri=code.find_all('td')
    for j in tri:
        z.append(j.text)
    count=0
    si=[]
    for k in z:
       count=count+1
       if count==25:
           si.append(m)
           m=[]
           count=1
           m.append(k)
       else:
           m.append(k)
    with open('city'+i+'.csv', 'a') as csvFile:    #Storing the data in csv file
        writer=csv.writer(csvFile)
          for j in si:
             writer.writerow(j)
    shuffle(si)           #calling shuffle function to shuffle the dataset
    train_set(si)         #creating training set
    test_set(si)          #creating test set
