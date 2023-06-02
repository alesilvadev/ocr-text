# Usamos una imagen base con Python 3.8
FROM python:3.8-slim-buster

# Directorio de trabajo en el contenedor
WORKDIR /source

# Agregamos los archivos necesarios
ADD . /app

# Instalamos las dependencias
RUN pip install --upgrade pip
RUN pip install flask easyocr Pillow numpy gunicorn

# Exponemos el puerto 8080
EXPOSE 8080

# Ejecutamos la aplicación
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 application:app