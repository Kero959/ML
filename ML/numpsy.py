import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([1.3,2,3,4,5],dtype="int")
c = np.zeros(10,dtype="int")
d = np.ones(10,dtype="int")
e = np.full((10,20),1,dtype="int")
f = np.arange(0,100,2)
g = np.linspace(1,3,200)
h = np.random.normal(10,4,(3,4))#ortalaması 10 standart sapması 4 olan 3 e 4 lük array.
i = np.random.randint(0,10,(2,2))
j = np.random.randint(10,size = 10,dtype="int64")
k = np.random.randint(10,size=(3,5))
print(j.ndim)
print(j.shape)
print(j.size)
print(j.dtype)
print(j)
print(k.ndim)
print(k.shape)
print(k.size)
print(k.dtype)
print(k)

#RESHAPING
a = np.arange(1,13)
print(a)
a = a.reshape((3,4))
print(a)
a = a.reshape((6,2))
print(a)

#CONCATENATION
x = np.array([1,2,3,4])
y = np.array([2,3,4,5])
print(np.concatenate([x,y]))

#SPLITTING
sp = np.array([1,2,3,4,66,1312,5,42124,2,2,2,2])
a,b,c,d = np.split(sp,[3,5,6])
print(a)
print(b)
print(c)
yeniarray=np.arange(16).reshape(8,2)
vsplt=np.vsplit(yeniarray,[2])
print(yeniarray)
print(vsplt)
hsplt = np.hsplit(yeniarray,[1])
print(hsplt)

#SORTING
srtarray = np.array([1,23,123,12,3])
print(srtarray)
print(np.sort(srtarray))
print(srtarray)
srtarray.sort()
print(srtarray)
tdimensionarray= np.random.randint(0,100,(10,10))
print(tdimensionarray)
print(np.sort(tdimensionarray,axis=1))
print(np.sort(tdimensionarray,axis=0))

#SATIR SÜTUN SEÇİMİ
arr=np.random.randint(0,100,(10,10))
print(arr)
print(arr[:,0])#SÜTUN
print(arr[:,1])
print(arr[0,:])#SATIR
print(arr[0:2,1:9])#0 ve 1. satırla 1den 9.sütuna kadar

#ALT KÜME İŞLEMLERİ
arrA=np.random.randint(0,10,size=(5,5))
alt_a=arrA[0:2,0:3]
print(alt_a)
alt_a[0,0]=1111
print(alt_a)
print(arrA)

arrB=np.random.randint(0,3,size=(5,5))
print(arrB)
alt_b=arrB[0:2,0:3].copy()
print(alt_b)
alt_b[0,0]=1111
print(alt_b)
print(arrB)
#Fancy index
arr = np.array([0,3,5,6,7,8,9,14,6,585,21,4,74,5467,456])
fncindex = [0,1,2]
fncindex2 = [3,6,9]
print(arr[fncindex])
print(arr[fncindex2])
#2.dereceden denklem
#5*x0+x1 = 12
#x0+3*x1 = 10
a = np.array([[5,1],[1,3]])
b = np.array([12,10])
print(a)
x = np.linalg.solve(a,b)
print(x)
