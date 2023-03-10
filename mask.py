import os
from datetime import datetime

now = datetime.now()
date_str = now.strftime("%d-%m-%Y")

filename =  "cards_pan_" + date_str.replace('-', '')
filename_txt = filename + ".txt"
filename2_txt = "cards_2_pan_" + date_str.replace('-', '') + ".txt"



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

