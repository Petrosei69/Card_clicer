from zipencrypt import ZipFile
from datetime import datetime
import os
import create_password

now = datetime.now()
date_str = now.strftime("%d-%m-%Y")
date_str = date_str.replace('-', '')
current_dir_session = "current_dir_session_passwords" + date_str + ".txt"

def arch(directory):
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    for folder in folders:
        # named archive
        zip_name = f"{folder}.zip"
        with ZipFile(zip_name, 'w') as zip_file:
            # create list of files in folders
            files = [f for f in os.listdir(os.path.join(directory, folder)) if os.path.isfile(os.path.join(directory, folder, f))]
            # add files to archive and set a password
            password = create_password.create_password()
            arr = bytes(password, 'utf-8')
            print(password)
            for file in files:
                zip_file.write(os.path.join(directory, folder, file), file, pwd=arr)

            with open('tg_msg.txt', 'a') as filehandle:
                filehandle.writelines(f"{folder}_" + date_str + " - " + password + "\n")

            with open(current_dir_session, 'a') as filehandle:
                filehandle.writelines(f"{folder}_" + date_str + " - " + password + "\n")
