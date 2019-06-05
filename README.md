# Identificación de productos para el Laboratorio de Almacenamiento de la universidad EAFIT

## Descripción
Herramienta de reconocimiento de imágenes para identificar productos del Laboratorio de Almacenamiento de la Universidad EAFIT, que tienen la particularidad de ser muy similares entre sí y dado su tamaño no es posible colocarles códigos de barras.

![prods_ex_2](/images/prods_ex_2.PNG?raw=true "prods_ex_2")

## Arquitectura de la red
La arquitectura usada toma como base *Inception v3* eliminando las capas superiores e inicializando sus pesos con los de ImageNet. A esta red se conecta una capa densa de 100 neuronas y sobre esta una capa Softmax de 60 salidas. 

![architecture](/images/arch.png?raw=true "architecture")

## Arquitectura del código
El código está dividido en los módulos: Data processing, Preprocessing, Training y Postprocessing. 

### Data processing
En este módulo se encuentran los scripts `preprocess` y `split_data`. `preprocess` escala las imágenes a resolución 299x299px y `split_data` divide el dataset  en los directorios `train`, `dev` y `set`.

### Preprocessing
En preprocessing se encuentra el código de los generadores usados para entrenar el modelo. En el generador de training se aplican las siguientes estrategias de *Data augmentation*:

* Rotation
* Shift
* Shear
* Zoom
* Horizontal and vertical flips

### Training
En este módulo se encuentra la definición del modelo y el ciclo de entrenamiento, que se realiza por 100 épocas con un *Learning Rate Decay* de 0.8 cada 5 iteraciones sin mejora.

### Postprocessing
Usado para procesar el vector obtenido de la capa softmax y obtener la clase predicha y una imagen de la misma.

## Integrantes
* Juan José Suarez Estrada - jsuare32@eafit.edu.co
* Juan Manuel Ciro Restrepo - jcirore@eafit.edu.co
