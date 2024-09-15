# Задание 1
# Дано два текстовых файла. Выяснить, совпадают ли 
# их строки. Если нет, то вывести несовпадающую строку 
# из каждого файла

# f = open('file.txt', 'r', encoding='utf-8')
# lines1 = set(f.read().split())
# f.close()
# f = open('file2.txt', 'r', encoding='utf-8')
# lines2 = set(f.read().split())
# f.close()

# print(lines1)
# print(lines2)

# print(lines1.intersection(lines2))





# Задание 3
# Дан текстовый файл. Удалить из него последнюю 
# строку. Результат записать в другой файл


# with open('delet.txt', 'r', encoding ='utf-8') as f:
#  lines = f.readlines()
# with open('delet2.txt', 'w',encoding ='utf-8') as f:
#  for line in lines:
#   if line.strip("\n") != "nickname_to_delete":
#    f.write(line)
#    print(lines)



# Задание 4
# Дан текстовый файл. Найти длину самой длинной 
# строки.


# f = open('leng.txt','r',encoding ='utf-8)
# s = f.read()
# m = 1
# maxlen = 0
# for i in range(len(s) - 1):
#     if s[i] == "R" and s[i + 1] == "R":
#         m += 1
#         if mexlen < m:
#             maxlen = m 
#     else:
#         m = 1
# if maxlen == 0 and "R" in s:
#     maxlen = 1
# print(maxlen) 


# Задание 5
# Дан текстовый файл. Посчитать сколько раз в нем 
# встречается заданное пользователем слово

# f: str = input('Введите фрукт:').lower()
# fruits: tuple = ('Apple', 'Banana','Watermelon', 'Berry', 'Apple', 'berry')
# counter = 0
# for i in fruits:
#  if i.lower() ==f:
#   counter += 1

#  print(f'Количество фрукт под названием "{f}":{counter}')

