import json
from typing import Dict, List, Tuple

class DefinitionNodeAIO:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key_definitions": ("STRING", {
                    "multiline": True,
                    "label": "Key Definitions",
                    "placeholder": "Enter definitions in format: [key, value1, value2, ...]\nExample:\n[1, pants, skirt, shorts]\n[2, blonde, brown, black, red]"
                })
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("definitions",)
    FUNCTION = "process_definitions"
    CATEGORY = "S0N3Y"
    
    def parse_key_definitions(self, key_definitions: str) -> Dict[str, List[str]]:
        key_dict = {}
        
        for line in key_definitions.strip().split('\n'):
            if not line.strip():
                continue
                
            try:
                parts = line.strip()[1:-1].split(',')
                if len(parts) < 2:
                    continue
                    
                key = parts[0].strip()
                options = [opt.strip() for opt in parts[1:]]
                key_dict[f'[{key}]'] = options
                
            except Exception as e:
                print(f"Warning: Skipping invalid key definition line: {line}")
                continue
                
        return key_dict

    def process_definitions(self, key_definitions: str) -> Tuple[str]:
        definitions = self.parse_key_definitions(key_definitions)
        return (json.dumps(definitions),)


NODE_CLASS_MAPPINGS = {
    "Definition Node AIO": DefinitionNodeAIO
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Definition Node AIO": "Definition Node AIO"
}