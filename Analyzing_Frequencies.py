from sklearn.metrics import precision_recall_fscore_support, accuracy_score
import csv
import numpy as np
import pandas as pd
import wget


data = pd.read_csv("D:\check\ValenzuelaAnnotations.csv")

r =  list(data.loc[: , "Follow-up"])

p =  list(data.loc[: , "freq"])

max = 0
lim = 0
loop = 0
b = []
while loop <16:

 a = []
 zz = []

 for k in p:

    if (k>=loop):
        a.append(1)
    else:
        a.append(0)

 for lo in r:

     if(lo== 0 or lo == 1):
         zz.append(0)
     else:
         zz.append(1)


 print("on " , loop)
 print(a)
 print(zz)


 accuracy = accuracy_score(zz, a)
 precision, recall, f1_score, _ = precision_recall_fscore_support(zz, a, average='binary')

 print("Accuracy: ", accuracy)
 print("Precision: ", precision)
 print("Recall: ", recall)
 print("F1 score: ", f1_score)


 # we can store these values of threshold, accuracy, precision, recall and f-measure to make graphs as we did in graph.py file

 if (max< f1_score):
     max=f1_score
     lim = loop
     b = a
 else:
     max = max

 loop = loop + 1



print("maximum f is : " , max)
print("maximum f is on: " , lim)
print(b)