import pandas as pd
import numpy as np
import random
from sklearn.datasets import load_iris

iris = load_iris()
# Obtener datos y etiquetas
X = iris.data  # Datos
y = iris.target  # Etiquetas

# Convertir a matrices NumPy
X_np = np.array(X)
y_np = np.array(y)

# Unir datos y etiquetas en un solo conjunto de datos NumPy
# iris_datos = np.column_stack((X_np, y_np))
iris_datos = X_np
dataset = iris_datos
# print(dataset)
# dataset = datos.to_numpy()
titles = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'Ciclos de indices']
def mostrar(arr):
  print()
  for i in arr:
    print(i)
  print()


for _ in range(2):
  print("CICLO NUMERO" , _)
  nuevoDato = []
  # tam_muestra = 9272
  tam_muestra = 20;
  for i in range(tam_muestra):
    nuevo = []
    for j in range(len(dataset[i])):
      nuevo.append(dataset[i][j])
    nuevo.append(i)
    nuevoDato.append(nuevo)

  # volviendolo aleatorio
  random.shuffle(nuevoDato)

  print('despues del shuffle')
  mostrar(nuevoDato)

  train = int(tam_muestra * 0.8)
  array_train = nuevoDato[:train]
  array_test = nuevoDato[train:]

  print("tamaño del train ", len(array_train))
  # print(array_train)
  print("tamaño del test ", len(array_test))
  # print(array_test)
  
  # mostrar(array_train)
  # print("test")
  # mostrar(array_test)

  # generando por columnas cualquier columna

  print("\ngenerando por columna el train")
  # print(len(nuevoDato[0]), len(array_train[0]))
  columna = []
  for i in range(len(array_train[0])):
    col = []
    for j in range(len(array_train)):
      col.append(array_train[j][i])
    print(titles[i], col)
  print()


  print("\ngenerando por columan el test")
  # print(len(nuevoDato[0]), len(array_test[0]))
  columna = []
  for i in range(len(array_test[0])):
    col = []
    for j in range(len(array_test)):
      col.append(array_test[j][i])
    print(titles[i], col)
  print()
