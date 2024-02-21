#Exemplo de uma curva de Bézier no qual p = 3

import matplotlib.pyplot as plt
import math
from sympy import *

#1 Dada uma curva de Bézier (grau p e pontos)

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

#número de pontos
numpnt = 30
#número de segmentos
numseg = numpnt-1
delta = (tf - ti) / numseg

x = [ ]
y = [ ]

print(" d = ", delta)

for i in range(1,numpnt):
      #equação do tempo
      t = ti + (i-1) * delta

      #equações das curvas
      #currX = EvalBez(Px,p,t);     
      #currY = EvalBez(Py,p,t);
      currX = Px[0] * (1-t)**3 + Px[1] * 3*(1-t)**2*t + Px[2] * 3*(1-t)*t**2 + Px[3] * t**3
      currY = Py[0] * (1-t)**3 + Py[1] * 3*(1-t)**2*t + Py[2] * 3*(1-t)*t**2 + Py[3] * t**3

      #escaneando os resultados de ambas as equações
      print(" X = ", currX)
      print(" Y = ", currY)
      
      #adicionando dados 
      x.append(currX)
      y.append(currY)

      #vetor da base
      bvec = []

      for i in range(0,p+1): #de 0 a p+1, o intervalo i alcança até o penúltimo termo, ou seja, p
      
           baseFunc =  (math.factorial(p)/(math.factorial(i)*math.factorial(p-i)))*(1-t)**(p-i)*t**i

           #Implementação das funções de base via recursão e comparação com equação fatorial
           bvec.append(baseFunc)

           # escaneando as funções de base em relação às funções vetoriais
           print("baseFunc = ", baseFunc)      
 
       
#calculando o comprimento da curva por meio do método iterativo de Gauss-Seidel
soma = 0
soma = soma - currX*currY    #sinal negativo devido ao resultado da curva Y
           
#escaneando o comprimento da curva
print("distance Curve = ", soma)
           
#plotando o gráfico com as curvas
plt.plot(x, y, color = 'blue')
plt.plot(Px, Py, "--", color = 'red')
plt.title("curva")
plt.xlabel("x")
plt.ylabel("y")

#apresentando o gráfico
plt.grid()
plt.show()

