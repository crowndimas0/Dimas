#import library

import matplotlib.pyplot as plt
import numpy as np

#open data AWS

file = open("aws.txt", "r") #u can get data AWS
data = file.readlines()
for i in range (len(data)):
  print(data[i])
file.close()

#change data 6 and 7
#using this if u want to change data

data[6]= "17-08-2019\t20.00\t29.3\t88\t998.8\n "
data[7]= "18-08-2019\t20.00\t24.0\t99\t999.7\n "

for i in range (len(data)):
  data[i]= data[i].split()

tanggal=[]
waktu=[]
suhu=[]
kelembapan=[]
tekanan=[]

for i in range(1,len(data)):
  
  waktu.append(data[i][0])
  suhu.append(data[i][1])
  kelembapan.append(data[i][2])
  tekanan.append(data[i][3])
 print (data)

#graph

plt.plot(waktu,suhu,"r--o", label='suhu')
plt.title('grafik suhu')
plt.xlabel('suhu')
plt.ylabel('waktu')
plt.show()
