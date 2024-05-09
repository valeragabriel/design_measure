import cv2
import numpy as np

# Função para calcular a distância euclidiana entre dois pontos
def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Carregando a imagem em cores
image = cv2.imread('MrOlympia.jpeg')

# Obtendo as dimensões da imagem
height, width, _ = image.shape

# Calculando o centro superior e inferior da imagem
center_top = (int(width / 2), int(height / 4))
center_bottom = (int(width / 2), int(3 * height / 4))

# Calculando a distância euclidiana entre os pontos
distance = euclidean_distance(center_top, center_bottom)

print("A distancia euclidiana entre os pontos {} e {} é: {:.2f}".format(center_top, center_bottom, distance))

# Desenhando uma linha entre os pontos na imagem
cv2.line(image, center_top, center_bottom, (0, 255, 0), 2)

# Exibindo a imagem com a linha desenhada mostrando a dinstância euclidiana
cv2.imshow('Image with Line', image)

# Aguardando até que uma tecla seja pressionada para fechar a janela
cv2.waitKey(0)
cv2.destroyAllWindows()
