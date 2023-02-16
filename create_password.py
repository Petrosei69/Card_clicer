import secrets
import string

def create_password():
    password = ''.join(
        secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(12))
    return password