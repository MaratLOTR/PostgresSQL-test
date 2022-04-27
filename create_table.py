import psycopg2
from config import db_name, user, host, password

try:
    connection = psycopg2.connect(
        dbname=db_name,
        user=user,
        password=password,
        host=host
    )

    cur = connection.cursor()
    create_table_author = '''CREATE TABLE author
                    (
                        author_id serial PRIMARY KEY,
                        name_author VARCHAR(50)
                    )'''
    cur.execute(create_table_author)
    connection.commit()
    cur.close()
    print('[INFO] Author table created')

    with connection.cursor() as cur:
        create_table_genre = '''CREATE TABLE genre
        (
            genre_id serial
                PRIMARY KEY,
            name_genre varchar(30)
        );'''
        cur.execute(create_table_genre)
        connection.commit()
        print('[INFO] Genre table created')

    with connection.cursor() as cur:
        connection.autocommit = True
        create_table_book = '''CREATE TABLE book
        (
            book_id serial
                PRIMARY KEY,
            title VARCHAR(50),
            author_id INT,
            genre_id int,
            price DECIMAL(8, 2),
            amount INT,
            FOREIGN KEY (author_id) REFERENCES author (author_id) ON DELETE CASCADE,
            FOREIGN KEY (genre_id) REFERENCES genre (genre_id) ON DELETE SET NULL
        );'''
        cur.execute(create_table_book)
        print('[INFO] Books table created')
except Exception as _ex:
    print("[INFO] Error while working with PostgresSQL",_ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgresSQL connection closed")