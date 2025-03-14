from typing import Tuple

class ControlPromptNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": True,
                    "label": "Control Prompt",
                    "placeholder": "Enter your template using [theme] placeholders\nExample: A woman with [hair-color] hair wearing a [dress-type] in [location]",
                    "lines": 20
                })
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt_text",)
    FUNCTION = "output_prompt"
    CATEGORY = "S0N3Y"
    
    def output_prompt(self, prompt: str) -> Tuple[str]:
        return (prompt,)


NODE_CLASS_MAPPINGS = {
    "Control Prompt": ControlPromptNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Control Prompt": "Control Prompt"
}