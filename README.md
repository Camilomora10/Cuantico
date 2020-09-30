# Experimento de la doble Rendija

El experimento de la doble rendija se hizo con la intención de determinar si la luz se comportaba como onda o como partícula. En este repositorio intentaremos estudiar y entender el comportamiento del universo cuántico entendiendo sus fundamentos mas básicos, y realizaremos un experimento para poder demostrarlo.

* ## Inicios

El experimento de la doble rendija fue planteado originalmente en 1801 por Thomas Young y lo hizo con la intención de determinar si la luz se comportaba como onda o como partícula, actualmente este experimento se repoduce en una cámara oscura la cual deja entrar un haz de luz por una rendija estrecha, cuando la luz llega a una pared intermedia de dos rendijas, la luz debe pasar por alguna de estas dos y chocar con una placa que se encuentra después de la rendija.
En la siguiente imagen se pude observar cómo es el comportamiento de las partículas en el experimento.

![image](https://github.com/Camilomora10/Cuantico/blob/master/rendija.jpg)

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

* ## Explicacion

Para poder lograr entender el resultado del experimento en la época aplicaron el principio de superposición cuántico en el que dice que las partículas (en este caso la luz) puede dos o más valores de una determinada magnitud (su posición ) tambien conocida como "onda de posibilidades" que pasan por las dos ranuras para luego interferir con ella misma hasta que golpear la pared de impacto y que al ser monitoreado este se ve afectado a que se dice que este principio colapsa y solo lograremos observar una de todos los posibles resultados.

* ## Simulacion del Experimento

Para las simulaciones utilizamos un modelo matemático basado en los grafos del sistema y las matrices adyacencia propias de los mismos, posteriormente realizamos una simulación en la librería_sistema_cuantico en python que se encuentra en el repositorio de la siguiente direccion:
```
https://github.com/Camilomora10/Tencologia-CNYT1
```
También tendremos en cuenta la forma en el que el experimento se representara, entonces el sistema tendra una matriz asociada y a su vez un vector de estado inicial.
A continuacio el Grafo del experimento:

![image](https://github.com/Camilomora10/Cuantico/blob/master/.idea/grafo.png)

A continuacio la matriz del experimento:

![image](https://github.com/Camilomora10/Cuantico/blob/master/.idea/matriz.png)

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

## Versiones

* Version 1 Doble rendija. (Actual)

## Licencia
[Licencia](https://github.com/Camilomora10/Cuantico/blob/master/License).(click para ver)
## Authors

* **Yesid Camilo Mora Barbosa** - Todas las librerias.

