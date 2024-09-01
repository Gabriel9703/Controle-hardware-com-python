import cv2
import os

# Parâmetros do script
video_source = 'video.mp4'  # Caminho do vídeo
output_dir = 'D:\\foto'
os.makedirs(output_dir, exist_ok=True)
min_area = 1500  # Tamanho mínimo da área para considerar como movimento
frame_skip = 5  # Pula frames para reduzir a frequência de captura

# Inicializa a captura de vídeo
cap = cv2.VideoCapture(video_source)

# Inicializa o primeiro frame
first_frame = None
frame_count = 0
skip_count = 0

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    skip_count += 1
    
    # Pula frames para reduzir a frequência de análise
    if skip_count % frame_skip != 0:
        continue

    # Converte o frame para escala de cinza e aplica um desfoque
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Define o primeiro frame como base de comparação ou atualiza periodicamente
    if first_frame is None or skip_count % (frame_skip * 10) == 0:
        first_frame = gray
        continue

    # Calcula a diferença absoluta entre o frame atual e o primeiro frame
    frame_delta = cv2.absdiff(first_frame, gray)
    thresh = cv2.threshold(frame_delta, 30, 255, cv2.THRESH_BINARY)[1]

    # Dilata a imagem do limiar para preencher buracos
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Encontra os contornos na imagem binária
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False

    for contour in contours:
        # Ignora pequenas áreas que não representam movimento significativo
        if cv2.contourArea(contour) < min_area:
            continue

        # Define a área de movimento detectada
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (w + x, h + y), (0, 255, 0), 2)
        motion_detected = True

    # Salva o frame somente se movimento significativo for detectado
    if motion_detected:
        frame_filename = os.path.join(output_dir, f'motion_{frame_count}.jpg')
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
        print(f'Movimento detectado! Salvando {frame_filename}')

    # Exibe o frame resultante com as áreas de movimento detectadas
    cv2.imshow('Security Feed', frame)

    # Pressione 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Limpeza
cap.release()
cv2.destroyAllWindows()
