import psycopg2
from Config import host, user, password, db_name

try:
    #connect to exist database
    connection = psycopg2.connect(
        host = host,
        user =user,
        password = password,
        database = db_name
    )

    # the cursor for perfoming database operations
    # cursor = connecion.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")


except Exception as ex:
    print("[INFO] Error while working with PostgreSQL", ex)
finally:
    if connection:
        #cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")