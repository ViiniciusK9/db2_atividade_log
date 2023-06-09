import psycopg2
import dotenv
import os
from tr import TR


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
        
    
    def fill_table(self, name : str, data : list):
        insert_query = f"INSERT INTO public.{name} VALUES"
        
        # Concatenando os dados
        for i in range(len(data[0])):
            insert_query += " ("
            for j in range(len(data)):
                insert_query += f"{data[j][i]}" + ( "," if (j != len(data)-1) else "" )
                
            insert_query += ( ")," if (i != len(data[0])-1) else ") " )
        
        # Executando a query para inserção
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(insert_query)
            except:
                print("Ocorreu um erro ao inserir na tabela.")
            finally:
                cursor.close()
                self.connection.commit()
       
    
    def update(self, name : str, tr : TR):
        update_query = f"UPDATE {name.lower()} SET {tr.get_column().lower()} = '{tr.get_new()}' WHERE id = '{tr.get_id()}'"
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(update_query)
            except Exception as e:
                print("Ocorreu um erro ao dar update.", e)
            finally:
                cursor.close()
                self.connection.commit()
    

    def redo(self, name : str, tr : TR):
        select_query = f"SELECT {tr.get_column().lower()} FROM {name} WHERE id = '{tr.get_id()}'"
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(select_query)
                return_data = cursor.fetchall()
                
                # Caso o dado atual seja diferente do novo, realizamos o update.
                if (return_data[0][0] != tr.get_new()):
                    update_query = f"UPDATE {name.lower()} SET {tr.get_column()} = '{tr.get_new()}' WHERE id = '{tr.get_id()}'"
                    try:
                        cursor.execute(update_query)
                    except Exception as e:
                        print("Ocorreu um erro ao dar update.", e)
            except Exception as e:
                print("Ocorreu um erro ao dar select.", e)
            finally:
                cursor.close()
                self.connection.commit()
        
    
    def undo(self, name : str, tr : TR):
        select_query = f"SELECT {tr.get_column().lower()} FROM {name} WHERE id = '{tr.get_id()}'"
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(select_query)
                return_data = cursor.fetchall()
                
                # Caso o dado atual seja igual ao que foi modificado, voltamos para o antigo.
                if (return_data[0][0] == tr.get_new()):
                    update_query = f"UPDATE {name.lower()} SET {tr.get_column()} = '{tr.get_old()}' WHERE id = '{tr.get_id()}'"
                    try:
                        cursor.execute(update_query)
                    except Exception as e:
                        print("Ocorreu um erro ao dar update.", e)
            except Exception as e:
                print("Ocorreu um erro ao dar select.", e)
            finally:
                cursor.close()
                self.connection.commit()
    
    
    def select_all(self, name : str) -> list:
        select_query = f"SELECT * FROM {name}"
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(select_query)
                return cursor.fetchall()    
            except:
                print("Erro ao printar o banco de dados")
        return list()
        