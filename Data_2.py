import sqlite3

# with sqlite3.connect('table.bd') as con:
#     cursor = con.cursor()
#
#     zap1 = "create table if not exists table1(id integer primary key, name text, age integer, password text);"
#     cursor.execute(zap1)
#
#     zap2 = "insert into table1(name, age, password) values(?,?,?);"
#     cursor.execute(zap2, ('dima', int(input()), '123'))
#     con.commit()
#
#     zap3 = "select * from table1;"
#     k = cursor.execute(zap3).fetchall()
#     cursor.close()
#
# for i in k:
#     print(i)

# Создать 2 таблицы в Базе Данных
# Одна будет хранить текстовые данные(1 колонка)
# Другая числовые(1 колонка)
# Есть список, состоящий из чисел и слов.
# Если элемент списка слово, записать его в соответствующую таблицу, затем посчитать длину слова и
# записать её в числовую таблицу
# Если элемент списка число: проверить, если число чётное записать его в таблицу чисел, если нечётное,
# то записать во вторую таблицу слово: «нечётное»
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице.
# Если меньше, то обновить 1 запись в первой таблице на «hello»

spis = ['home', 'name', 'country', 1, 3, 6, 22]
with sqlite3.connect('less_2_data_1.db') as con:
    cursor = con.cursor()

    zap1 = "create table if not exists tab_words(words text);"
    cursor.execute(zap1)

    zap2 = "create table if not exists tab_nums(nums integer);"
    cursor.execute(zap2)

    ln = 0
    cht_ncht = 'нечетное'
    for i in spis:
        if type(i) is str:
            zap1_1 = "insert into tab_words(words) values(?);"
            cursor.execute(zap1_1, (i,))
            con.commit()
            ln = len(i)
            zap2_1 = "insert into tab_nums(nums) values(?);"
            cursor.execute(zap2_1, (f'Длинна {i} - {ln}',))
            con.commit()
        elif type(i) is int:
            zap2_1 = "insert into tab_nums(nums) values(?);"
            cursor.execute(zap2_1, (i,))
            con.commit()
            if i % 2 != 0:
                zap1_1 = "insert into tab_words(words) values(?);"
                cursor.execute(zap1_1, (f'{i} - {cht_ncht}',))
                con.commit()

    zap3 = "select * from tab_words;"
    k_1 = cursor.execute(zap3).fetchall()
    print(k_1)

    zap4 = "select * from tab_nums;"
    k_2 = cursor.execute(zap4).fetchall()
    print(k_2)

    if len(k_2) > 5:
        print(f'из первой таблицы удалили {k_1[0]}')
        k_1.remove(k_1[0])
        print(k_1)
    elif len(k_2) < 5:
        k_1[0] = 'hello'

    zap5 = "drop table tab_words;"
    cursor.execute(zap5)
    zap6 = "drop table tab_nums;"
    cursor.execute(zap6)
    cursor.close()
