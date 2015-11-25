import itertools
import string
from num2words import num2words
import re

class Bazeries:

    alfabeto='abcdefghiklmnopqrstuvwxyz'
    llave=''
    texto=''
    cifrado=''
    descifrado=''
    matrix=[[0 for x in range(5)] for x in range(5)]
    matrix2=[[0 for x in range(5)] for x in range(5)]
    indices_matriz_alfabeto={}
    indices_matriz_llave = {}


    def __init__(self):

        #Rellenamos la primera matriz con el alfabeto
        indice = 0
        for i in range(0,5):
            for j in range(0,5):
                self.matrix[j][i] = self.alfabeto[indice]
                self.indices_matriz_alfabeto[self.alfabeto[indice]] = j,i
                indice = indice + 1




    def cifrar(self, texto, llave):

        # Preprocesamiento del texto
        texto = re.sub(' ', '',texto)

        texto = texto.lower()

        #Actualizamos el valor de texto y llave
        self.texto = texto
        self.llave = llave

        i = 0
        texto_reverso = ''

        # Obtenemos los digitos de la llave
        digitos = []
        llave = int(llave)
        while llave:
            llave, d = divmod(llave, 10)
            digitos.append(d)
        digitos.reverse() 

        # Obtenemos el texto en grupos dados por la llave y le damos la vuelta a cada grupo
        for d in itertools.cycle(digitos):

            texto_reverso+=self.reverse(texto[i:i+d])
            texto_reverso+= ' '
            i +=d

            if( i >= len(texto)):
                break

        # Obtenemos la llave en letras   
        # De la key sacamos las palabras
        # Ej: 153 -> one hundred fifty three

        numero_a_palabra = num2words(llave)

        numero_a_palabra = re.sub(',', '',numero_a_palabra)

        numero_a_palabra = re.sub(' and |-| ', '',numero_a_palabra)


        # Rellenamos la segunda matriz
       

        # aux_matriz2 => String donde se almacena el alfabeto modificado por la clave
        # antes de ser pasado a la matriz

        aux_matriz2='' 

        for i in numero_a_palabra:
            if i not in aux_matriz2:
                aux_matriz2+=i


        for i in self.alfabeto:
            if i not in aux_matriz2:
                aux_matriz2+=i

        # Rellenamos la 2 matriz
        indice = 0

        for i in range(0,5):
            for j in range(0,5):
                self.matrix2[i][j] = aux_matriz2[indice]
                self.indices_matriz_llave[aux_matriz2[indice]] = j,i
                indice = indice + 1


        # Procedemos a cifrar

        aux = []
        for t in texto_reverso:
            if t != ' ':
                aux = self.indices_matriz_alfabeto[t]

                self.cifrado += str(self.matrix2[aux[0]][aux[1]])

            elif t == ' ':
                self.cifrado += ' '

        return(self.cifrado)

    def descifrar(self, texto, llave):

        aux_descifrado=''

        for t in self.cifrado:
            if t != ' ':
                aux = self.indices_matriz_llave[t]

                aux_descifrado += str(self.matrix[aux[1]][aux[0]])

            elif t == ' ':
                aux_descifrado += ' '


        #Volteamos cada paquete y quitamos espacios
        aux_descifrado = aux_descifrado.split(" ")

        for i in aux_descifrado:
            self.descifrado+=self.reverse(i)

        return(self.descifrado)

    #http://stackoverflow.com/questions/931092/reverse-a-string-in-python
    def reverse(self,text):
        r_text = ''
        index = len(text) - 1

        while index >= 0:
            r_text += text[index] 
            index -= 1

        return r_text



if __name__ == "__main__":

    b = Bazeries()

    texto = "holaatodos"
    clave = 123

    cifrado = b.cifrar(texto,clave)

    descifrado = b.descifrar(cifrado,clave)


    print("Texto descifrado:", descifrado)




