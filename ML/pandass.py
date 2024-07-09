import pandas as pd
import numpy as np
############################# PANDAS ################################
intseri = pd.Series([1,2,45,2,6,7])
seri = pd.Series(["kero","ahmet","mehmet"])
print(type(seri))
print(type(intseri))
print(seri.axes)
print(seri.dtype)
print(seri.size)
print(seri.shape)
print(seri.ndim)
print(seri.values)
print(seri.head(3))
print(seri.tail(1))
print(pd.Series([1,3,5,2,32,34,23,5], index = [1,3,4,8,9,7,2,6]))
sozluk = pd.Series({"reg":10,"log":11})
print(sozluk)
print(pd.concat([seri,sozluk]))
seri.keys
seri.index
print(list(sozluk.items()))
print("reg" in sozluk)
####DATA FRAME####
liste =[5,4,7,8,9]
df = pd.DataFrame(seri,columns=["KERONUN FRAME'İ"])
print(seri)
tdimensionarray = np.arange(1,10).reshape((3,3))
print(tdimensionarray)
arraydataframe = pd.DataFrame(tdimensionarray,columns=["var 1","var 2","var 3"])
print(arraydataframe)
df.drop(0,axis=0, inplace=True)
##loc kapalı parantez##iloc kapalı açık parantez##
print(df.loc[0:2])
print(df.iloc[0:2])