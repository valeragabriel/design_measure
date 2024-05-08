import cv2

# Carregar a imagem
image = cv2.imread('Socrates_face.jpg')

# Carregar o classificador de detecção de rostos pré-treinado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Converter a imagem para tons de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar rostos na imagem
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Desenhar retângulos ao redor dos rostos detectados
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Exibir a imagem com os rostos detectados
cv2.imshow('Deteccao de Rostos', image)

# Esperar por uma tecla e fechar a janela
cv2.waitKey(0)
cv2.destroyAllWindows()