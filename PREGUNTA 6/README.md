# Detalle del Ejercicio

[Enunciado del problema]()

# Algoritmos de preprocesamiento en Python



## 1. Algoritmo LabelEncoder

EXPLICACIÓN:
Este algoritmo se esta usango porque justo en el dataset se tiene columnas que son de tipo string,
y al hacer operaciones sobre esas columnas se  necesita que sean de tipo number, y LabelEncoder()
codificar las cadenas -> es como si a cada cadenas de la un hash (un numero) y reemplaza todas las cadenas con ese mismo nuevo numero
para el dataset en la columna "Country" nos sirve de mucho ya que  podemos poener a entrenarlo utilizando dicha columna

![Código]()

DataSet antes de aplicar el algoritmo

![Solucion]()

Dataset despues de aplicar el algoritmo

![Solucion]()


## 2. Algoritmo StandarScaler

EXPLICACION DEL ALGORITMO
se usara este algoritmo para que todas las caracteristicas del data set, tengan la misma escala, esto es para  mejorar la presicion del modelo
en realcion al entrenamiento

![Código]()

DataSet antes de aplicar el algoritmo

[Solucion]()

Dataset despues de aplicar el algoritmo

[Solucion]()


## 3. Algoritmo SimpleInputer

EXPLICACION DEL ALGORITMO
se usara este algoritmo para para rellenar los espacios vacios en el dataset
una opcion es borrar las columnas con datos faltantes, pero eso afectaria al preprocesamiento de los datos
para este caso se va a rrellenar utilizando la media
ej: si en la COLUMNA de ranking hay datos faltantes se puede rellenar con la media, asi suponiendo que los usuarios sin datos, tiene  un ranking de la media del resto


![Código]()

DataSet antes de aplicar el algoritmo

[Solucion]()

Dataset despues de aplicar el algoritmo

[Solucion]()
