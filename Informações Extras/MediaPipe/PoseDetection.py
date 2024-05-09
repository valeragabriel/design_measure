import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2

def draw_landmarks_on_image(rgb_image, detection_result):
  pose_landmarks_list = detection_result.pose_landmarks
  annotated_image = np.copy(rgb_image)

  # Loop através da pose detectada para ser visualizado 
  for idx in range(len(pose_landmarks_list)):
    pose_landmarks = pose_landmarks_list[idx]

    # Desenhando pose landmarks.
    pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    pose_landmarks_proto.landmark.extend([
      landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
    ])
    solutions.drawing_utils.draw_landmarks(
      annotated_image,
      pose_landmarks_proto,
      solutions.pose.POSE_CONNECTIONS,
      solutions.drawing_styles.get_default_pose_landmarks_style())
  return annotated_image

model_path = "pose_landmarker_lite.task"

img_path =  "MrOlympia.jpeg"

# Imagem OpenCv
img = cv2.imread(img_path)

BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Criando o pose landmark detector 
options = vision.PoseLandmarkerOptions(
    base_options=python.BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.IMAGE,
    output_segmentation_masks=True)
detector = vision.PoseLandmarker.create_from_options(options)

# Image MediaPipe
mp_image = mp.Image.create_from_file(img_path)

with PoseLandmarker.create_from_options(options) as landmarker:
  # Inicializando landmark 
  pose_landmarker_result = landmarker.detect(mp_image)

  # Aplicando a função de desenho dos landmarks na imagem aberta pelo OpenCV
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
annotated_image = draw_landmarks_on_image(img_rgb, pose_landmarker_result)
cv2.imshow("Image with Landmarks", annotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Com a aplicacao de pose feita pela MediaPipe, com os resultados dos landmarks, podemos criar uma máscara de segmentação
segmentation_mask = pose_landmarker_result.segmentation_masks[0].numpy_view()
visualized_mask = np.repeat(segmentation_mask[:, :, np.newaxis], 3, axis=2) * 255
cv2.imshow("Segmantation img", visualized_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Resultados de posição dos landmarks na imagem, em coordenadas normalizadas (x, y, z)
pose_landmarker_result

# Caso queira acessar um landmark específico, basta acessar o índice do landmark desejado
nose_landmark = pose_landmarker_result.pose_landmarks[0][0]
nose_landmark