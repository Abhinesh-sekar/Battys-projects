import pandas as pd     
import numpy as np
import datetime
import os


###########################################33
p = input("PARTY NAME : ")
p = p.upper()
o = (input("ENTER ORDER NUMBER : "))
k = "D:\Dropbox\Batty's company\PRODUCTION\LABEL MAKING\LABEL IMAGES"
j = ".jpg"
path = os.path.dirname(__file__)
pr = pd.read_csv(path + "/price.csv")
x = pd.read_csv(path + "/INPUT.csv")
prg = pd.read_csv(path + "/gprice.csv")

del x["lining"]
del x["f/b"]
del x['stich']

y = pd.melt(x,id_vars=['article','colour'],var_name="size",value_name="copy")

y = y.dropna()

y = y.sort_values(by=["article",'colour'])

y['image']=k+chr(92)+y['article']+j

y['month']=datetime.datetime.now().month

y['year']=datetime.datetime.now().year

y["party"]=p

y['order number']=o

if (p == "GENDER"):
    y = y.merge(prg, on='article', how='left')
else:
    y = y.merge(pr, on='article', how='left')

y = y.replace(to_replace = ['BL SYN', 'BR SYN','BR MILD','BL MILD','TAN SYN','BR/BL SYN','BL/BR SYN'], value = ['BLACK', 'BROWN','BROWN','BLACK','TAN','BROWN','BLACK'])

y = y.replace(np.nan,'', regex=True)

y = y.drop_duplicates()

y = y[['copy','article','colour','image','month','order number','party','price','size','year']]

y.to_clipboard(index = False)

##output order##
#COPY	ART	COL	IMAGE	MONTH	ORd.NO	PARTY	PRICE	SIZE	YEAR

print(y)

y.to_csv(path + "/OUTPUT.csv")