from zipencrypt import ZipFile
from datetime import datetime
import os
import create_password

now = datetime.now()
date_str = now.strftime("%d-%m-%Y")
date_str = date_str.replace('-', '')
current_session = "current_session_passwords" + date_str + ".txt"

directory = os.getcwd()

folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

def arch(file):
    file_zip = file.replace(".txt", "").replace(date_str, "") + date_str + ".zip"
    password = create_password.create_password()
    # archiving
    arr = bytes(password, 'utf-8')
    with ZipFile(file_zip, "w") as myzip:
        myzip.write(file, pwd=arr)

    with open('tg_msg.txt', 'a') as filehandle:
        filehandle.writelines(file_zip + " - " + password + "\n")

    with open(current_session, 'w') as filehandle:
        filehandle.writelines(file_zip + " - " + password + "\n")

def arch_both(file, file2):
    file_zip = file.replace(".txt", "").replace(date_str, "") + date_str + ".zip"
    password = create_password.create_password()
    # archiving
    arr = bytes(password, 'utf-8')
    with ZipFile(file_zip, "w") as myzip:
        myzip.write(file, pwd=arr)

    with open('tg_msg.txt', 'a') as filehandle:
        filehandle.writelines(file_zip + " - " + password + "\n")

    with open(current_session, 'w') as filehandle:
        filehandle.writelines(file_zip + " - " + password + "\n")

    file_zip = file2.replace(".txt", "").replace(date_str, "") + date_str + ".zip"
    password = create_password.create_password()
    # archiving
    arr = bytes(password, 'utf-8')
    with ZipFile(file_zip, "w") as myzip:
        myzip.write(file2, pwd=arr)

    with open('tg_msg.txt', 'a') as filehandle:
        filehandle.writelines(file_zip + " - " + password + "\n")

    with open(current_session, 'a') as filehandle:
        filehandle.writelines(file_zip + " - " + password + "\n")
