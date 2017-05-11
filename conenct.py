import psycopg2


def connect_to_db():
    try:
        connect_str = "dbname='codecool' user='alex' host='localhost' password='alex@Bq150'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        return cursor
    except Exception as e:
        print(e)
