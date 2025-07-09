import cv2 as cv

# img = cv.imread('Resources/Photos/lady.jpg')
# cv.imshow('Lady',img)

haar_cascade = cv.CascadeClassifier('./haar_face.xml')

capture = cv.VideoCapture(0)

# Verificá si la cámara se abrió correctamente
if not capture.isOpened():
    print("No se pudo abrir la cámara")
    exit()

vuelta = False

# Bucle para capturar frame por frame
while True:
    ret, frame = capture.read()  # Leer un frame
    if not ret:
        print("No se pudo recibir el frame. Saliendo...")
        break
    frame = cv.flip(frame, 1)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    for i, (x, y, w, h) in enumerate (faces_rect):
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
        cv.putText(frame, f'Face {i+1}',(x+w, y+h), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0), thickness=2)
    print(f'Number of faces found = {len(faces_rect)}')
    cv.imshow('Camera', frame)  # Mostrar el frame

    if cv.waitKey(1) & 0xFF == ord('q'):  # Salir con la tecla 'q'
        break


capture.release()
cv.destroyAllWindows()