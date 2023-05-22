import psycopg2
import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())

database = os.getenv('DATABASE')
host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
port = os.getenv('PORT')

connection = psycopg2.connect(
    dbname= database,
    host= host,
    user= user, 
    password= password,
    port= port
)

print(connection)
with connection:
    with connection.cursor() as curs:
        try:
            curs.execute("INSERT INTO public.mesas(id, lugares, livre) VALUES (50, 50, 50)")
        except:
            print("deu ruim")