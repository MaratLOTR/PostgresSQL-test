import psycopg2
from config import db_name, user, host, password

try:
    connection = psycopg2.connect(
        dbname=db_name, user=user,
        password=password, host=host
    )
    connection.autocommit = True
    with connection.cursor() as cur:
        insert_query_author = '''INSERT INTO author (name_author)
                            VALUES ('Булгаков М.А.'),
                                   ('Достоевский Ф.М.'),
                                   ('Есенин С.А.'),
                                   ('Пастернак Б.Л.');'''
        cur.execute(insert_query_author)

    with connection.cursor() as cur:
        insert_query_genre = '''INSERT INTO genre (name_genre)
                                VALUES  ('Роман'),
                                        ('Поэзия'),
                                        ('Приключения');'''
        cur.execute(insert_query_genre)

    with connection.cursor() as cur:
        insert_query_book_sample = '''INSERT INTO book (title, author_id, genre_id, price, amount)
                                        VALUES (%s, %s, %s, %s, %s)'''
        book_tuple = ('Мастер и Маргарита', 1, 1, 670.99, 3)
        cur.execute(insert_query_book_sample, book_tuple)

        insert_query_book = '''INSERT INTO book (title, author_id, genre_id, price, amount)
                                VALUES 
                                       ('Белая гвардия ', 1, 1, 540.50, 5),
                                       ('Идиот', 2, 1, 460.00, 10),
                                       ('Братья Карамазовы', 2, 1, 799.01, 3),
                                       ('Игрок', 2, 1, 480.50, 10),
                                       ('Стихотворения и поэмы', 3, 2, 650.00, 15),
                                       ('Черный человек', 3, 2, 570.20, 6),
                                       ('Лирика', 4, 2, 518.99, 2);'''

    with connection.cursor() as cur:
        select_author_name = '''SELECT name_author FROM author LIMIT 10'''
        cur.execute(select_author_name)
        print(cur.fetchone()) #Булгаков
        print(cur.fetchone()) #Достоевский

        for record in cur.fetchone():
            print("fetchone", record)

        for record in cur.fetchmany(3):
            print("fetchmany",record)

        for record in cur.fetchall():
            print("fetchall", record)

except Exception as _ex:
    print("[INFO] Error while working with PostgresSQL",_ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgresSQL connection closed")


