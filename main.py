import math

import numpy as np
from matplotlib import pyplot as plt

valid = False
while not valid:
    try:
        a = int(input("Digite el valor de A: "))             #demanda anual
        valid = True
    except ValueError:
        print('Por favor, ingrese números enteros')

valid = False
while not valid:
    try:
        cp = float(input("Digite el valor de Cp: "))        #costo de ordenar el lote
        valid = True
    except ValueError:
        print('Por favor, ingrese números enteros')

valid = False
while not valid:
    try:
        ch = float(input("Digite el valor de Ch: "))        #costo de mantener
        valid = True
    except ValueError:
        print('Por favor, ingrese números enteros')


# q = 25
# cp = 1417.61
# a = 115
# ch = 535.30

# optimun quantity to be ordered
q = round(math.sqrt(2*a*cp/ch))

# iterated array to hold the possible number of units
# it increases in steps of 4 until 68
unity = np.arange(4, 70, 4)

#creating 2d arrays to hold the values
cpArray = np.zeros(17)
chArray = np.zeros(17)
ctArray = np.zeros(17)

# generating data for comparison and populate the graph plot
for i, new_val in enumerate(unity):
    cpArray[i] = cp * (a / unity[i])
    chArray[i] = ch * (unity[i] / 2)
    ctArray[i] = cpArray[i] + chArray[i]

def CT(q):
    return (a/q)*cp + (q/2)*ch


# plotting
plt.title("Costos EOQ")
plt.xlabel("El valor de cantidad económica óptima es: " + str(q))
plt.plot(np.array(chArray), color="green")
plt.plot(np.array(cpArray), color="red")
plt.plot(np.array(ctArray), color="blue")
# plt.plot(q, CT(q), 'r+')
plt.xticks(range(len(unity)), unity)


# showing the graph plot
plt.show()


