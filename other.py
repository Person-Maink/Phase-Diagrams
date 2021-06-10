import pandas as pd
import matplotlib.pyplot as plt
import pygame as pg
import colorsys as cs
import numpy as np


coordArr = []

for i in range(2,14,2):
    fileName = str(i/10) + 'rad.csv'
    df = pd.read_csv(fileName)
    # print(df)

    for arr in df.iterrows():
        data = arr[1]
        for i in range(1,13,2):
            appendArr = []
            # Angle(rad)      Velocity(rad/s)
            # coordDict[arr[i]] = arr[i+1]
            appendArr.append(data[i])
            appendArr.append(data[i+1])
            coordArr.append(appendArr)
        
print(len(coordArr))
        
# plt.xlabel('Angle')        
# plt.ylabel('Angular Velocity')        

# for coordinate in coordArr: 
#     plt.plot(coordinate[0], coordinate[1])

# plt.grid()
# plt.show()

WIDTH = 800
HEIGHT = 800 
SIZE = (WIDTH, HEIGHT)
CENTER = (WIDTH//2, HEIGHT//2)
PI = np.pi
pg.init()
pg.display.set_caption("Points")
screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()


screen.fill((255,255,255))
for coordinate in coordArr:
    xC = coordinate[0] + CENTER[0]
    yC = coordinate[1] + CENTER[1]
    xS = xC / (2* PI) * WIDTH
    yS = yC / (2* PI) * HEIGHT 

    pg.draw.circle(screen, (0,0,0), (xS, yS), 1) 
    pg.display.flip()

pg.draw.circle(screen, (0,0,0), CENTER, 2)


running = True
while running: 
    clock.tick(60)
    
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            running = False



