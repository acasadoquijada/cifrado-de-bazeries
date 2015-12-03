# Bazeries
Implementación en python del algoritmo de cifrado [Bazeries](http://serdis.dis.ulpgc.es/~ii-cript/PAGINA%20WEB%20CLASICA/CRIPTOGRAFIA/RECIFRADOS/cifra%20bazeries.htm).

Para esta implementación me he inspirado en la de [Koen Crolla](https://github.com/Cairnarvon/goldbug)

##Introducción

Étienne Bazeries (21 agosto 1846 - 7 noviembre 1931) fue un militar criptoanalista ffrancés activo entre 1890 y el final de la primera guerra mundial. Es conocido por desarrollar el `Cilindro de Bazeries`, una mejora respecto a la versión del cilindro de cifrado de Thomas Jefferson.

Otro hito importante de Bazeries es que en la década de 1890 venció a un gran sistema nomenclador denominado el "Great Cipher", este sistema fue creado por Rossignols en el siglo 17.

Una vez presentado Étienne Bazeries vamos a hablar del algoritmo de cifrado que lleva su nombre.

Se trata de un algoritmo de cifrado clásico, mono-alfabético, basado en transposición y sustitución, para ello se usa la llave y dos matrices.

La entrada del algoritmo es:

* Un texto plano en minúscula o mayúscula sin espacios

* Una llave compuesta únicamente por números

Lo primero que hace el algoritmo es separar el texto plano en bloques según la llave, a su vez cada bloque resultante es invertido. Ejemplo:

Texto plano = textoescondido
Llave = 1325

El texto plano se separaría en bloques de 1 carácter, 3 caracteres, 2 caracteres, 5 caracteres, 1 carácter, 2 caracteres... así hasta que todo el texto este completamente separado. Si el último bloque no se puede completar con lo indicado en la llave no ocurre nada, se deja igual.

El texto resultante tras este paso en nuestro ejemplo es: `t txe eo dnocs i od`

En el siguiente paso contamos con dos matrices, una formada por las letras del alfabeto y la segunda formada por la llave y las letras del alfabeto.

La matriz alfabeto es:

        A F L Q V
        B G M R W
        C H N S X
        D I O T Y
        E K P U Z

La matriz ha de ser 5x5 por lo que debemos descartar alguna letra, en este caso he optando por descartar la `j`.

Para la segunda matriz hay que pasar la llave a sus correspondientes palabras, en este ejemplo suponemos que el idioma es inglés. Ejemplo:

Nuestra llave es 1325, por lo que su conversión a palabras sería: `one thousand three hundred twenty five`

Para construir la segunda matriz usamos las letras no repetidas de la conversión de la llave a palabras, a esto hay que añadirle el resto de las letras de nuestro alfabeto. Ejemplo:

En nuestro caso formaríamos la matriz con: onethusadrwyfiv (letras no repetidas de la llave pasada a palabras) + bcgklmpqxz (alfabeto restante). Dicha matriz quedaría así:

        O N E T H 
        U S A D R 
        W Y F I V 
        B C G J K 
        L M P Q X

Cabe mencionar que la primera matriz se rellena por columnas mientras que la segunda por filas.

Ahora que ya disponemos de las dos matrices vamos a proceder a cifrar el mensaje. Para ello buscamos la posición de cada letra del texto resultante de primer paso en la primera matriz y la sustituimos por la letra que ocupe su misma posición en la segunda matriz. Ejemplo:

Nuestro texto resultante de primer paso es `t txe eo dnocs i od` y aplicando lo comentado arriba nos quedaría: `k kvm mg bfgwi c gb`

Nota: En la explicación del algoritmo de cifrado ponemos el texto cifrado separado en bloques para que resulte mas sencilla la explicación, realmente el texto cifrado va sin ningun tipo de separación.

El descifrado del texto codificado consiste en realizar el paso anterior a la inversa, buscar la posición de cada letra del texto cifrado en la segunda matriz y sustituirla por la letra que ocupe su misma posición en la primera matriz. Ejemplo:

Del texto cifrado `k kvm mg bfgwi c gb` obtendríamos `textoescondido`


##Aproximación a la implementación

Para implementar este algoritmo de cifrado he decidido utilizar python, concretamente su versión 3. He creado una clase `Bazeries` que cuenta con 4 métodos: uno para cifrar, otro para descifrar, un tercero que se encarga de separar el texto en bloques y darle la vuelta a cada uno de ellos, y una función que podemos considerarla "auxiliar" ya que se encarga de invertir una cadena de texto.

En el constructor se inicializa la primera matriz con los valores del alfabeto escogido.

El `método` cifrar recibe un texto a cifrar y una llave para tal objetivo. El método se encarga de procesar el texto dado, por si tiene mayúsculas y/o espacios, tras esto divide la llave en dígitos y los utiliza para separar el texto en bloques como se ha descrito anteriormente, no olvidar que cada bloque es invertido.

Tras eso, pasamos la llave a palabras usando `num2word(llave)` y tras otro procesamiento obtenemos el resultado deseado. Posteriormente generamos la segunda matriz de forma idéntica a lo explicado en el apartado anterior.

Por último se realiza el cifrado del texto plano, este método devuelve el texto cifrado.

El método `descifrar` se encarga únicamente de descifrar y devolver el texto correctamente, para ello se encarga de deshacer el reverso que sufre cada bloque y realiza la sustitución con los valores de la matriz1.

El método `separar_en_grupos` se encarga de separar el texto recibido en bloques según la llave y de invertir el orden de cada bloque.

El método `reverse` se encarga de invertir el orden de una cadena de texto dado.

En el método `main` se construye el objeto Bazeries y se realiza un cifrado y descifrado, presentando los resultados por pantalla.

##Dependencias

Para ejecutar el programa necesitas `num2words` para instalarlo puedes usar `sudo pip3 install num2words` o descargarlo desde [aquí](https://pypi.python.org/pypi/num2words)

##Uso

Hay que recordar que el programa ha de ser ejecutado con python versión 3, de lo contrario fallará.

Tambien es necesario instalar `num2words` para ello basta ejecutar `sudo pip3 install num2wordsv` para que se instale en nuestro sistema.

Para elegir el texto plano a cifrar usamos la variable `texto` del método `main`, para elegir la llave usamos la variable `llave` que también se encuentra en el método `main`

##Posibles ataques

Como hemos comentado, se trata de un algoritmo de cifrado basado en transposición y sustitución, también es mono-alfabético por lo que es susceptible de ser atacado mediante un análisis de frecuencia, este tipo de ataque puede realizarse tanto a mano como utilizando algún software.

Obtener la llave una vez obtenido el texto plano es sencillo:

Imaginemos que tenemos de texto cifrado `kkvmmgbfgwicgb` y mediante un ataque basado en el análisis de frecuencias hemos obtenido `ttxeeodnocsiod` bastaría con ir dándole la vuelta a grupos de palabras hasta que el texto tenga un sentido completo, los tamaños de cada grupo forman la llave.

##Bibliografía

* https://github.com/Cairnarvon/goldbug/blob/master/goldbug/cipher.py

* http://www.thonky.com/kryptos/bazeries-cipher

* https://en.wikipedia.org/wiki/%C3%89tienne_Bazeries


##Licencia

[Licencia](LICENSE)

