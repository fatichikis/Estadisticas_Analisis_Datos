#para hacer todos juntos
import numpy as np
import math
from decimal import Decimal
import numpy as np


Vectorx1 = np.matrix((input("Ingresa el valor del vector original\n")))
#ingresamos cuantos valores vamos a restar (nuestro caso 10)
n = int(input("Cuantos vectores va comparar con el original:"))
#arreglo para guardar esos datos
arr = []
restavectores =[]
multiplicacion3=[]
resultadosumavectoe=[]
mostrandodatos=[]
resultadopaso2=[]
resultadopaso3=[]
resultado4=[]
sumatoriafinaldetodoslosvectores=[]
resultadoxnmultiysuma=[]
resultadofinaldelosfinales=[]
mostrandodatos2=[]
variablearraynueva=[]
variablearraynueva2=[]
sumatoriafinalmultiplicacionesvectores=[]
sumatoriafinaldetodoslosvectoresmultiplicados=[]
for i in range(n):
    print("Ingresa el valor del vector \n ",i)
    Vectorxn= np.matrix((input()))
    arr.append(Vectorxn)
#comenzamos con el ciclo para mostrar restas
for _ in range(n):
    mostrandodatos=Vectorx1,arr[_]
    print("El vector que se esta realizando es:")
    print(mostrandodatos)
    print''
    print("La resta de su vector ",arr[_], "Es:")
    restavectores= Vectorx1 - arr[_]
    transpose= np.transpose(restavectores)
    print(transpose)
    #
    print("La Multiplicacion de su vector",arr[_], "Es:")
    multiplicacion3= transpose*restavectores
    print(multiplicacion3)
    #
    print("La SUMA de su vector",arr[_], "Es:")
    sumavector=np.around(np.sum([multiplicacion3],axis=0),decimals = 2)
    resultadosumavectoe=sumavector.sum(axis=0)
    print(resultadosumavectoe)
    #
    print("Operacion de 1/.18",arr[_], "Es:")
    resultadopaso2=np.around((abs(resultadosumavectoe)/.18), decimals = 2)
    print(resultadopaso2)
    #
    print("Operacion de elevar al 2.71",arr[_], "Es:")
    resultadopaso3=np.around((pow(resultadopaso2, 2.71)), decimals = 2)
    print(resultadopaso3)
    #
    print("Operacion de multiplicar * 0.025",arr[_], "Es:")
    resultado4=np.around((resultadopaso3*0.025), decimals = 2)
    print(resultado4)
    print''
    #
    vectoresquesevanasumar= np.matrix([resultado4])
    variablearraynueva.append(vectoresquesevanasumar)
    #
    sumatoriafinaldetodoslosvectores=np.around(np.sum([variablearraynueva],axis=1),decimals = 2)
    #
if n==n:
     print("Los vectores que se van a sumar son:")
     print(variablearraynueva)
     print''
     print("La Suma de todos los vectores es:")
     print(sumatoriafinaldetodoslosvectores)
     print''
for w in range(n):
    pass
    print("Multiplicacion de la suma final de vectores del vector:" ,arr[w])
    b = np.matrix(sumatoriafinaldetodoslosvectores)
    resultadoxnmultiysuma=np.around(np.multiply(arr[w],b),decimals = 2)
    print(resultadoxnmultiysuma)
    print''
    #
    sumatoriafinalmultiplicacionesvectores=np.array([resultadoxnmultiysuma])
    variablearraynueva2.append(sumatoriafinalmultiplicacionesvectores)
    #
    sumatoriafinaldetodoslosvectoresmultiplicados=np.around(np.sum([variablearraynueva2],axis=1),decimals = 2)
    #
    resultadofinaldelosfinales=sumatoriafinaldetodoslosvectores
    resultadofinaldelosfinales2=sumatoriafinaldetodoslosvectoresmultiplicados
    resultadorte=resultadofinaldelosfinales,"/",resultadofinaldelosfinales2
    resultadodivisionfinal=np.nan_to_num(abs(resultadofinaldelosfinales/resultadofinaldelosfinales2))


if n==n:
    print("Suma Final de las multiplicaciones es:")
    print(sumatoriafinaldetodoslosvectoresmultiplicados)
    print''
    print("Division para obtener resultado final es el siguiente:")
    print(resultadorte)
    print''
    print("El resultado Final del vector:", Vectorx1, "ES:")
    print(resultadodivisionfinal)
    print''
    #
