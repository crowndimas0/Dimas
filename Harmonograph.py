import numpy as np
import matplotplib.pyplot as plt

#using parameter
n = 100000
t = np.logspace(np.log10(20),np.log10(600),n)

#u can change this parameter
A = [ 1, 4, 1.4, 1.5, 2.6 ] #amplitudo
d = [ .004, .001, .005, .008, .0013 ] #dumping
f = [ 3, 2, 4, 2.4, 4 ] #frequency

#make x and y using this formula
x = A[0]*np.sin(t*f[0])*np.exp(-d[0]*t) + A[1]*np.sin(t*f[1])*np.exp(-d[1]*t) + A[2]*np.sin(t*f[2])*np.exp(-d[2]*t)
y = A[3]*np.sin(t*f[3])*np.exp(-d[3]*t) + A[4]*np.sin(t*f[4])*np.exp(-d[4]*t)
#if u want to add more parameter A, d, f, u must add to x and y. based on amount of array

#show the plot
plt.plot(x,y,'k',linewidth=.1)
plt.axis('off')
plt.show()

#Reference https://www.megabagus.id/download/harmonograph-python/#
