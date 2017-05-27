import psycopg2
import credentials


def connect(sql_com):
    def conn_(*args, **kwargs):
        conn_str = "dbname={} user={} host={} password={}".format(credentials.login['dbname'],
                                                       credentials.login['user'],
                                                       credentials.login['host'],
                                                       credentials.login['password'])
        conn = psycopg2.connect(conn_str)
        cursor = conn.cursor()
        try:
            cursor.execute("BEGIN")
            retval = sql_com(cursor, *args, **kwargs)
            cursor.execute("COMMIT")
        except:
            cursor.execute("ROLLBACK")
            raise
        finally:
            cursor.close()
            conn.close()

        return retval

    return conn_

