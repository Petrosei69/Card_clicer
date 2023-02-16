from zipencrypt import ZipFile
import secrets
import string
import os

def create_password():
    password = ''.join(
        secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(12))
    return password

folder_path = 'venv'
zip_name = 'my_archive.zip'
zip_password = create_password()


with ZipFile(zip_name, 'w') as myzip:
    print(zip_password)
    for root, dirs, files in os.walk(folder_path):
        password = create_password()
        arr = bytes(password, 'utf-8')
        for file in files:
            myzip.write(os.path.join(root, file), pwd=arr)

