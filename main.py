# Cleaner file to the strings

#  empty line cleaner
with open('file.txt') as f:
    lines = f.readlines()
    non_empty_lines = (line for line in lines if not line.isspace())
    with open('new_file.txt', 'w') as n_f:
        n_f.writelines(non_empty_lines)

#  space cleaner
def read2list(file):
    # открываем файл в режиме чтения utf-8
    file = open('new_file.txt', 'r', encoding='utf-8')

    # читаем все строки и удаляем переводы строк
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]
    return lines
lines = read2list('new_file.txt')


for i in range(len(lines)):
    lines[int(i)] = lines[int(i)].replace(' ', '')

with open('new_file.txt','w', encoding="utf-8") as tfile:
	tfile.write('\n'.join(lines))


file = open('new_file.txt', "r")
all_words = []
line = file.readline().split()
while line:
    all_words.extend(line)
    line = file.readline().split()

arr1 = []
result_list = []

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
        arr1[i].pop(k + 6,)
        arr1[i].insert(k + 6, '*')
    arr2.append(arr3)

arr4 = []
arr5 = []

for i in range(len(arr1)):
    s = ''.join(map(str, arr1[i]))
    arr4.append(s)

with open('array1.txt', 'w') as filehandle: filehandle.writelines("%s\n" % place for place in arr4)

for i in range(len(arr2)):
    q = ''.join(map(str, arr2[i]))
    arr5.append(q)

with open('array2.txt', 'w') as filehandle: filehandle.writelines("%s\n" % place for place in arr5)

