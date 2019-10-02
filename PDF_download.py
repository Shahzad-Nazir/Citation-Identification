import pandas as pd
import wget


data = pd.read_csv("D:\check\ValenzuelaAnnotations.csv") # path of file

me =  data.drop_duplicates(subset='Cited-by', keep="last")

z =  list(me.loc[: , "Cited-by"])

z2 =  list(me.loc[: , "Paper"])


# downloading citing papers
for x in z:

 print("downloading "+x+"")
 url = 'http://www.aclweb.org/anthology/'+x+''
 wget.download(url, 'D:/new work/citing/'+x+'.pdf')
 print("donload done of "+x+"")


# downloading cited papers
for x2 in z2:

 print("downloading "+x2+"")
 url = 'http://www.aclweb.org/anthology/'+x2+''
 wget.download(url, 'D:/new work/citedpapers/'+x2+'.pdf')
 print("donload done of "+x2+"")

