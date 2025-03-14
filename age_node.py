import json
from typing import Tuple

class CustomAgeDefinitionsNode:
    """
    A node that accepts user input for ages and outputs age definitions for different age groups.
    Each output is a JSON-formatted string containing the age definition.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "age_1": ("INT", {"default": 18, "min": 1, "max": 100}),
            "age_2": ("INT", {"default": 20, "min": 1, "max": 100}),
            "age_3": ("INT", {"default": 23, "min": 1, "max": 100}),
            "age_4": ("INT", {"default": 27, "min": 1, "max": 100}),
            "age_5": ("INT", {"default": 30, "min": 1, "max": 100}),
            "age_6": ("INT", {"default": 33, "min": 1, "max": 100}),
            "age_7": ("INT", {"default": 37, "min": 1, "max": 100}),
            "age_8": ("INT", {"default": 40, "min": 1, "max": 100}),
            "age_9": ("INT", {"default": 43, "min": 1, "max": 100}),
            "age_10": ("INT", {"default": 47, "min": 1, "max": 100}),
            "age_11": ("INT", {"default": 50, "min": 1, "max": 100}),
            "age_12": ("INT", {"default": 55, "min": 1, "max": 100}),
        }}
    
    RETURN_TYPES = ("STRING",) * 12
    RETURN_NAMES = ("age_1", "age_2", "age_3", "age_4", "age_5", "age_6", "age_7", "age_8", "age_9", "age_10", "age_11", "age_12")
    FUNCTION = "generate_ages"
    CATEGORY = "S0N3Y"
    
    def generate_ages(self, age_1: int, age_2: int, age_3: int, age_4: int, age_5: int, age_6: int, 
                     age_7: int, age_8: int, age_9: int, age_10: int, age_11: int, age_12: int) -> Tuple[str, str, str, str, str, str, str, str, str, str, str, str]:
        """Generate age definitions for each age group based on user input."""
        ages = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8, age_9, age_10, age_11, age_12]
        definitions = []
        
        for age in ages:
            age_dict = {"[age]": [f"{age}-year-old"]}
            definitions.append(json.dumps(age_dict))
            
        return tuple(definitions)


NODE_CLASS_MAPPINGS = {
    "Custom Age Definitions": CustomAgeDefinitionsNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Custom Age Definitions": "Custom Age Definitions"
}