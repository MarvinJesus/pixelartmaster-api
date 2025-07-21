import runpod
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import numpy as np
import base64
from io import BytesIO

# === CONFIGURACIÓN ===
BASE_MODEL = "runwayml/stable-diffusion-v1-5"
LORA_REPO = "marvin90/pixelartmaster-lite-faces"

# Detectar dispositivo
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if device == "cuda" else torch.float32

# Cargar modelo y LoRA solo una vez
pipe = StableDiffusionPipeline.from_pretrained(BASE_MODEL, torch_dtype=dtype).to(device)
pipe.load_lora_weights(LORA_REPO)

# Función para convertir imagen a base64
def image_to_base64(image: Image.Image) -> str:
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

# Función principal que será llamada por RunPod
def generate_pixelart(job):
    prompt = job["input"].get("prompt", "")
    if not prompt:
        return {"error": "Missing prompt"}

    image = pipe(prompt).images[0]
    image_base64 = image_to_base64(image)

    return {"image_base64": image_base64}

# Asociar handler con RunPod
runpod.serverless.start({"handler": generate_pixelart})
