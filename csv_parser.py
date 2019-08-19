import csv
import unidecode
from urllib.parse import quote

unique_book_names_csv = []
unique_book_names_treated_csv = []
with open('tombo.csv') as tombo:
    reader = csv.DictReader(tombo, delimiter=';')
    for row in reader:
        try:
            if not any(row['Cutter'] in sublist['Cutter'] for sublist in unique_book_names_csv):
                unique_book_names_csv.append({'Cutter':row['Cutter'],
                                              'Titulo':quote(unidecode \
                                              .unidecode(row['Título']).lower(), safe='')})
        except GeneratorExit:
            pass
with open('cutter_name.csv', 'w') as cutter_name_csv:
    writer = csv.DictWriter(cutter_name_csv, ['Cutter', 'Titulo'])
    writer.writeheader()
    writer.writerows(unique_book_names_csv)
