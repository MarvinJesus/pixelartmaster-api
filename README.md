# PixelArtMaster Serverless API

Este repositorio implementa un endpoint serverless en RunPod que genera imágenes estilo pixel art a partir de texto utilizando un modelo LoRA personalizado.

## 🚀 ¿Qué hace?

- Usa `StableDiffusionPipeline` con LoRA desde Hugging Face.
- Responde a solicitudes POST con un prompt de texto.
- Devuelve la imagen generada codificada en base64.

## 📦 Requisitos

- RunPod Serverless
- GPU (modo serverless con A10 o superior recomendado)

## 📂 Estructura del repositorio

- `handler.py`: lógica principal del endpoint
- `requirements.txt`: dependencias
- `runpod.serverless`: configuración para RunPod

## 🛠️ Despliegue en RunPod

1. Selecciona `GitHub Repo` en RunPod
2. Conecta este repositorio
3. Asegúrate de usar la rama correcta (main o master)
4. Elige GPU y configura el endpoint

## 📫 Ejemplo de solicitud

```bash
curl -X POST https://TU_ENDPOINT.runpod.run \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Pixel art character of a cyber ninja"}'
