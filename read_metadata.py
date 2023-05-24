import json
from db import DB
from tr import TR

with open("metadado.json") as my_json:
    data = json.load(my_json)

#print(data)
#print(data.keys())
tables = data.keys()
for table in tables:
    print(table)
#print(table)

#print(data[table])

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

log = list()

with open("entrada_log", "r") as arquivo:
    for row in arquivo:
        log.append(row.replace('\n', ''))
        
print(log)

lista_log = list()
tag_redo = set()
tag_undu = set()

for row in log:
    row = row.replace('<', '').replace('>', '')
    print(row)
    aux = row.split(" ")
    if (len(aux) == 2):
        
        if (aux[0] == "start"):
            tag_undu.add(aux[1])
        else:
            tag_undu.remove(aux[1])
            tag_redo.add(aux[1])
        
    else:
        a = list(row.split(","))
        tr1 = TR(*a)
        print(tr1)
        
        
print(tag_redo)
print(tag_undu)

