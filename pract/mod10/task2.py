import re

def check_color_validity(color):
    rgb_pattern = (r'^(?:#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})|(?:rgb)\(\s*(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d|0)%?\s*,\s*){2}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d|0)%?\s*\))$')
    rgb_match = re.fullmatch(rgb_pattern, color) 

    hex_pattern = (r'#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}')
    hex_match = re.fullmatch(hex_pattern, color) 

    hsl_pattern = (r'hsl\(\s*(\d{1,3})\s*,\s*(\d{1,2}|100)%\s*,\s*(\d{1,2}|100)%\s*\)')
    hsl_match = re.fullmatch(hsl_pattern, color) 
    
    if rgb_match or hex_match or hsl_match:
        return True
    else:
        return False

color_input = input()

valid_color = check_color_validity(color_input)

print(valid_color)