import re
import doctest

def validate_password(s:str) -> bool:
    """
    >>>validate_password('aA1!*!1Aa')
    True
    >>>validate_password('rtG3FG!Tr^e')
    True
    >>>validate_password('oF^a1D@y5e6')
    True
    >>>validate_password('enroi#$rkdeR#$092uWedchf34tguv394h')
    True
    >>>validate_password('пароль')
    False
    >>>validate_password('password')
    False
    >>>validate_password('qwerty')
    False
    >>>validate_password('lOngPa$$$W0Rd')
    False
    """
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


doctest.testmod()