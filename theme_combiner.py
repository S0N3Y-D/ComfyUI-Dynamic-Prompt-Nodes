import json
from typing import Tuple

class ThemeCombinerNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})
            },
            "optional": {
                "def1": ("STRING", {"default": None}),
                "def2": ("STRING", {"default": None}),
                "def3": ("STRING", {"default": None}),
                "def4": ("STRING", {"default": None}),
                "def5": ("STRING", {"default": None}),
                "def6": ("STRING", {"default": None}),
                "def7": ("STRING", {"default": None}),
                "def8": ("STRING", {"default": None}),
                "def9": ("STRING", {"default": None}),
                "def10": ("STRING", {"default": None}),
                "def11": ("STRING", {"default": None}),
                "def12": ("STRING", {"default": None}),
                "def13": ("STRING", {"default": None}),
                "def14": ("STRING", {"default": None}),
                "def15": ("STRING", {"default": None}),
                "def16": ("STRING", {"default": None}),
                "def17": ("STRING", {"default": None}),
                "def18": ("STRING", {"default": None}),
                "def19": ("STRING", {"default": None}),
                "def20": ("STRING", {"default": None}),
                "def21": ("STRING", {"default": None}),
                "def22": ("STRING", {"default": None}),
                "def23": ("STRING", {"default": None}),
                "def24": ("STRING", {"default": None}),
                "def25": ("STRING", {"default": None}),
                "def26": ("STRING", {"default": None}),
                "def27": ("STRING", {"default": None}),
                "def28": ("STRING", {"default": None}),
                "def29": ("STRING", {"default": None}),
                "def30": ("STRING", {"default": None}),
                "def31": ("STRING", {"default": None}),
                "def32": ("STRING", {"default": None}),
                "def33": ("STRING", {"default": None}),
                "def34": ("STRING", {"default": None}),
                "def35": ("STRING", {"default": None}),
                "def36": ("STRING", {"default": None}),
                "def37": ("STRING", {"default": None}),
                "def38": ("STRING", {"default": None}),
                "def39": ("STRING", {"default": None}),
                "def40": ("STRING", {"default": None}),
                "def41": ("STRING", {"default": None}),
                "def42": ("STRING", {"default": None}),
                "def43": ("STRING", {"default": None}),
                "def44": ("STRING", {"default": None}),
                "def45": ("STRING", {"default": None}),
                "def46": ("STRING", {"default": None}),
                "def47": ("STRING", {"default": None}),
                "def48": ("STRING", {"default": None}),
                "def49": ("STRING", {"default": None}),
                "def50": ("STRING", {"default": None})
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("combined_definitions",)
    FUNCTION = "combine_definitions"
    CATEGORY = "S0N3Y"
    
    def combine_definitions(self, seed, **kwargs) -> Tuple[str]:
        combined_dict = {}
        
        for key, value in kwargs.items():
            if value is not None:
                try:
                    theme_dict = json.loads(value)
                    combined_dict.update(theme_dict)
                except json.JSONDecodeError:
                    print(f"Warning: Invalid JSON in {key}, skipping")
        
        return (json.dumps(combined_dict),)

NODE_CLASS_MAPPINGS = {
    "Theme Combiner": ThemeCombinerNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Theme Combiner": "Theme Combiner"
}