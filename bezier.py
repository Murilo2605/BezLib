
import matplotlib.pyplot as plt
import math

import numpy

#def EvalBezierCurv(ti, tf, n, p):
#    return P


def basisfunc(t,p):
  """
  Retorna as bases de Bernstein de grau p, avaliadas no ponto t.

  Created on 20/12/2023. 
  """
  B = numpy.empty(p+1)

  for i in range(0,p+1):
    B[i] =  (math.factorial(p)/(math.factorial(i)*math.factorial(p-i)))*(1-t)**(p-i)*t**i

  return B

