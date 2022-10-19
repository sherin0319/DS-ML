import matplotlib.pyplot as plt
import numpy as np
x=np.array(['Mon','Tues','Wed','Thurs','Fri'])
y=np.array([300,450,150,400,650])
plt.subplot(1,2,1)
plt.plot(x,y,color='c',linestyle='dotted',marker='h',mfc='m',mec='k')
plt.xlabel('DAYS')
plt.ylabel("SALES OF DRINKS")
plt.title("SALES DATA-1",loc='right')
x=np.array(['Mon','Tues','Wed','Thurs','Fri'])
y=np.array([400,500,350,300,500])
plt.subplot(1,2,2)
plt.plot(x,y,color='y',linestyle='dashed',marker='d',mfc='g',mec='r')
plt.xlabel('DAYS')
plt.ylabel("SALES OF FOOD")
plt.title("SALES DATA-2",loc='center')
plt.show()