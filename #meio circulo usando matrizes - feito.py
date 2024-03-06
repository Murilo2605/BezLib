#meio circulo usando matrizes  test1

import matplotlib.pyplot as plt
import numpy as np
import math

p = 2

#p_0 = [-0.5,0,]
#p_1 = [-0.5,0.5]
#p_2 = [0,0.5]
#p_3 = [0.5,0]
#p_4 = [0.5,0.5]
#p_5 = [0,0.5]
p_0 = []
p_1 = []
p_2 = []
p_3 = []
p_4 = []
p_5 = []
p_6 = []
p_7 = []

#excluindo o np.array...
#apenas usando os pontos, sem os pesos
p_0.append(-0.5)
p_0.append(-0.5)
p_0.append(0)

#p_1.append(-0.5)
#p_1.append(0.5)
p_1.append(0)
p_1.append(0.5)
p_1.append(0.5)

#p_2.append(0)
#p_2.append(0.5)
p_2.append(0.5)
p_2.append(0.5)
p_2.append(0)

#p_3.append(0.5)
#p_3.append(0)
p_3.append(0)
p_3.append(0.5)
p_3.append(0.5)

#p_4.append(0.5)
#p_4.append(0.5)
p_4.append(-0.5)
p_4.append(-0.5)
p_4.append(0)

#p_5.append(0)
#p_5.append(0.5)
p_5.append(0)
p_5.append(-0.5)
p_5.append(-0.5)

p_6.append(0.5)
p_6.append(0.5)
p_6.append(0)

p_7.append(0)
p_7.append(-0.5)
p_7.append(-0.5)

ti = 0
tf = 1

numpnt = 3000
numseg = numpnt-1
delta = (tf - ti) / numseg

x = []
y = []
a = []
b = []
d = []
e = []
g = []
h = []

print("  d = ", delta)

basfunc = [1, 1, 1]


for i in range(1,numpnt):
      t = ti + (i-1) * delta

      basfunc = np.empty(3)
      b0 = (1-t)**2
      b1 = (2*(1-t)*t)
      b2 = t**2
      basfunc[0] = b0
      basfunc[1] = b1
      basfunc[2] = b2
      print(basfunc)
      print(t)
      currX = p_0[0] * b0 + p_0[1] * b1 + p_0[2] * b2
      currY = p_1[0] * b0 + p_1[1] * b1 + p_1[2] * b2
      
      #currX = pnt_0
      #currY = pnt_1

      currA = p_2[0] * b0 + p_2[1] * b1 + p_2[2] * b2
      currB = p_3[0] * b0 + p_3[1] * b1 + p_3[2] * b2
      currD = p_4[0] * b0 + p_4[1] * b1 + p_4[2] * b2 
      currE = p_5[0] * b0 + p_5[1] * b1 + p_5[2] * b2
      currG = p_6[0] * b0 + p_6[1] * b1 + p_6[2] * b2 
      currH = p_7[0] * b0 + p_7[1] * b1 + p_7[2] * b2

      P_0 = p_0[0] * basfunc.transpose( )
      P_1 = p_1[0] * basfunc.transpose( )
      P_2 = p_2[0] * basfunc.transpose( )
      P_3 = p_3[0] * basfunc.transpose( )
      P_4 = p_4[0] * basfunc.transpose( )
      P_5 = p_5[0] * basfunc.transpose( )
      P_6 = p_6[0] * basfunc.transpose( )
      P_7 = p_7[0] * basfunc.transpose( )

      P__0 = p_0[1] * basfunc.transpose( )
      P__1 = p_1[1] * basfunc.transpose( )
      P__2 = p_2[1] * basfunc.transpose( )
      P__3 = p_3[1] * basfunc.transpose( )
      P__4 = p_4[1] * basfunc.transpose( )
      P__5 = p_5[1] * basfunc.transpose( )
      P__6 = p_6[1] * basfunc.transpose( )
      P__7 = p_7[1] * basfunc.transpose( )

      P___0 = p_0[2] * basfunc.transpose( )
      P___1 = p_1[2] * basfunc.transpose( )
      P___2 = p_2[2] * basfunc.transpose( )
      P___3 = p_3[2] * basfunc.transpose( )
      P___4 = p_4[2] * basfunc.transpose( )
      P___5 = p_5[2] * basfunc.transpose( )
      P___6 = p_6[2] * basfunc.transpose( )
      P___7 = p_7[2] * basfunc.transpose( )


      x.append(currX)
      y.append(currY)
      a.append(currA)
      b.append(currB)
      d.append(currD)
      e.append(currE)
      g.append(currG)
      h.append(currH)

print(P_0, P__0, P___0)
print(P_1, P__1, P___1)
print(P_2, P__2, P___2)
print(P_3, P__3, P___3)
print(P_4, P__4, P___4)
print(P_5, P__5, P___5)
print(P_6, P__6, P___6)
print(P_7, P__7, P___7)


      

      
plt.plot(p_0, p_1, p_2, p_3, p_4, p_5, p_6, p_7, color = 'blue')
plt.plot(x, y, a, b, d, e, g, h,"--", color = 'red')
plt.title("Círculo de Bézier da forma matricial")
plt.xlabel("x")
plt.ylabel("y")

plt.grid()
plt.show()

