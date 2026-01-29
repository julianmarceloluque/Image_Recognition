# 📷 OpenCV Basics with Python

Este repositorio contiene ejemplos prácticos del uso de OpenCV con Python para trabajar con imágenes, dibujos y video en tiempo real. Cada archivo aborda funcionalidades específicas que permiten familiarizarse con la biblioteca OpenCV de forma progresiva.

## 🧰 Requisitos

Asegurate de tener instaladas las siguientes dependencias:

```bash
pip install opencv-python numpy
```

---

## 📁 Archivos incluidos

### ✅ `read.py` — Captura de video desde la cámara

Este script utiliza la cámara web por defecto (`cv.VideoCapture(0)`) para mostrar un video en tiempo real. Es ideal para probar si OpenCV detecta correctamente tu cámara.

**Características:**

- Accede a la cámara integrada o conectada
- Muestra el video en vivo en una ventana
- Finaliza al presionar la tecla `q`

**Uso:**

```bash
python read.py
```

---

### 🔧 `rescale.py` — Redimensionamiento de imágenes y video

Este script incluye funciones útiles para trabajar con el tamaño de imágenes y frames de video. Ideal para adaptar la resolución a las necesidades del sistema o mejorar el rendimiento.

**Funciones:**

- `rescaleFrame(frame, scale=0.75)`: Redimensiona un frame (imagen o video)
- `changeRes(width, height)`: Cambia la resolución del video en vivo

**Flujo del script:**

1. Carga y muestra una imagen (`Resources/Photos/cat.jpg`)
2. Muestra la misma imagen redimensionada
3. Inicia la cámara web y muestra el video en tiempo real

**Uso:**

```bash
python rescale.py
```

> 📌 Asegurate de tener la imagen `cat.jpg` en la ruta `Resources/Photos/`.

---

### ✏️ `draw.py` — Dibujo de formas y texto en una imagen

Este script demuestra cómo crear una imagen en blanco (`np.zeros`) y superponerle figuras geométricas y texto usando OpenCV.

**Funciones demostradas:**

- Pintar regiones específicas de una imagen
- Dibujar rectángulos, líneas y círculos
- Escribir texto sobre la imagen con distintas fuentes

**Ejemplos incluidos:**

- Coloreado por regiones
- Rectángulos con grosor o relleno completo
- Círculos y líneas con coordenadas personalizadas
- Texto centrado o libre

**Uso:**

```bash
python draw.py
```

<!-- ---

## 🎯 Objetivo

Este repositorio está pensado para quienes están dando sus primeros pasos en **visión por computadora** con Python y OpenCV. Cada script es una pieza clave para construir proyectos más complejos en el futuro, como reconocimiento de objetos, segmentación o procesamiento de video.

---

## 🙌 Contribuciones

¿Querés mejorar estos ejemplos, agregar otros nuevos o dejar feedback? ¡Estás más que bienvenido! Podés hacer un fork y enviar un pull request.

---

## 📬 Contacto

Si tenés dudas o sugerencias, no dudes en abrir un issue en el repositorio o escribirme por mensaje directo.

--- -->
