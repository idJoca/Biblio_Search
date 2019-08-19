import csv
import subprocess
import threading
import request

threads = []
threads_index = 0
pool_size = 2
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

def call_request(book_name, book_cutter):
    subprocess.Popen('python request.py ' + str(book_name) + " " + str(book_cutter))

with open('complete.csv') as complete:
    reader = csv.reader(complete)
    row_count = sum(1 for row in reader)
    last_index = (row_count - 1) / 2

with open('cutter_name.csv') as cutter_name_csv:
    reader = csv.DictReader(cutter_name_csv)
    for row in reader:
        if (index < last_index):
            index += 1
            continue
        else:
            request.Request(row['Cutter'], row['Titulo']).run()
