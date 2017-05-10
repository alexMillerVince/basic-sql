import psycopg2


def connect_to_db():
    try:
        connect_str = "dbname='codecooler' user='alex' host='localhost' password='alex@Bq150'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        return cursor
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


if __name__ == '__main__':
    connect_to_db()