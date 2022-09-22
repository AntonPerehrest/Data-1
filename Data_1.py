import sqlite3

#Создаем БД
conn = sqlite3.connect('name.db')
# или так - with sqlite3.connect('name.db')as conn:    - тогда не нужно вручную закрывать БД
# Создаем курсор, который будет взаимодействовать с нашей БД
cursor = conn.cursor()
#создадим таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
#  |id | col_1 | col_2|
#  |1 |_______||_____|
#  |2 |_______||_____|
#  |3 |_______||_____|
#заполняем таблицу
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES ('hello','world')''')
# Сохраняем изменения
conn.commit()
#  |id | col_1 | col_2|
#  |1 |__hello_|world|
#  |2 |_______||_____|
#  |3 |_______||_____|
d = 'red'
f = 'black'
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?,?) ''',(d,f))
conn.commit()
#  |id | col_1 | col_2|
#  |1 |__hello_|world|
#  |2 |__red__||black|
#  |3 |_______||_____|



cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)
cursor.close()
conn.close()