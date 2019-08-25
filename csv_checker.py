import csv

with open('complete.csv', encoding='utf-8') as complete:
    with open('ExemplaresDaUnidade.csv', encoding='utf-8') as exemplares:
        complete_reader = csv.DictReader(complete, delimiter=',')
        exemplares_reader = csv.DictReader(exemplares, delimiter=';')
        new_checked_csv = []
        while True:
            row_complete = next(complete_reader)
            row_exemplares = next(exemplares_reader)
            if (row_complete['Cutter'] == row_exemplares['Cutter']):
                row_complete['CDD'] = row_exemplares['\ufeffCDD']
                new_checked_csv.append(row_complete)
        