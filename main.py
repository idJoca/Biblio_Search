import csv
import subprocess
import threading
import request

file_path = 'complete_utf.csv'
complete_csv_header = ["Cutter",
                       "Titulo",
                       "Descricao",
                       "Ano",
                       "Autores",
                       "Paginas",
                       "ISBN",
                       "Idioma",
                       "Src"]

index = 0

with open(file_path, 'a+', encoding='utf-8') as complete:
    reader = csv.reader(complete)
    row_count = sum(1 for row in reader)
    last_index = (row_count - 1) / 2

with open('cutter_name.csv', encoding='utf-8') as cutter_name_csv:
    reader = csv.DictReader(cutter_name_csv)
    for row in reader:
        if (index < last_index):
            index += 1
            continue
        else:
            request.Request(row['Cutter'], row['Titulo'], file_path).run()
