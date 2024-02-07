
import matplotlib.pyplot as plt
import math

def EvalBezierCurv(ti, tf, n, p):
    return P

# aqui 2

#1 Dada uma curva de Bézier (grau p e pontos)


import matplotlib.pyplot as plt

    # Dados da curva de Bézier

    # pontos de controle e grau.

p = 3

Px = []
Py = []

Px.append(2)
Px.append(3)
Px.append(5)
Px.append(5)
Py.append(3)
Py.append(4)
Py.append(-1)
Py.append(-4)
    
P1x = 2
P1y = 3
P2x = 3
P2y = 4
P3x = 5
P3y = -1
P4x = 5
P4y = -4    



ti = 0
tf = 1

numpnt = 30
numseg = numpnt-1
delta = (tf - ti) / numseg

x = [ ]
y = [ ]

print("  d = ", delta)


for i in range(1,numpnt):
      t = ti + (i-1) * delta
      currX = Px[0] * (1-t)**3 + Px[1] * 3*(1-t)**2*t + Px[2] * 3*(1-t)*t**2 + Px[3] * t**3
      currY = Py[0] * (1-t)**3 + Py[1] * 3*(1-t)**2*t + Py[2] * 3*(1-t)*t**2 + Py[3] * t**3

      #currX = EvalBez(Px,p,t);     
      #currY = EvalBez(Py,p,t);

      print(" X = ", currX)
      print(" Y = ", currY)
      
      x.append(currX)
      y.append(currY)


plt.plot(x, y, color = 'blue')
plt.plot(Px, Py, "--", color = 'red')
plt.title("curva")
plt.xlabel("x")
plt.ylabel("y")



plt.grid()
plt.show()


# 
#  Avaliar as funções de base em uma dada coordenada t.

def EvalBezierBasis(t, p):

    bvec = []
    
    
    for i in range(0,p+1):

        baseFunc =  (math.factorial(p)/(math.factorial(i)*math.factorial(p-i)))*(1-t)**(p-i)*t**i

        bvec.append(baseFunc)

    return bvec

# 
#  Vetor de bases avaliadas em t (avaliadas em t) EvalBezBasis(t,p,CP) -> considerando que a curva está definida entre 0 e 1.   
#  Assert(t>=0 && t <= 1)

def EvalBezierBasis(t, p, CP):

    bvec = []
    
    
    for i in range(0,p+1):
        #assert t>=0 & t<=1

        baseFunc =  (math.factorial(p)/(math.factorial(i)*math.factorial(p-i)))*(1-t)**(p-i)*t**i

        bvec.append(baseFunc)

    return bvec

#  



