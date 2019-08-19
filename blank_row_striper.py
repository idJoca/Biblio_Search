import csv

with open('complete_sem_acento.csv') as in_file:
    with open('complete.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        for row in in_file:
            if row != '\n':
                out_file.write(row)