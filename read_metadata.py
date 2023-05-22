import json
from db import DB

with open("metadado.json") as my_json:
    data = json.load(my_json)

print(data)
print(data.keys())
tables = data.keys()
for table in tables:
    print(table)
print(table)

print(data[table])

columns_list = list()
dados_list = list()

for column in data[table]:
    columns_list.append(column)
    dados_list.append(data[table][column])

print(columns_list)
print(dados_list)
    

database = DB()

database.create(table, columns_list)
database.fill_table(table, dados_list)
