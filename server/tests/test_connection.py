import psycopg2
from psycopg2 import OperationalError

def test_connection():
    try:
        connection = psycopg2.connect(
            user="siddharth",
            password="22it3052",
            host="192.168.61.130",  # Replace with your PostgreSQL server's IP
            port="5432",
            database="oil_spill_detection"
        )
        print("Connection successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    finally:
        if 'connection' in locals() and connection:
            connection.close()

test_connection()