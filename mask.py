import os
from datetime import datetime
import arc_file
import arc_all
import tkinter as tk

# current dateTime
now = datetime.now()

# convert to string
date_str = now.strftime("%d-%m-%Y")

filename =  "cards_pan_" + date_str.replace('-', '')
filename_txt = filename + ".txt"
filename_zip = filename + ".zip"
filename2 =  "cards_2_pan_" + date_str.replace('-', '')
filename2_txt = filename2 + ".txt"
filename2_zip = filename2 + ".zip"


print(filename)
print(filename_txt)
print(filename_zip)

#  empty line cleaner
with open('file.txt') as f:     # enter your filename
    lines = f.readlines()
    non_empty_lines = (line for line in lines if not line.isspace())

    try:
        os.mkdir(os.path.join(os.getcwd(), 'out_files'))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), 'out_files'))

    with open('cards_full_pan.txt', 'w') as n_f:
        n_f.writelines(non_empty_lines)


#  space cleaner
def read2list(file):
    file = open('cards_full_pan.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]
    return lines

lines = read2list('cards_full_pan.txt')


for i in range(len(lines)):
    lines[int(i)] = lines[int(i)].replace(' ', '')

with open('cards_full_pan.txt','w', encoding="utf-8") as tfile:
	tfile.write('\n'.join(lines))

# part of creating new files:  1.sequence with hidden numbers  2.hidden numbers only
def cutter(cards_full_pan):
    file = open('cards_full_pan.txt', "r")
    all_words = []
    line = file.readline().split()
    while line:
        all_words.extend(line)
        line = file.readline().split()

    arr1 = []

    for i in range(len(all_words)):
        arr2 = []
        for x in all_words[i]:
            arr2.append(x)
        arr1.append(arr2)

    arr2 = []
    for i in range(len(all_words)):
        arr3 = []
        for k in range(6):
            arr3.append(arr1[i][k + 6])
            arr1[i].pop(k + 6, )
            arr1[i].insert(k + 6, '*')
        arr2.append(arr3)

    for i in range(len(arr1)):
        arr1[i].insert(4, ' ')
        arr1[i].insert(9, ' ')
        arr1[i].insert(14, ' ')

    arr4 = []
    arr5 = []

    for i in range(len(arr1)):
        s = ''.join(map(str, arr1[i]))
        arr4.append(s)

    with open(filename2_txt, 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in arr4)

    for i in range(len(arr2)):
        q = ''.join(map(str, arr2[i]))
        arr5.append(q)
    
    with open(filename_txt, 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in arr5)

cutter(filename_txt)


# os.chdir(r'put here your directory')                  # <-------------  Enter directory to archive all folders inside
file = "put here your name of file"                     # <-------------  Your file in current directory, this file must be in the folder above
directory = os.getcwd()



root = tk.Tk()
root.geometry('840x500')

label = tk.Label(root, text=" Привет, если ты видишь это окно, значит файлы с данными карт уже созданы в отдельной папке проекта \n"
                            "           чтобы архивировать эти файлы на выбор предоставлены три первые кнопки                 \n\n"
                            " Чтобы архивировать любой другой файл, нужно указать его имя и путь до него в указанном месте в скрипте и нажать кнопку 4\n\n"
                            " Чтобы архивировать все папки внутри определенной директории, нужно указать эту директорию в указанном месте в скрипте и нажать кнопку 5\n")


button1 = tk.Button(root, text="1. Архивировать оба файла с данными карт", command=lambda: arc_file.arch_both(filename_txt, filename2_txt), width=50, height=2)
button2 = tk.Button(root, text="2. Архивировать файл с 6 цифрами", command=lambda: arc_file.arch(filename_txt), width=50, height=2)
button3 = tk.Button(root, text="3. Архивировать файл с 10 цифрами", command=lambda: arc_file.arch(filename2_txt), width=50, height=2)
button4 = tk.Button(root, text="4. Архивировать свой файл", command=lambda: arc_file.arch(file), width=50, height=2)
button5 = tk.Button(root, text="5. Архивировать все папки в указанной директории", command=lambda: arc_all.arch(directory), width=50, height=2)

label.grid(row=0, column=0, padx=10, pady=10)
button1.grid(row=1, column=0, padx=10, pady=10)
button2.grid(row=2, column=0, padx=10, pady=10)
button3.grid(row=3, column=0, padx=10, pady=10)
button4.grid(row=4, column=0, padx=10, pady=10)
button5.grid(row=5, column=0, padx=10, pady=10)

root.mainloop()
