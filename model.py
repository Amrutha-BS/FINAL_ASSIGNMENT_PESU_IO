#TRAIN_SET AND TEST_SET ARE BEING IMPORTED FROM scraper.py
#CODE TO SHUFFLE DATA,CREATE TRAIN_SET AND TEST_SET ARE THERE IN scraper.py
import scraper
from scraper import train_data
from scraper import test_data
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import numpy as np
#INITIALIZING THE WEIGHTS#
w1=float(np.random.randn())
w2=float(np.random.randn())
w3=float(np.random.randn())
w4=float(np.random.randn())
w5=float(np.random.randn())
w6=float(np.random.randn())
w7=float(np.random.randn())
w8=float(np.random.randn())
w9=float(np.random.randn())
w10=float(np.random.randn())
w11=float(np.random.randn())
b=float(np.random.randn())
#SIGOID FUNCTION
def sigmoid(x):
    return 1/(1+np.exp(-x))
#DERIVATIVE OF SIGMOID FUNCTION
def sigmoid_p(x):
    return sigmoid(x)*(1-sigmoid(x))
print("entering training loop")
#TRAINING LOOP
learning_rate=0.0001
costs=[]
for i in range(1000):
  for j in range(len(train_data)):
      z=float(float(train_data[j][2])*w1+float(train_data[j][3])*w2+float(train_data[j][4])*w3+float(train_data[j][8])*w4+float(train_data[j][11])*w5+float(train_data[j][12])*w6+float(train_data[j][13])*w7+float(train_data[j][14])*w8+float(train_data[j][19])*w9+float(train_data[j][20])*w10+float(train_data[j][22])*w11+b)
      print(z)
      if train_data[j][23]=="yes":
          train_data[j][23]=int(1)
      else:
          train_data[j][23]=int(0)
      pred=sigmoid(z/0.001)
   
      target=train_data[j][23]
      cost=np.square(pred-target)
      '''print(cost)'''            #IF REQUIRED
      costs.append(cost)
      dcost_pred=2*(pred-target)
      dpred_dz=sigmoid_p(z)
    
      dz_dw1=float(train_data[j][2])
      dz_dw2=float(train_data[j][3])
      dz_dw3=float(train_data[j][4])
      dz_dw4=float(train_data[j][8])
      dz_dw5=float(train_data[j][11])
      dz_dw6=float(train_data[j][12])
      dz_dw7=float(train_data[j][13])
      dz_dw8=float(train_data[j][14])
      dz_dw9=float(train_data[j][19])
      dz_dw10=float(train_data[j][20])
      dz_dw11=float(train_data[j][22])
      dz_db=float(1)
    
      dcost_dz=float(dcost_pred*dpred_dz)
    
      dcost_dw1=dcost_dz*dz_dw1
      dcost_dw2=dcost_dz*dz_dw2
      dcost_dw3=dcost_dz*dz_dw3
      dcost_dw4=dcost_dz*dz_dw4
      dcost_dw5=dcost_dz*dz_dw5
      dcost_dw6=dcost_dz*dz_dw6
      dcost_dw7=dcost_dz*dz_dw7
      dcost_dw8=dcost_dz*dz_dw8
      dcost_dw9=dcost_dz*dz_dw9
      dcost_dw10=dcost_dz*dz_dw10
      dcost_dw11=dcost_dz*dz_dw11
      dcost_db=dcost_dz*dz_db
    
      w1=w1-learning_rate*dcost_dw1
      w2=w2-learning_rate*dcost_dw2
      w3=w3-learning_rate*dcost_dw3
      w4=w4-learning_rate*dcost_dw4
      w5=w5-learning_rate*dcost_dw5
      w6=w6-learning_rate*dcost_dw6
      w7=w7-learning_rate*dcost_dw7
      w8=w8-learning_rate*dcost_dw8
      w9=w9-learning_rate*dcost_dw9
      w10=w10-learning_rate*dcost_dw10
      w11=w11-learning_rate*dcost_dw11
      b=b-learning_rate*dcost_db

result=[]
prediction=[]
d={}
cr=0
wr=0
#TESTING LOOP
for j in range(len(test_data)):
      z=float(float(test_data[j][2])*w1+float(test_data[j][3])*w2+float(test_data[j][4])*w3+float(train_data[j][8])*w4+float(train_data[j][11])*w5+float(train_data[j][12])*w6+float(train_data[j][13])*w7+float(train_data[j][14])*w8+float(train_data[j][19])*w9+float(train_data[j][20])*w10+float(train_data[j][22])*w11+b)
      if test_data[j][23]=="yes":
          test_data[j][23]=int(1)
      else:
          test_data[j][23]=int(0)
      pr=sigmoid(z)
      if pr<0.5:
          result.append(0)
      else:
          result.append(1)
for i in range(test_data):
      if test_data[i][23]==result[i]:
          cr=cr+1
      else:
          wr=wr+1
#COMPUTING ACCURACY
accuracy=(cr*100)/(cr+wr) 
prediction.append(accuracy)
with open('results.py', 'w') as cv:    #Storing the data in csv file
        writer=csv.writer(cv)
        for i,j in d.items():
            writer.writerrow('[',i,':',j,']')
#COMPUTING AVERAGE ACCURACY
sum=0            
for i in d:
    sum=sum+d[i]
avg_accuracy=sum/49
with open('results.py', 'a') as cv:    #Storing the data in csv file
        writer=csv.writer(cv)
        writer.writerrow(avg_accuracy)


   
     
    
    