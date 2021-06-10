import pandas as pd
import matplotlib.pyplot as plt
import colorsys as cs
import numpy as np


coordArrx = []
coordArry = []

# for i in range(2,14,2):
#     fileName = str(i/10) + 'rad.csv'
#     df = pd.read_csv(fileName)

df = pd.read_csv('1.2rad.csv')

for arr in df.iterrows():
    data = arr[1]
    for i in range(1,13,2):
        appendArr = []
        # Angle(rad)      Velocity(rad/s)
        # coordDict[arr[i]] = arr[i+1]
        coordArrx.append(data[i])
        coordArry.append(data[i+1])
   
fig = plt.figure()
plt.xlabel('Angle')        
plt.ylabel('Angular Velocity')        

plt.scatter(coordArrx, coordArry,15, alpha=0.01) 
plt.grid()
plt.show()
fig.savefig('1.2rad.png',dpi=300)
