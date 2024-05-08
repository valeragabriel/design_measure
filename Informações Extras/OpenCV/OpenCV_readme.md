## OpenCV 
 O OpenCV https://opencv.org possui uma série de vantagens e características distintivas que a destacam como a solução ideal para o desenvolvimento de aplicações fundamentadas em técnicas de visão computacional, uma delas é sua natureza de código aberto. Essa característica oferece aos desenvolvedores acesso ao código-fonte, permitindo modificações e personalizações de acordo com as necessidades específicas do projeto.

Outro ponto relevante é a compatibilidade multiplataforma da OpenCV. Com suporte para uma ampla gama de sistemas operacionais, incluindo Windows, Linux, macOS, Android e iOS, os desenvolvedores têm a flexibilidade de criar aplicativos de visão computacional que funcionam em diversos dispositivos, garantindo a escalabilidade e a acessibilidade do algoritmo desenvolvido. 

Também, há uma integração facilitada do OpenCV com outras bibliotecas e frameworks populares, como NumPy, SciPy, TensorFlow e MediaPipe, e isso amplia ainda mais suas capacidades, possibilitando o desenvolvimento de soluções poderosas e flexíveis.

Tutorial guia: 
1. Instalação:
Certifique-se de ter o Python instalado em seu sistema. Em seguida, instale a OpenCV usando o pip:
    ```
    pip install opencv-python
    ```
2. Importação: 
    ```
    import cv2
    ```
Utilidades: 
Após ter sido feito a Instalação e Importação da OpenCV podemos utilizar alguns rescursos dela e aqui está alguns exemplos:
- **Carregar e exibir Imagem:**
    ```
    # Carregar uma imagem
    image = cv2.imread('caminho/para/sua/imagem.jpg')

    # Exibir a imagem em uma janela
    cv2.imshow('Imagem', image)

    # Esperar por uma tecla e fechar a janela
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ```
- **Carregar e exivir Vídeo:**
    ```
    # Cria um objeto VideoCapture para capturar vídeo da webcam padrão
    # Caso queira trocar para um vídeo já disponível em seu computador basta trocar o 0 pelo caminho do seu vídeo 
    cap = cv2.VideoCapture(0)

    # Loop para ler e exibir o vídeo quadro a quadro
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Video', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'): # Pressione 'q' para sair
                break
        else:
            break

    # Liberar o objeto VideoCapture e fechar as janelas
    cap.release()
    cv2.destroyAllWindows()
    ```
- **Processamento de Imagens:**
    ```  
    # Converter a imagem para tons de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar desfoque gaussiano para reduzir o ruído
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Detectar as bordas na imagem usando o operador Canny
    edges = cv2.Canny(blurred_image, threshold1=30, threshold2=100)

    # Exibir a imagem das bordas detectadas
    cv2.imshow('Bordas', edges)
    ```
- **Detecção de Objetos:**
    ```  
    # Carregar o classificador de detecção de objetos pré-treinado
    object_cascade = cv2.CascadeClassifier('caminho/para/seu/classificador.xml')

    # Detectar objetos na imagem
    objects = object_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5)

    # Desenhar retângulos ao redor dos objetos detectados
    for (x, y, w, h) in objects:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Exibir a imagem com os objetos detectados
    cv2.imshow('Detecção de Objetos', image)
    ```

## Funcionamento em prática
Deixarei um código exemplo de detecção de rosto, FaceDetection.py 
