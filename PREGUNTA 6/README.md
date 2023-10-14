# Detalle del Ejercicio

[Enunciado del problema](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-PRIMER-PARCIAL/blob/master/PREGUNTA%206/Enunciado.txt)

# Algoritmos de preprocesamiento en Python



## 1. Algoritmo LabelEncoder

EXPLICACIÓN:
Este algoritmo se esta usango porque justo en el dataset se tiene columnas que son de tipo string,
y al hacer operaciones sobre esas columnas se  necesita que sean de tipo number, y LabelEncoder()
codificar las cadenas -> es como si a cada cadenas de la un hash (un numero) y reemplaza todas las cadenas con ese mismo nuevo numero
para el dataset en la columna "Country" nos sirve de mucho ya que  podemos poener a entrenarlo utilizando dicha columna

[Código](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-PRIMER-PARCIAL/blob/master/PREGUNTA%206/algoritmo1.py)

DataSet antes de aplicar el algoritmo

![Solucion](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-PRIMER-PARCIAL/blob/master/PREGUNTA%206/algoritmo1_inicio.jpeg)

Dataset despues de aplicar el algoritmo

![Solucion](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-PRIMER-PARCIAL/blob/master/PREGUNTA%206/algoritmo1_fin.jpeg)


## 2. Algoritmo StandarScaler

EXPLICACION DEL ALGORITMO
se usara este algoritmo para que todas las caracteristicas del data set, tengan la misma escala, esto es para  mejorar la presicion del modelo
en realcion al entrenamiento

[Código](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-PRIMER-PARCIAL/blob/master/PREGUNTA%206/algoritmo2.py)

DataSet antes de aplicar el algoritmo

![Solucion](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-PRIMER-PARCIAL/blob/master/PREGUNTA%206/algoritmo2_inicio.jpeg)

Dataset despues de aplicar el algoritmo

![Solucion](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-PRIMER-PARCIAL/blob/master/PREGUNTA%206/algoritmo2_fin.jpeg)


## 3. Algoritmo SimpleInputer

EXPLICACION DEL ALGORITMO
se usara este algoritmo para para rellenar los espacios vacios en el dataset
una opcion es borrar las columnas con datos faltantes, pero eso afectaria al preprocesamiento de los datos
para este caso se va a rrellenar utilizando la media
ej: si en la COLUMNA de ranking hay datos faltantes se puede rellenar con la media, asi suponiendo que los usuarios sin datos, tiene  un ranking de la media del resto


[Código](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-PRIMER-PARCIAL/blob/master/PREGUNTA%206/algoritmo3.py)

DataSet antes de aplicar el algoritmo

![Solucion](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-PRIMER-PARCIAL/blob/master/PREGUNTA%206/algoritmo3_inicio.jpeg)

Dataset despues de aplicar el algoritmo

![Solucion](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-PRIMER-PARCIAL/blob/master/PREGUNTA%206/algoritmo3_fin.jpeg)
