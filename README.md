# Bazeries
Implementación en python del algoritmo de cifrado [Bazeries](http://serdis.dis.ulpgc.es/~ii-cript/PAGINA%20WEB%20CLASICA/CRIPTOGRAFIA/RECIFRADOS/cifra%20bazeries.htm).

Para esta implementación me he inspirado en la de [Koen Crolla](https://github.com/Cairnarvon/goldbug)

##Introducción

Se trata de un algoritmo de cifrado clásico que combina transposición y substitución.

La entrada del algoritmo es un texto a cifrar/descifrar y una clave.

Para la clave usamos un entero que tratamos de dos formas:

* Para permutar el texto

* Para sustitución

##Ejemplo

Nuestro texto a cifrar es `estoesunaprueba`, el texto no debe presentar separación de ningun tipo.

Por clave elegimos `1523`

Ahora dividimos el texto en bloques según la clave: bloque de 1 letra, bloque de 5 letras, bloque de 2 letras, bloque de 3 letras, bloque de 1 letra... dividir todo el texto. En este paso cada bloque es invertido

En nuestro caso la salida del primer paso seria: `e seots nu rpa u abe`

Bien, ahora procedamos con la sustitución.

En este paso transformamos la clave a palabras, en este caso en ingles. Para ello hay que usar `num2words` y limpiar la salida para que sea similar a este formato: `onethousandfivehundredtwentythree`

Para la sustitución disponemos de dos matrices:

        A F L Q V
        B G M R W
        C H N S X
        D I O T Y
        E K P U Z

Esta matriz es simplemente el alfabeto.

La segunda matriz comienza por los elementos no repetidos de nuestra clave transformada en palabras, el resto de la matriz se rellena con los elementos del alfabeto que aún no han aparecido. 

Por lo que en nuestro caso la matriz sería:

        O N E T H 
        U S A D F 
        I V R W Y 
        B C G K L 
        M P Q X Z 


Una vez que tengamos las dos matrices podemos comenzar el cifrado, para ello vemos en el texto resultado del paso1 (`e seots nu rpa u abe`) el índice de la primera matriz que pertenece a cada letra y sustituimos esa letra por la correspondiente de la segunda matriz.

Con nuestro texto sería de la siguiente forma:

Buscamos el índice de la letra e, (0,4) y en la salida escribimos la letra correspondiente a ese índice de la matriz2, m. Este paso se repite hasta que todas las letras hayan sido sustituidas.

Nuestro texto cifrado resultante es: `m wmgkw rx dqo x oum`

El descifrado se realiza de forma idéntica al cifrado, solo que primero miramos en la matriz2 y luego en la primera


##Dependencias

Para ejecutar el programa necesitas `num2words` para instalarlo puedes usar `sudo pip install num2words` o descargarlo desde [aquí](https://pypi.python.org/pypi/num2words)


##Licencia

[Licencia](LICENSE)

