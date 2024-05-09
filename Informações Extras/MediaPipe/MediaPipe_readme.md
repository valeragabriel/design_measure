## MediaPipe 

A MediaPipe é uma biblioteca de código aberto altamente eficiente desenvolvida pelo Google(https://developers.google.com/mediapipe). Ela oferece uma série de componentes pré-construídos para diversas tarefas de processamento de imagem e vídeo permitindo aos desenvolvedores criar aplicações envolvendo detecção de objetos, reconhecimento facial, rastreamento de mãos, estimativa de pose, entre outras funcionalidades de visão computacional e aprendizado de máquina.

No escopo deste trabalho, focaremos especificamente na MediaPipe Pose Detection (https://developers.google.com/mediapipe/solutions/vision/pose_landmarker), uma solução oferecida pela MediaPipe para a detecção de pose corporal. Esta biblioteca é baseada em redes neurais convolucionais (CNNs) e é projetada para extrair landmarks específicos do corpo humano e traçar seu esqueleto. Ela oferece 33 landmarks que podem ser utilizados para uma variedade de aplicações. A escolha desta biblioteca se deu principalmente pela quantidade de landmarks oferecidos e pela eficiência com que é capaz de
estimar a pose humana em imagens.

Uma vez que a pose é extraída usando a MediaPipe Pose Detection, podemos obter os resultados das posições dos landmarks. Esses landmarks fornecem referências úteis, como a posição do braço direito, que podem ser utilizadas para uma variedade de operações. Por exemplo, é possível calcular o ângulo do braço conforme o cotovelo se rotaciona, ou analisar se o braço está levantado ou abaixado. Essas informações podem ser fundamentais em aplicações que envolvem análise de movimento corporal ou interação humano-computador.

## Tutorial guia: 
1. Instalação:
Certifique-se de ter o Python instalado em seu sistema. Em seguida, instale a MediaPipe usando o pip:
    ```
    pip install mediapipe
    ```
2. Importação: 
    ```
    import mediapipe as mp 
    ```
## MediaPipe Pose detection:
Deixei um codigo disponível com nome de PoseDetection.py mostrando o passo a passo de como utilizar o MediaPipe Pose Detection em uma imagem 