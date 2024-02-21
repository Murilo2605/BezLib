#Funções de base

#Avaliar as funções de base em uma dada coordenada t.
import math

def EvalBezierBasis(t, p):

    bvec = []
    
#uma das formas corretas
    for i in range(0,p+1):

        baseFunc =  (math.factorial(p)/(math.factorial(i)*math.factorial(p-i)))*(1-t)**(p-i)*t**i

        bvec.append(baseFunc)

    return bvec



#ocorre erro na função nos seguintes casos

def EvalBezierBasis(t, p):

    bvec = []
    for i in range(-1,p): #de -1 a p, o intervalo i alcança até o penúltimo termo, ou seja, p-1

        baseFunc =  (math.factorial(p)/(math.factorial(i)*math.factorial(p-i)))*(1-t)**(p-i)*t**i

        #Implementação das funções de base via recursão e comparação com equação fatorial
        bvec.append(baseFunc)

    return bvec
        
        #o fatorial (-1) não existe, logo não é possível retornar


def EvalBezierBasis(t, p):

    bvec = []
#ocorre erro na função nos seguintes casos
    for i in range(0,p+2): #de 0 a p+2, o intervalo i alcança até o penúltimo termo, ou seja, p+1
      
           baseFunc =  (math.factorial(p)/(math.factorial(i)*math.factorial(p-i)))*(1-t)**(p-i)*t**i

           #Implementação das funções de base via recursão e comparação com equação fatorial
           bvec.append(baseFunc)
    
    return bvec
           
           #neste caso, não é possível retonar o resultado devido à inexistência do fatorial 


def EvalBezierBasis(t, p):

    bvec = []
    for i in range(1,p+3): #de 1 a p+3, o intervalo i alcança até o penúltimo termo, ou seja, p+2
      
           baseFunc =  (math.factorial(p)/(math.factorial(i)*math.factorial(p-i)))*(1-t)**(p-i)*t**i

           #Implementação das funções de base via recursão e comparação com equação fatorial
           bvec.append(baseFunc)
    
    return bvec
           
           #novamente, não é possível retonar o resultado devido à inexistência do fatorial
           
           #e assim para os demais casos




#  Vetor de bases avaliadas em t (avaliadas em t) EvalBezBasis(t,p,CP) -> considerando que a curva está definida entre 0 e 1.   
#  Assert(t>=0 && t <= 1)

def EvalBezierBasis(t, p, CP):

    bvec = []
    
    
    for i in range(0,p+1):
        assert t>=0 & t<=1

        baseFunc =  (math.factorial(p)/(math.factorial(i)*math.factorial(p-i)))*(1-t)**(p-i)*t**i

        bvec.append(baseFunc)

    return bvec



