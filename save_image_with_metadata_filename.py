import os
import torch
import numpy as np
import piexif
from PIL import Image
from datetime import datetime
import folder_paths

class SaveImageWithMetadata:
    def __init__(self):
        self.type = "output"
        
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "decoded_image": ("IMAGE",),
                "prompt_text": ("STRING",),  
                "noise": ("NOISE",),
            },
            "optional": {
                "prefix": ("STRING", {"default": ""}),
                "software_name": ("STRING", {"default": "ComfyUI"}),
            }
        }
    
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    OUTPUT_NODE = True
    FUNCTION = "save_images"
    CATEGORY = "S0N3Y"

    def save_images(self, decoded_image, prompt_text, noise, prefix="", software_name="ComfyUI"):
        output_dir = folder_paths.get_output_directory()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results = []
        batch_size = decoded_image.shape[0]
        
        print(f"Starting to process batch of {batch_size} images")

        for i in range(batch_size):
            try:
                image = Image.fromarray(np.clip(255. * decoded_image[i].cpu().numpy(), 0, 255).astype(np.uint8))
                
                current_seed = noise.seeds[i] if hasattr(noise, 'seeds') else getattr(noise, 'seed', f"unknown_{i}")
                
                filename = f"{prefix}_{timestamp}_{i}_seed-{current_seed}.jpg" if prefix else f"{timestamp}_{i}_seed{current_seed}.jpg"
                filepath = os.path.join(output_dir, filename)

                if image.mode != 'RGB':
                    image = image.convert('RGB')

                exif_dict = {
                    "0th": {
                        piexif.ImageIFD.ImageDescription: f"{prompt_text} - Seed: {current_seed}".encode("utf-8"),
                        piexif.ImageIFD.Software: software_name.encode("utf-8"),
                        piexif.ImageIFD.DateTime: datetime.now().strftime("%Y:%m:%d %H:%M:%S").encode("utf-8"),
                    }
                }
                exif_bytes = piexif.dump(exif_dict)
                
                image.save(filepath, "jpeg", quality=100, exif=exif_bytes)
                results.append(filepath)
                
                print(f"Saved image {i+1} with seed: {current_seed}")
                
            except Exception as e:
                print(f"Error saving image {i}: {str(e)}")
                continue
        
        print(f"Completed saving {len(results)} images")
        return (decoded_image, {"ui": {"images": results}})

NODE_CLASS_MAPPINGS = {
    "Save Image with Metadata": SaveImageWithMetadata
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Save Image with Metadata": "Save Image With Metadata"
}