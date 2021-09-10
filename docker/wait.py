import psycopg2
import time

while True:
    time.sleep(0.5)
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="code-project",
            user="postgres",
            password="1234"
        )
        break
    except:
        print("Waiting for database...")