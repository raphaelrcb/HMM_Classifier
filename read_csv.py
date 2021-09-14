
import csv

print ("hello world")

file = open ("run6.csv")

csvreader = csv.reader(file)

cabecalho = []
cabecalho = next(csvreader)

while (cabecalho[0][0] != 'X'):#Procura pela definição dos dados no arquivo.
    cabecalho = next(csvreader)

print(cabecalho)

rows = []
for row in csvreader:
        rows.append(row)
# print(rows[0])

file.close()
