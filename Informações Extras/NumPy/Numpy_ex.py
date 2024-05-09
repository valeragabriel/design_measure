import numpy as np 

# Criando um array a partir de uma lista Python
arr1 = np.array([1, 2, 3, 4, 5])

# Criando um array de zeros com shape (2, 3)
arr2 = np.zeros((2, 3))

# Criando um array de uns com shape (3, 2)
arr3 = np.ones((3, 2))

# Criando um array de números aleatórios com shape (2, 2)
arr4 = np.random.random((2, 2))

# Adição
result_add = arr1 + arr1

# Subtração
result_sub = arr1 - arr1

# Multiplicação
result_mul = arr1 * arr1

# Divisão
result_div = arr1 / arr1

# Acessando o primeiro elemento de arr1
first_element = arr1[0]

# Fatiando arr1 para obter os primeiros três elementos
subset = arr1[:3]

# Função de exponenciação
exponentials = np.exp(arr1)

# Função seno
sin_values = np.sin(arr1)

# Multiplicação de matriz
mat_mul = np.dot(arr2, arr3)

# Transposição de matriz
mat_transpose = np.transpose(arr4)