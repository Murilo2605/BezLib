#Efeito da variação do peso no qual p = 2

import matplotlib.pyplot as plt
import numpy as np
import math

# Dados da curva de Bézier
# pontos de controle e grau.

p = 2


Px = []
Py = []
Pw = []

Px.append(-1)
Px.append(-1)
Px.append(0)

Py.append(0)
Py.append(1)
Py.append(1)

Pw.append(2)
Pw.append(2)
Pw.append(2)

P1x = 0
P2x = 1
P3x = 3/2
P4x = 3

P1y = 0
P2y = 4/3
P3y = 2
P4y = 4

ti = 0
tf = 1

numpnt = 30
numseg = numpnt-1
delta = (tf - ti) / numseg

x = [ ]
y = [ ]

print("  d = ", delta)

basfunc = [0, 0, 0]

for i in range(1,numpnt):
      t = ti + (i-1) * delta

      basfunc[0] = (1-t)**2
      basfunc[1] = (2*(1-t)*t)
      basfunc[2] = t**2

      #efeito da variação do peso
      W = basfunc[0] * Pw[0] + basfunc[1] * Pw[1] + basfunc[2] * Pw[2]

      #base racional
      basfunc[0] = basfunc[0] * Pw[0] / W
      basfunc[1] = basfunc[1] * Pw[1] / W
      basfunc[2] = basfunc[2] * Pw[2] / W


      currX = Px[0] * basfunc[0] + Px[1] * basfunc[1] + Px[2] * basfunc[2]
      currY = Py[0] * basfunc[0] + Py[1] * basfunc[1] + Py[2] * basfunc[2]

      #distancia da curva calculada
      soma = 0        
      soma = soma - currX*currY


      #currX = EvalBez(Px,p,t);     
      #currY = EvalBez(Py,p,t);

      #escaneando os resultados e
      print("peso = ", W)
      print(" X = ", currX)  
      print(" Y = ", currY)
      print(" dist = ", soma)
      
      x.append(currX)
      y.append(currY)

      bvec = []

      for i in range(0,p+1):
      
           baseFunc =  (math.factorial(p)/(math.factorial(i)*math.factorial(p-i)))*(1-t)**(p-i)*t**i

           bvec.append(baseFunc)

           # escaneando as funções de base em relação às funções vetoriais
           print("baseFunc = ", baseFunc)       
       

plt.plot(x, y, color = 'blue')
plt.plot(Px, Py, "--", color = 'red')
plt.title("curva")
plt.xlabel("x")
plt.ylabel("y")

plt.grid()
plt.show()
