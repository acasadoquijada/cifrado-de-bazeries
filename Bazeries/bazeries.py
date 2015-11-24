import itertools
import string
from num2words import num2words # https://pypi.python.org/pypi/num2words
import re

matrix = [[0 for x in range(5)] for x in range(5)]

alfabeto='abcdefghiklmnopqrstuvwxyz'

indices_matriz_alfabeto={}

#Primer square
indice = 0
for i in range(0,5):
    for j in range(0,5):
        matrix[j][i] = alfabeto[indice]
        indices_matriz_alfabeto[alfabeto[indice]] = j,i
        indice = indice + 1


#Sacamos la key de los numeros    
digits = []
key = '1325'
key = int(key)
while key:
    key, d = divmod(key, 10)
    digits.append(d)
digits.reverse()


i = 0

texto = 'sampleplaintext'
texto_reverso = ''

#http://stackoverflow.com/questions/931092/reverse-a-string-in-python

def reverse(text):
    r_text = ''
    index = len(text) - 1

    while index >= 0:
        r_text += text[index] #string canbe concatenated
        index -= 1

    return r_text


# Obtenemos el texto en grupos dados por 'key' y le damos la vuelta a cada grupo
for d in itertools.cycle(digits):

    texto_reverso+=reverse(texto[i:i+d])
    texto_reverso+= ' '
    i +=d

    if( i >= len(texto)):
        break


#Expresiones regulares para quitarme de enmedio - , and
# De la key sacamos las palabras
# Ej: 153 -> one hundred fifty three

numero_a_palabra = num2words(1325)

numero_a_palabra = re.sub(',', '',numero_a_palabra)

numero_a_palabra = re.sub(' and |-| ', '',numero_a_palabra)


#sacamos el second square
pre_llave=''

for i in numero_a_palabra:
    if i not in pre_llave:
        pre_llave+=i


for i in alfabeto:
    if i not in pre_llave:
        pre_llave+=i


matrix2 = [[0 for x in range(5)] for x in range(5)]
indice = 0
indices_matriz_llave = {}
for i in range(0,5):
    for j in range(0,5):
        matrix2[i][j] = pre_llave[indice]
        indices_matriz_llave[pre_llave[indice]] = j,i
        indice = indice + 1


# Procedemos a cifrar

cifrado =''

aux = []
for t in texto_reverso:
    if t != ' ':
        aux = indices_matriz_alfabeto[t]

        cifrado += str(matrix2[aux[0]][aux[1]])

    elif t == ' ':
        cifrado += ' '


# Desciframos
descifrado =''
for t in cifrado:
    if t != ' ':
        aux = indices_matriz_llave[t]

        descifrado += str(matrix[aux[1]][aux[0]])

    elif t == ' ':
        descifrado += ' '


#Volteamos cada paquete y quitamos espacios

descifrado_limpio =''
aux = descifrado.split(" ")

for i in aux:
    descifrado_limpio+=reverse(i)

# Mostramos los resultados

print("Texto original:",texto)
print("Texto original del reves y en bloques:",texto_reverso)
print("Texto cifrado:",cifrado)
print("Texto descifrado del reves y en bloques:",descifrado)
print("Texto descifrado limpio:", descifrado_limpio)





