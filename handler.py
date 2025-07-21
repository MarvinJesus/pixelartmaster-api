import runpod
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
from io import BytesIO
import base64
import os

# Ruta del modelo base (puede ser remoto o precargado localmente)
BASE_MODEL = "runwayml/stable-diffusion-v1-5"  # o ruta local si lo tienes en disco
LORA_PATH = "/workspace/output/pixelartmastermodel-lite.safetensors"

device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if device == "cuda" else torch.float32

# Cargar modelo base
pipe = StableDiffusionPipeline.from_pretrained(BASE_MODEL, torch_dtype=dtype).to(device)

# Cargar pesos LoRA desde archivo local
pipe.load_lora_weights(LORA_PATH)

# Convertir imagen a base64
def image_to_base64(img: Image.Image) -> str:
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

# Función principal que RunPod ejecutará
def generate_pixelart(job):
    prompt = job["input"].get("prompt")
    if not prompt:
        return {"error": "Falta el prompt"}

    image = pipe(prompt).images[0]
    base64_img = image_to_base64(image)
    return {"image_base64": base64_img}

# Iniciar servicio en RunPod
runpod.serverless.start({"handler": generate_pixelart})
