# Reto MNIST
## Descripcion
El [MNIST](http://yann.lecun.com/exdb/mnist/) es un conjunto de imágenes de digitos del 0 al 9 escritos a mano.

![alt text][s1]

Este dataset tiene mas de 60,000 imágenes separadas en 10 clases. El reto es construir un clasificador de imágenes que sea capaz de reconocer los digitos.


### Solucion


##### Requerimientos
* Python 2.7 con paquetes especificados en `requirements.txt`

```
pip install -r requirements.txt
```

##### Procedimiento
Corre el siguiente codigo en consola
```
python knn.py
```

##### Metodo
Usado el metodo "k nearest neighbours" con parametros "n_neighbors=2, algorithm='brute', leaf_size=7". El algoritmo 'brute' hizo metodo muy rapido. 'leaf_size' no hay efecto en la velocidad de algoritmo. 'n_neighbors' no poder ser muy grande. Si no, la exactitud ser no bueno.

##### Resultados
0.9628



[s1]: http://rodrigob.github.io/are_we_there_yet/build/images/mnist.png?1363085077 "S"
