import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Não foi possível acessar a câmera")
    exit()

filtermode = 0

while True:
    success, frame = camera.read()

    if not success:
        print("Erro ao capturar imagem")
        break

    if filtermode == 1:
        processed_frame = cv2.GaussianBlur(frame, (55, 55), 0)


    elif filtermode == 2:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        processed_frame = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

    elif filtermode == 3:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        processed_frame = cv2.Canny(gray, 50, 200)

    else:
        processed_frame = frame
    cv2.imshow("Minha Camera", processed_frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    elif key == ord('f'):
        filtermode = 1

    elif key == ord('g'):
        filtermode = 2


    elif key == ord('n'):
        filtermode = 0

    elif key == ord('c'):
        filtermode = 3

camera.release()
cv2.destroyAllWindows()