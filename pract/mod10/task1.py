import re

def validate_password(s:str) -> bool:
    if re.fullmatch(r'[A-Z, a-z, 0-9, (^$%@#&*!?)]*', s) == None:
        return False
    if re.fullmatch(r'.{6,}', s) == None:
        return False
    if re.search(r'[A-Z]+', s) == None:
        return False
    if re.search(r'[0-9]{1}', s) == None:
        return False
    if re.search(r'^(?=(?:.*[A-Z]){2})(?=.*\d)(?=(?:.*[@$%^#&*!?]){2})(?!.*(.)\1\1)[A-Za-z0-9^$%@#&*!?]{6,}$', s) == None:
        return False
    if re.search(r'[A-Z, a-z, 0-9, (^$%@#&*!?)]{0,2}', s) == None:
        return False
    return True

password = input()

print(validate_password(password))