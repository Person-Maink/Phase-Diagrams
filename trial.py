import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0,10,100)
y = np.linspace(20,55, 100)

result = zip(x,y)

result = list(result)
print(result)

plt.plot(x, y)

plt.show()
