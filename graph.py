import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv("D:\check\F.measure.csv") # file path

h =  list(data.loc[: , "Threshold "])

p =  list(data.loc[: , " Precision "])

r =  list(data.loc[: , " Recall "])

ac =  list(data.loc[: , " Accuracy "])

fm =  list(data.loc[: , "Fmeasure"])


plt.plot(r, label = 'Recall')

plt.plot(p, label = 'Precision')
plt.plot(fm, label = 'F.measure')
plt.plot(ac, label = 'Accuracy')


plt.xlabel('Threshold Values')
plt.ylabel('Values')
plt.title('Performance measures')

plt.legend()
plt.show()