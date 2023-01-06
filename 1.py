import numpy as np
import matplotlib.pyplot as plt
x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y=['173','153','195','147','120','144','148','109','174','130','172','131']
plt.xlabel("Month of year",fontsize='18')
plt.ylabel("sales data")
plt.scatter(x,y,color="pink")


x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y=['189','189','105','112','173','109','151','197','174','177','145','161']
plt.scatter(x,y,color='yellow')


x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
y=['185','185','126','134','196','153','112','133','200','145','167','110']
plt.scatter(x,y,color='blue')
plt.show()

