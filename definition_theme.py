import json
from typing import Tuple

class ThemeDefinitionNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "variable_id": ("STRING", {
                    "label": "Variable ID",
                    "placeholder": "Enter variable name (e.g. skirt, hairstyle)"
                }),
                "options": ("STRING", {
                    "multiline": True,
                    "label": "Options",
                    "placeholder": "Enter options, one per line\nExample:\nskater\nmaxi\nmidi\nmini",
                    "lines": 10
                })
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("definitions",)
    FUNCTION = "generate_definition"
    CATEGORY = "S0N3Y"
    
    def generate_definition(self, options: str, variable_id: str) -> Tuple[str]:
        option_list = [opt.strip() for opt in options.strip().split('\n') if opt.strip()]
        
        definitions = {f"[{variable_id}]": option_list}
        
        return (json.dumps(definitions),)


NODE_CLASS_MAPPINGS = {
    "Theme Definition": ThemeDefinitionNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Theme Definition": "Theme Definition"
}