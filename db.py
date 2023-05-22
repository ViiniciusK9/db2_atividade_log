import psycopg2
import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())

database = os.getenv('DATABASE')
host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
port = os.getenv('PORT')

class DB:
    
    connection = psycopg2.connect(
        dbname= database,
        host= host,
        user= user, 
        password= password,
        port= port
    )
    

    print(connection)
    
    def create(self, name : str, columns : list):
        drop_table_if_exists_query = f"DROP TABLE IF EXISTS public.{name}"
        
        # Caso a tabela já exista no banco ela deve ser apagada previamanete
        try:
            with self.connection.cursor() as cursor:
                try:
                    cursor.execute(drop_table_if_exists_query)
                except:
                    print("Ocorreu um erro ao dropar a tabela.")
        except:
            print("Ocorreu um erro ao tentar obter o cursor.")

        create_query = f"CREATE TABLE IF NOT EXISTS public.{name} ("
        
        # Percorre as colunas na lista de colunas e adiciona ela na create_query
        for column in columns:
            create_query += column + " varchar(200)" + ( "," if (column != columns[-1]) else "" )
        
        create_query += " )"
        
        # Efetua a criação da tabela
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(create_query)
            except:
                print("Ocorreu um erro ao criar a tabela.")
            finally:
                cursor.close()
                self.connection.commit()
        
        
    
    
    def fill_table(self, name : str, dados : list):
        insert_query = f"INSERT INTO public.{name} VALUES"
        
        # Concatenando os dados
        for i in range(len(dados[0])):
            insert_query += " ("
            for j in range(len(dados)):
                insert_query += f"{dados[j][i]}" + ( "," if (j != len(dados)-1) else "" )
                
            insert_query += ( ")," if (i != len(dados[0])-1) else ") " )
        
        # Executando a query para inserção

        with self.connection.cursor() as cursor:
            try:
                cursor.execute(insert_query)
            except:
                print("Ocorreu um erro ao criar a tabela.")
            finally:
                cursor.close()
                self.connection.commit()
       
        
        