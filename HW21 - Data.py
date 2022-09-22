import sqlite3
import random

# Задание №1
# Создайте новую Базу данных.
# В ней создайте таблицу с тремя полями, два текстовых, одно – целое число.
# Число запрашивается с клавиатуры, а слова задаются статически.
# * Выведите каждую запись в отдельную строку
# with sqlite3.connect('data_1.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     col_1 TEXT,
#     col_2 TEXT,
#     col_3 INT)''')
#     a = 'hello'
#     b = 'world'
#     cursor.execute('''INSERT INTO tab_1(col_1, col_2, col_3) VALUES (?,?,?)''',(a, b, int(input('Введите число:'))))
#     # cursor.execute('''DELETE FROM tab_1''')
#     #cursor.execute('''DROP TABLE tab_1''')
#
#     conn.commit()
#     cursor.execute('''SELECT*FROM tab_1''')
#     k = cursor.fetchall()
#     cursor.close()
# for i in k[0][1:]:
#     print(i)


# Задание №2
# Создайте новую Базу данных.
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Посчитайте среднее арифметическое всех элементов без учёта id
# Если среднее арифметическое больше количества записей в БД, то удалите четвёртую запись БД

# conn = sqlite3.connect('data_2.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     col_1 INTEGER,
#     col_2 INTEGER)''')
# cursor.execute('''INSERT INTO tab_2(col_1, col_2) VALUES(?,?)''', (random.randint(0, 9), random.randint(0, 9)))
# conn.commit()
# cursor.execute('''SELECT*FROM tab_2''')
# k = cursor.fetchall()
# # cursor.execute('''DROP TABLE tab_2''')
# # conn.commit()
# print(k)
#
#
# sred = 0
# for i in k:
#     for j in i[1:]:
#         sred += j / 2
# print(f'Среднее арифметическое - {sred}')
# if sred > len(k):
#     cursor.execute('''DELETE FROM tab_2 WHERE id = 4''')
#     conn.commit()
#     print(k)


#Задание №3
# Создайте новую Базу данных
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Выберите случайную запись из БД
# Если каждое число данной записи чётное, то удалите эту запись, если нечётное, то обновите данные в ней на(2,2)

# conn = sqlite3.connect('data_3.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_3(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     col_1 INTEGER,
#     col_2 INTEGER)''')
# cursor.execute('''INSERT INTO tab_3(col_1, col_2) VALUES(?,?)''', (random.randint(0, 9), random.randint(0, 9)))
# conn.commit()
# cursor.execute('''SELECT*FROM tab_3''')
# k = cursor.fetchall()
# # cursor.execute('''DROP TABLE tab_3''')
# # conn.commit()
# print(k)
#
#
# rand_choice = random.choice(k)
# print(rand_choice)
# if (rand_choice[1] % 2 != 0) and (rand_choice[-1] % 2 != 0):
#     cursor.execute('''UPDATE tab_3 SET
#                             col_1 = 2,
#                             col_2 = 2 WHERE id = ?''', (rand_choice[0],))
#     conn.commit()
#     print(k)
# elif (rand_choice[1] % 2 == 0) and (rand_choice[-1] % 2 == 0):
#     cursor.execute('''DELETE FROM tab_3 WHERE id = ?''', (rand_choice[0],))
#     conn.commit()
#     print(k)


#Задание №5
# Создать таблицу в Базе Данных с тремя колонками(id, 2 - text, 3 - text).
# Заполнить её с помощью INSERT данными (3 записи).
# Удалить с помощью DELETE 2 запись. Обновить значения 3-ей записи на: hello world с помощью UPDATE
# *Записать данные с таблицы в файл в три колонки. Первая – id, вторая и третья с данными.

conn = sqlite3.connect('data_4.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_4(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                '2' TEXT,
                '3' TEXT)''')
cursor.execute('''INSERT INTO tab_4('2', '3') VALUES('two','three')''')
conn.commit()
cursor.execute('''SELECT*FROM tab_4''')
k = cursor.fetchall()
# cursor.execute('''DROP TABLE tab_4''')
conn.commit()
print(k)

cursor.execute('''DELETE FROM tab_4 WHERE id = 1''')
conn.commit()
cursor.execute('''DELETE FROM tab_4 WHERE id = 2''')
conn.commit()

cursor.execute('''UPDATE tab_4 SET '2' = 'hello', '3' = 'world' WHERE id = 3''')
conn.commit()
print(k)

try:
    with open('text.txt','r+', encoding='utf-8') as file_1:
        file_1.write('id\t2\t3\n')
        for i in k:
            for j in i:
                file_1.write(f'{j}\t')
                if j == i[-1]:
                    file_1.write('\n')
except FileNotFoundError:
    print('UNABLE TO OPEN THE FILE')

conn.close()
cursor.close()


