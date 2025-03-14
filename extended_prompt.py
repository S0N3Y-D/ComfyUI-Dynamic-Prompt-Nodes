import torch
import random
import json
from typing import Dict, List, Tuple

class ExtendedPromptNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "clip": ("CLIP",),
                "theme_definitions": ("STRING",),
                "template": ("STRING", {
                    "multiline": True,
                    "label": "Template",
                    "placeholder": "Enter your template using [theme] placeholders\nExample: A woman with [hair-color] hair wearing a [dress-type] in [location]",
                    "lines": 20
                }),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})
            },
            "optional": {
                "age_definitions": ("STRING", {"default": None}),
                "definitions_aio": ("STRING", {"default": None}),
                "control_prompt": ("STRING", {"default": None})
            }
        }
    
    RETURN_TYPES = ("CONDITIONING", "STRING",)
    RETURN_NAMES = ("conditioning", "prompt_text",)
    FUNCTION = "generate"
    CATEGORY = "S0N3Y"

    def generate_prompt(self, template: str, theme_definitions_json: str, age_definitions_json: str, definitions_aio_json: str, rng: random.Random) -> str:
        try:
            theme_definitions = json.loads(theme_definitions_json)
            
            if age_definitions_json is not None:
                try:
                    age_definitions = json.loads(age_definitions_json)
                    theme_definitions.update(age_definitions)
                except json.JSONDecodeError:
                    print("Warning: Invalid age definitions JSON received")
            
            if definitions_aio_json is not None:
                try:
                    definitions_aio = json.loads(definitions_aio_json)
                    theme_definitions.update(definitions_aio)
                except json.JSONDecodeError:
                    print("Warning: Invalid definitions AIO JSON received")
            
        except json.JSONDecodeError:
            print("Warning: Invalid theme definitions JSON received")
            return template
            
        result = template
        
        for key, options in theme_definitions.items():
            if key in result and options:
                selected = rng.choice(options)
                result = result.replace(key, selected)
                
        return result

    def generate(self, clip, theme_definitions: str, template: str, seed: int, age_definitions: str = None, definitions_aio: str = None, control_prompt: str = None) -> Tuple[List[Tuple[torch.Tensor, dict]], str]:
        rng = random.Random(seed)
        
        actual_template = control_prompt if control_prompt is not None else template
        
        prompt = self.generate_prompt(actual_template, theme_definitions, age_definitions, definitions_aio, rng)
        
        tokens = clip.tokenize(prompt)
        cond, pooled = clip.encode_from_tokens(tokens, return_pooled=True)
        
        conditioning = [(cond, {"pooled_output": pooled})]
        
        return (conditioning, prompt)

NODE_CLASS_MAPPINGS = {
    "Extended Prompt": ExtendedPromptNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Extended Prompt": "Extended Prompt"
}
