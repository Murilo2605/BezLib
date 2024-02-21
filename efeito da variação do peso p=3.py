#efeito da variação do peso p=3

import matplotlib.pyplot as plt
import numpy as np
import math

# Dados da curva de Bézier
# pontos de controle e grau.

p = 3

Pp = []

Px = []
Py = []
Pz = []
Pw = []

Pk = []
Pl = []
Pm = []
Pn = []

Px.append(2)
Px.append(3)
Px.append(5)
Px.append(5)

Py.append(3)
Py.append(4)
Py.append(-1)
Py.append(-4)

Pz.append(2)
Pz.append(3)
Pz.append(5)
Pz.append(5)

Pw.append(3)
Pw.append(4)
Pw.append(-1)
Pw.append(-4)

Pk.append(5)
Pk.append(5)
Pk.append(7)
Pk.append(8)

Pl.append(-4)
Pl.append(-7)
Pl.append(-12)
Pl.append(-11)

Pm.append(5)
Pm.append(5)
Pm.append(7)
Pm.append(8)

Pn.append(-4)
Pn.append(-7)
Pn.append(-12)
Pn.append(-11)
    
P1x = 2
P1y = 3
P1z = 1
P1w = 3
P1k = 5
P1l = -4
P1m = 5
P1n = -4

P2x = 3
P2y = 4
P2z = 3
P2w = 4
P2k = 5
P2l = -7
P2m = 5
P2n = -7

P3x = 5
P3y = -1
P3z = 3
P3w = 6
P3k = 5
P3l = -12
P3m = 5
P3n = -12

P4x = 5
P4y = -4
P4z = 4
P4w = 6
P4k = 8
P4l = -11
P4m = 8
P4n = -11  

#aplicando o peso
Pp.append(4.5)
Pp.append(4.5)
Pp.append(4.5)
Pp.append(4.5)

ti = 0
tf = 1

numpnt = 30
numseg = numpnt-1
delta = (tf - ti) / numseg

x = [ ]
y = [ ]
z = [ ]
w = [ ]
k = [ ]
l = [ ]
m = [ ]
n = [ ]

print("  d = ", delta)

basfunc = [0, 0, 0, 0]

for i in range(1,numpnt):
      t = ti + (i-1) * delta

      basfunc[0] = (1-t)**3
      basfunc[1] = 3*(1-t)**2*t
      basfunc[2] = 3*(1-t)*t**2
      basfunc[3] = t**3

      #efeito da variação do peso
      W = basfunc[0] * Pp[0] + basfunc[1] * Pp[1] + basfunc[2] * Pp[2] + basfunc[3] * Pp[3]

      #base racional
      basfunc[0] = basfunc[0] * Pp[0] / W
      basfunc[1] = basfunc[1] * Pp[1] / W
      basfunc[2] = basfunc[2] * Pp[2] / W
      basfunc[3] = basfunc[3] * Pp[3] / W

      #currX = EvalBez(Px,p,t);     
      #currY = EvalBez(Py,p,t);
      currX = Px[0] * basfunc[0] + Px[1] * basfunc[1] + Px[2] * basfunc[2] + Px[3] * basfunc[3] 
      currY = Py[0] * basfunc[0] + Py[1] * basfunc[1] + Py[2] * basfunc[2] + Py[3] * basfunc[3] 
      currZ = Pz[0] * basfunc[0] + Pz[1] * basfunc[1] + Pz[2] * basfunc[2] + Pz[3] * basfunc[3] 
      currW = Pw[0] * basfunc[0] + Pw[1] * basfunc[1] + Pw[2] * basfunc[2] + Pw[3] * basfunc[3]

      currK = Pk[0] * basfunc[0] + Pk[1] * basfunc[1] + Pk[2] * basfunc[2] + Pk[3] * basfunc[3] 
      currL = Pl[0] * basfunc[0] + Pl[1] * basfunc[1] + Pl[2] * basfunc[2] + Pl[3] * basfunc[3] 
      currM = Pm[0] * basfunc[0] + Pm[1] * basfunc[1] + Pm[2] * basfunc[2] + Pm[3] * basfunc[3] 
      currN = Pn[0] * basfunc[0] + Pn[1] * basfunc[1] + Pn[2] * basfunc[2] + Pn[3] * basfunc[3]
      
      #distancia da curva calculada
      soma = 0        
      soma = soma - currX*currY

      #imprimindo os resultados 
      print("peso = ", W)
      print(" X = ", currX)  
      print(" Y = ", currY)
      print(" dist = ", soma)
      
      x.append(currX)
      y.append(currY)
      z.append(currZ)
      w.append(currW)
      k.append(currK)
      l.append(currL)
      m.append(currM)
      n.append(currN)
      
      #vetor de base
      bvec = []

      for i in range(0,p+1):
           
           #função de base
           baseFunc =  (math.factorial(p)/(math.factorial(i)*math.factorial(p-i)))*(1-t)**(p-i)*t**i

           bvec.append(baseFunc)

           # escaneando as funções de base em relação às funções vetoriais
           print("baseFunc = ", baseFunc)       
       
#plotando as curvas
plt.plot(x, y, z, w, k, l, m, n, color = 'blue')
plt.plot(Px, Py, Pz, Pw, Pk, Pl, Pm, Pn, Pp, "--", color = 'red')
plt.title("curva")
plt.xlabel("x")
plt.ylabel("y")

#apresentando o gráfico
plt.grid()
plt.show()
