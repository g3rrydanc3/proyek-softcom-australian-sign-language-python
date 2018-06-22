import math
import random

def binary(x):
    temp = []
    for i in range(7):
        temp.append(0 if x % 2 == 0 else 1)
        x = x // 2
    return list(reversed(temp))

def sigmoid(x):
    return 1/(1+math.exp(-x))

def f(x):
    return sigmoid(x) * (1 - sigmoid(x))

file_object  = open("random.txt")

X = []

m_dataCollection = file_object.readlines()
for i in range(len(m_dataCollection)):
	m_baru = m_dataCollection[i].replace("\n", "")
	X.append(m_baru.split(','))

y = []

for i in range(len(X)):
    X[i] = list(map(float, X[i]))
    y.append(binary(X[i][10]))
    del X[i][10]
    
print(X[0]);
print(len(X));

iterasi = 5
jum_layer = 9
jum_fitur = 10
jum_target = 7
alpha = 0.001

w = []
deltaW = []

file_simpan = open("simpan.txt")
data_simpan = file_simpan.readlines()

for k in range(jum_fitur):
    tmp = []
    tmp2 = []
    baris = data_simpan[k].split(",")
    for l in range(jum_layer):
        tmp.append(float(baris[l]))
        tmp2.append(0)
    w.append(tmp)
    deltaW.append(tmp2)

v = []
deltaV = []

for k in range(jum_layer):
    tmp = []
    tmp2 = []
    baris = data_simpan[k].split(",")
    for l in range(jum_target):
        tmp.append(float(baris[l]))
        tmp2.append(0)
    v.append(tmp)
    deltaV.append(tmp2)
	
for i in range(1):
    for j in range(len(X) - 100, len(X)):
        mid = []       
        for k in range(jum_layer):
            hitung = 0
            for l in range(jum_fitur):
                hitung += X[j][l] * w[l][k]
            mid.append(sigmoid(hitung))
        print("1")
        final = []
        for k in range(jum_target):
            hitung = 0
            for l in range(jum_layer):
                hitung += mid[l] * v[l][k]
            final.append(sigmoid(hitung))
        print("hasil : ", final)
        for i in range(len(final)):
            if final[i] < 0.5:
                final[i] = 0
            else:
                final[i] = 1
        
        print("target : ", y[j])
        
