import psycopg2
import time

while True:
    time.sleep(0.5)
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="code_project",
            user="postgres",
            password="1234"
        )
        print("Connected to database!")
        break
    except:
        print("Waiting for database...")