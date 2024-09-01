import cv2
import os

# Caminho para o vídeo MP4
video_path = 'video.mp4'

# Diretório para salvar as imagens
output_dir = 'D:\\netflix'
os.makedirs(output_dir, exist_ok=True)

# Abrir o vídeo
cap = cv2.VideoCapture(video_path)

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Salvar o frame como imagem
    frame_filename = os.path.join(output_dir, f'frame_{frame_count}.jpg')
    cv2.imwrite(frame_filename, frame)
    
    print(f'Salvando {frame_filename}')
    frame_count += 1

# Liberar o vídeo
cap.release()
cv2.destroyAllWindows()
