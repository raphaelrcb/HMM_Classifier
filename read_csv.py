
import csv

print ("Iniciando leitura do arquivo")

file = open ("run8.csv")

csvreader = csv.reader(file)

cabecalho = []
cabecalho = next(csvreader)

while (cabecalho[0][0] != 'X'):   #Procura pela definição dos dados no arquivo.
    cabecalho = next(csvreader)

print(cabecalho)
# print(n_variables)

rows = []
for row in csvreader:
        rows.append(row)
# print(rows[0])

file.close()
