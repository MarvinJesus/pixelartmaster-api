# Imagen base con PyTorch + CUDA
FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

# Crear carpeta de trabajo
WORKDIR /app

# Copiar archivos del repo
COPY . .

# Actualizar pip y setuptools
RUN pip install --upgrade pip setuptools

# Instalar dependencias
RUN pip install -r requirements.txt

# Ejecutar el handler de RunPod
CMD ["python", "handler.py"]
