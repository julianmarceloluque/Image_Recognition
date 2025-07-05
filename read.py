import cv2 as cv

# # Reading Images
# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('Cat',img)
# cv.waitKey(0)


# # Reading Video
# capture = cv.VideoCapture(0)
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

# Crear un objeto VideoCapture con el índice 0 (cámara por defecto)
capture = cv.VideoCapture(0)

# Verificá si la cámara se abrió correctamente
if not capture.isOpened():
    print("No se pudo abrir la cámara")
    exit()

# Bucle para capturar frame por frame
while True:
    ret, frame = capture.read()  # Leer un frame
    if not ret:
        print("No se pudo recibir el frame. Saliendo...")
        break

    cv.imshow('Cámara', frame)  # Mostrar el frame

    if cv.waitKey(1) & 0xFF == ord('q'):  # Salir con la tecla 'q'
        break

# Liberar la cámara y cerrar ventanas
capture.release()
cv.destroyAllWindows()