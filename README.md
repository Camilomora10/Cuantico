# Experimento de la doble Rendija

El experimento de la doble rendija se hizo con la intención de determinar si la luz se comportaba como onda o como partícula. En este repositorio intentaremos estudiar y entender el comportamiento del universo cuántico entendiendo sus fundamentos mas básicos, y realizaremos un experimento para poder demostrarlo.

* ## Inicios

El experimento de la doble rendija fue planteado originalmente en 1801 por Thomas Young y lo hizo con la intención de determinar si la luz se comportaba como onda o como partícula, actualmente este experimento se repoduce en una cámara oscura la cual deja entrar un haz de luz por una rendija estrecha, cuando la luz llega a una pared intermedia de dos rendijas, la luz debe pasar por alguna de estas dos y chocar con una placa que se encuentra después de la rendija.
En la siguiente imagen se pude observar cómo es el comportamiento de las partículas en el experimento.

![image](https://github.com/Camilomora10/Cuantico/blob/master/.idea/rendija.jpg)

* ## Explicacion

En el experimento se uso un láser que arroja un haz de luz sobre una placa de papel aluminio. Si esta tiene una sola abertura o rendija entonces tendremos la proyección de un solo punto la luz pasa por una sola rendija, esto representa un sistema clásico deterministico, es decir que podemos observar y predecir un patrón sobre una pared cuando usamos el láser, tal como se presenta en la siguiente imagen teórica resultado.

![image](https://github.com/Camilomora10/Cuantico/blob/master/.idea/0BA.jpg)
El experimento de doble rendija (Crédito de la imagen: GIPhotoStock / Science Photo Library)

Si cambiamos un poco del sistema utilizando dos rendijas en teoría si nos ceñimos a los resultados anteriores pudimos predecir que se presentará el mismo patrón solo que en dos regiones por que la mitad de la dispersión total se trasladará a la otra rendija, sin embargo el resultado es totalmente diferente pues se da un patrón en cual las probabilidades no encajan para explicarlo tendremos que cambiar de un sistemas clásico a un sistemas cuántico. En la mecánica cuántica se puede predecir este patrón con la función de onda de Erwin Schrödinger que describe un campo en todos los puntos del espacio con números complejos, que posteriormente Niels Bohr descubrió que la norma al cuadrado de esos puntos obtenía otro campo capaz de predecir probabilisticamente el mundo cuántico.

Ahora que sabemos predecir el patrón, podemos explicar mejor que pasa con variaciones del experimento para entender mejor los resultados anteriores un ejemplo es lo que pasa si de amplia o reduce la distancias entre rendijas, pues a pesar que se repite el patrón este sufre un cambio de distancias en las proyecciones, esto se debe a que la función de onda de Schrödinger que causa que el estado del sistema sufra superposición de estados (donde se acentúan las proyecciones) e interferencia con el cancelamiento de algunas proyecciones, no obstante la relación de la separación entre distancias de separación y proyección se debe a un entrelazamiento de estados que interpreta dicha distancia proectandose en los resultados

* ## Experimento

Para realizar la simulación del experimento se debe apuntar con un láser a la redija ya creada y montada, según lo observado se ve que el resultado se asemeja más al comportamiento de ondas con el patrón de interferencia. A continucacion te mostramos que necesitas para elaborar el experimento.

**Materiales**
* Un laser
* Cinta aislante negra 
* Cartulina blanca
* Una aguja
* Alambre

![image](https://github.com/Camilomora10/Cuantico/blob/master/.idea/materiales.jpeg)

**Pasos**

* Colocamos un trozo alambre en la mitad del laser logrando el efecto de la doble rendija y con ayuda de la cinta aislante la sujetamos:

![image](https://github.com/Camilomora10/Cuantico/blob/master/.idea/laser.jpeg)

* Para la rendija con ayuda de la aguja cortamos el papel aluminio dos surcos para tener el efecto de doble rendija. Y la colocamos sobre una base para que no se mueva.

![image](https://github.com/Camilomora10/Cuantico/blob/master/.idea/papel.jpeg)

* Ahora preparamos una base con un altura muy similar a la que usamos con el papel aluminio. Y sujetamos el laser a esta.
Tenga en cuenta que la luz del laser debe apuntar por los surcos que tiene el papel aluminio.

![image](https://github.com/Camilomora10/Cuantico/blob/master/.idea/sistemas.jpeg)

* Por ultimo Colocamos la cartulina en la dirreccion que apunta el laser, con el fin de que se pueda observar mejor el patron de interferencia.

![image](https://github.com/Camilomora10/Cuantico/blob/master/.idea/cartulina.jpeg)

* ## Resultado

Acontinuacion el resultado es el de patrón de interferencia de las ondas que hallamos en nuestro experimento:

![image](https://github.com/Camilomora10/Cuantico/blob/master/.idea/resultado1.jpeg)
![image](https://github.com/Camilomora10/Cuantico/blob/master/.idea/resultado2.jpeg)
![image](https://github.com/Camilomora10/Cuantico/blob/master/.idea/resultado3.jpeg)

A continuación un vistazo con mas detalle sobre el experimento realizado, en el siguiente enlace:

```
https://www.youtube.com/watch?v=__paV0TRzA0
```

* ## Explicacion

Para poder lograr entender el resultado del experimento en la época aplicaron el principio de superposición cuántico en el que dice que las partículas (en este caso la luz) puede dos o más valores de una determinada magnitud (su posición ) tambien conocida como "onda de posibilidades" que pasan por las dos ranuras para luego interferir con ella misma hasta que golpear la pared de impacto y que al ser monitoreado este se ve afectado a que se dice que este principio colapsa y solo lograremos observar una de todos los posibles resultados.

* ## Simulacion del Experimento

Para las simulaciones utilizamos un modelo matemático basado en los grafos del sistema y las matrices adyacencia propias de los mismos, posteriormente realizamos una simulación en la librería_sistema_cuantico en python que se encuentra en el repositorio de la siguiente direccion:
```
https://github.com/Camilomora10/Cuantico.git
```
También tendremos en cuenta la forma en el que el experimento se representara, entonces el sistema tendra una matriz asociada y a su vez un vector de estado inicial.
A continuacio el Grafo del experimento:

![image](https://github.com/Camilomora10/Cuantico/blob/master/.idea/grafo.png)

A continuacio la matriz del experimento:

![image](https://github.com/Camilomora10/Cuantico/blob/master/.idea/matriz_sis.png)

* ## Simulacion en  la libreria
```
c1 = [[-1 / (6 * 0.5)],[ 1 / (6 ** 0.5)]]
c2 = [[-1 / (6 ** 0.5)],[ -1 / (6 ** 0.5]]
c3 = [[1 / (6 ** 0.5)],[ -1 / (6 ** 0.5]]

Matriz = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
         [[1/2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
         [[1/2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
         [[0, 0], c1, [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
         [[0, 0], c2, [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
         [[0, 0], c3, c1, [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
         [[0, 0], [0, 0], c2, [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
         [[0, 0], [0, 0], c3, [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]
vector_estado = [[[1, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]], [[0, 0]]]
```

* ## Libreria exportadas

Para conocer el manejo de las librerias que mencionamos anteriorimente, dirigete al siguiente repositorio, alli te explicaran el paso a paso de como puedes usarlas.

```
https://github.com/Camilomora10/Tencologia-CNYT1
```
# Sistemas Clasicos Y Cuanticos
Ademas completamos retos de programación realizando los siguientes experimentos:
* Los experimentos de la canicas con coeficiente booleanos
* Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
* Experimento de las múltiples rendijas cuántico.
* Cree una función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados. La imagen se debe poder guardar en el computador con un formato de imagen.

Estos experimentos se encuentran en el capitulo 3 del libro [Quantum Computing for Computer Scientists](https://www.researchgate.net/publication/252906420_Quantum_Computing_for_Computer_Scientists_NS_Yanofsky_and_MA_Manucci) (Click para ver). De el autor N.S. Yanofsky and M.A. Manucci.

## Pre-requisitos
Para que puedas usar nuestra libreia de numeros complejos necesitaras un ordenador con caracteristicas adecuadas para ejecutar un lenguaje de programacion, ademas de un programa en el cual puedas usar el lenguaje de programacion, donde podras usar nuestras librerias.
El lenguaje de programacion que usaremos sera phyton el cual lo puedes ejecutar desde consolas como lo son ide o PyCharm entre otros.

## Instalacion
Para que puedas usar las funciones de los numeros complejos primero tendras que cumplir con algunas condiciones:
1. Descargar el lenguaje de programacion [phyton](https://www.python.org/downloads/)(click para descargar), ya que nuestras librerias se basan en este lenguaje,usa versiones superiores a la 3 para que no tengas problemas con el uso de librerias externas.
2. Necesitaras una consola donde puedas ejecutar phyton, en este caso usaremos [PyCharm Comiunity](https://www.jetbrains.com/es-es/pycharm/download/#section=windows)(click para descargar) pero tu podras usar la que quieras.
3. Descarga las librerias correspondientes que deseas usar, Dirijase a la opcion ¨Codigo¨ en el inicio de este repositorio, Allí podras descargar los archivos en formato zip.A continuacion te presentamos las librerias con que contamos:
   * [Libreria de Operaciones Basicas de Numeros Complejos](https://github.com/Camilomora10/Cuantico/blob/master/libreriaComplejos.py).(click para ver)
   * [Libreria de matrices y Vectores Complejos](https://github.com/Camilomora10/Cuantico/blob/master/vectores_matrices.py).(click para ver)
   * [Libreria Sistemas Clasicos y Cuanticos](https://github.com/Camilomora10/Cuantico/blob/master/libreria_sistema_clasico_cuantico.py).(click para ver)
4. Una vez descargado el archivo zip descomprimelo,  Allí podras encontrar las librerias estas se caracterizan por terminar en .py.
5. Una vez descargadas las librerias inicialas en la aplicacion pycharm commiunity en la ventana file-open, Allí selecciona la ubicacion donde descargaste las librerias.
6. Una vez abiertas podra ver las funciones de los numeros complejos y poder usarlas. ¡Disfrutalas!

Adicionalmente usamos librerias externa que debes tener instaladas en tu consola para que te funcionen todas nuestras librerias.
* [Numpy](https://numpy.org/)(Click para descargar).
* [matplotlib](https://matplotlib.org/downloads.html)(Click para descargar).

Mira el siguiente Tutorial para instalar las librerias en Pycharm Commiunity:
* [Importar librerias PyCharm Commiunity](https://www.youtube.com/watch?v=aROm4KYHXLI)(Click para ver).

## Manual de Uso
 * ## Introduccion
Antes de empezar se debe tener en cuenta la forma en que los numeros complejos seran representados, como se sabe los numeros complejos se caracterizan por tener una parte real  y una imaginaria como se observa a continuacion:
```
a + bi
```
lo equivalente para la libreria sera una lista de longitud 2, cuya posicion 0 sera la parte real y la posicion 1 la parte imaginaria; con respecto al numero anterior el equivalente en la libreria  sera:

```
[a,b]
```
Ademas para representar vectores y matrizes lo haremos por medio de listas en donde la longitud de la lista seran las filas y las columnas la longitud de las filas.

* Una matriz de tamaño 2x2 compleja seria:
```
 | a + bi   c + di |
 | e + fi   g - hi |
```
En nuestra libreria sera:
```
[ [[a,b],[c,d]], [[e,f],[g,h]] ]
```
* Un vector de 2 elementos complejo seria:
```
 | a + bi |
 | c + di |
```
En nuestra libreria sera:
```
[ [[a,b]], [[e,f]] ]
```
* Un numero en forma polar sera:
```
(r, θ) 
```
En nuestra libreria sera:
```
[r, θ] 
```
* Simulaciones y Experimentos Cuanticos:


1. simulation de experimento de la canicas con coeficiente booleanos:
Son matrizes y vectores que todos sus componentes son booleanos
```
matriz = [[bool], [bool], [bool], ....] 

vector = [bool, ...]

```

2. Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas. 
Son matrizes y vectores que todos sus componentes son Numeros complejos de la forma a + bi([a,b])
```
matriz = [[[a,b], [c,d], ...], ....]

vector = [[e,f], [i,h], ...] 
```

3. Experimento de las múltiples rendijas cuántico.
Son matrizes y vectores que todos sus componentes son Numeros complejos de la forma a + bi([a,b]) y el vector prob (probabilidad) es un vector con elementos ded tipo float.
```
matriz = [[[a,b], [c,d], ...], ....]

vector = [[e,f], [i,h], ...] 
proba = [float, ...]
```

4. Diagrama de barras que muestre las probabilidades de un vector de estados:
el vector prob (probabilidad) es un vector con elementos ded tipo float.
```
Prob = [float, ...]
```

 * ## ¿Cómo usar las Funciones?
 Para que puedas usar las funciones de los numeros complejos abre la libreria que deseas usar y dirigete al final del archivo, digita main y dale enter, te aparesera lo sieguiente:
 
```
if__name__ == '__main__': 
```
Ahora crea una variable respuesta en donde su valor sera el resultado de la operacion que deseas usar e imprimelo.
 ```
if__name__ == '__main__': 
    respuesta = operacion
    print(respuesta)
```
Cambia "respuesta" por la operacion que deseas realizar, allí podras digitara los parametros que requiere la operacion compleja, luego dale Run en la consola y automaticamente te aparecera la respuesta de la operacion que usaste. A continuacion un ejemplo:
 1. Coloca la operacion que deseas realizar:
```
if__name__ == '__main__': 
    respuesta = suma_complejos()
    print(respuesta)
```
2. Digite los parametros:
```
if__name__ == '__main__': 
    respuesta = suma_complejos([12,3],[4,6])
    print(respuesta)
```
3. Salida del Resultado:
```
(17,7)
```
 * ## Documentacion
 Es necesario que conozcas que operacion realiza cada funcion y cuales son los parametros que debes ingresar para poder usarla, por eso te mostramos la documuentacion de las librerias que manejamos.
 1. [Documentacion Complejos](https://github.com/Camilomora10/LIBRERIAS-CNYT/blob/master/documentacion1.md).(click para ver)
 2. [Documentacion Matrizes y Vectores](https://github.com/Camilomora10/LIBRERIAS-CNYT/blob/master/documentacion2.md).(click para ver)
 3. [Documentacion Sistemas Cuanticos](https://github.com/Camilomora10/Tecnologia/blob/master/documentacion3.md).(click para ver)
 
 * ## Pruebas
Las pruebas en un programa nos permiten verificar que las funcionalidades del programa se cumplan correctamente,usamos la biblioteca unittest de python con el parámetro assertEqual para comparar las respuestas.
Para este caso usaremos la libreria de python unittest ; la cual es usada para comparar un resultado con otro diciendo si son iguales o no, esta es importada con la línea de codigo import unittest, y la puedes encontrar en nuestro repositorio en formato .py. Los archivos de prueba con que contamos son:
1. [Unittest Numeros Complejos](https://github.com/Camilomora10/Tencologia-CNYT1/blob/master/test_complejo.py).(click para ver)
2. [Unittest Matrices y Vectores](https://github.com/Camilomora10/Tencologia-CNYT1/blob/master/test_matrices.py).(click para ver)
3. [Unittest Sistemas Clasicos y Caunticos](https://github.com/Camilomora10/Tencologia-CNYT1/blob/master/test_cuantico.py).(click para ver)

A continuacion se mostrara un ejemplo de una prueba de la funcion suma_vectores la cual nos dice el resultado de la suma entre los vectores complejos a y b el cual es igual a [[2, 6], [4, 8]],  de forma analoga sera para las demas funciones:
```
#Numeros Complejos
a = [ 1,3 ]
b = [ 2,4 ]

def testsumaVect(self):
   self.assertEqual(suma_vectoresr2([a, b], [a, b]), [[2, 6], [4, 8]])
```
* ## Ejecutar Pruebas 
Primero tienes que descargar el reporsitorio:
```
https://github.com/Camilomora10/Cuantico.git
```
Ahora Importa las librerias que deseas usar.

ejemplo:
```
from sistema_clasico_cuantico import canicas_clicks, probabilistico_clicks, cuantico_clicks
```

 * ## Clonar
Tambien puedes apropiarte de las librerias que usamos clonandolas, para realizar esto dirigete a la opcion ¨Codigo¨ en el inicio de el repositorio, Allí tendras 2 opciones:
 1. Descarga los archivos en formato zip, descomprimelos y usa las librerias en tu consola, estas se caracterizan por terminar en .py.
 2. Para poder clonar el repositorio sin necesidad de descargarlo, debes tener instalado la aplicacion [Git hup](https://desktop.github.com/)(Click para descargar). Una vez instalada la aplicacion crea una cuenta, Ahora dirigete a la opcion ¨Codigo¨ en el inicio de el repositorio y selecciona "Abrir con GitHup Deskop" y automaticamente la aplicacion clonara el repositorio en tu cuenta.
 3. Tambien podras compartir la libreria usando el comando git clone el cual se enceuntra en la opcion la opcion ¨Codigo¨ en el inicio de el repositorio, Alli encontraras el link:
 ```
https://github.com/Camilomora10/Cuantico.git
```

* ## Ejecutar Pruebas Unittest
1. Descarga Nuestro Repositorio con alguna de las formas que te mostramos antes.
2. Mira el siguiente tutorial [unittest-Marco de prueba automatizado](https://rico-schmidt.name/pymotw-3/unittest/)(click para ver).
Recuerda que las pruebas se encuentran en formato .py en la pagina principal del repositorio, en las siguientes direcciones:
* [Unittest Numeros Complejos](https://github.com/Camilomora10/Tencologia-CNYT1/blob/master/test_complejo.py).(click para ver)
* [Unittest Matrices y Vectores](https://github.com/Camilomora10/Tencologia-CNYT1/blob/master/test_matrices.py).(click para ver)
* [Unittest Sistemas Clasicos y Caunticos](https://github.com/Camilomora10/Tencologia-CNYT1/blob/master/test_cuantico.py).(click para ver)


## Built With

* [GipHup](https://desktop.github.com/) - Plataforma utilizada para crear el proyecto.
* [Pycharm Commiunity](https://www.jetbrains.com/es-es/pycharm/download/#section=windows) - Consola utilizada para crear funciones.
* [phyton 3.8](https://www.python.org/downloads/) - lenguaje de programacion usado.

## Versiones
* Version 1 Numeros Complejos.
* Version 2 Matrices y Vectores Complejos
* Version 3 Sistemas cuanticos 
* Version 4 Doble rendija. (Actual)

## Licencia
[Licencia](https://github.com/Camilomora10/Cuantico/blob/master/License).(click para ver)
## Authors

* **Yesid Camilo Mora Barbosa** - Todas las librerias.

