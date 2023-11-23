import re
import doctest

def check_color_validity(color):
    """
    >>>check_color_validity('#21f48D')
    True
    >>>check_color_validity('#888')
    True
    >>>check_color_validity('rgb(255, 255,255)')
    True
    >>>check_color_validity('rgb(10%, 20%, 0%)')
    True
    >>>check_color_validity('hsl(200,100%,50%)')
    True
    >>>check_color_validity('hsl(0, 0%, 0%)')
    True
    >>>check_color_validity('#2345')
    False
    >>>check_color_validity('ffffff')
    False
    >>>check_color_validity('rgb(257, 50, 10)')
    False
    >>>check_color_validity('hsl(20, 10, 0.5)')
    False
    >>>check_color_validity('hsl(34%, 20%, 50%)')
    False
    """
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


doctest.testmod()