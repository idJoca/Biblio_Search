import csv
import re

complete_csv_path = 'complete_utf.csv'
raw_csv_path = 'tombo.csv'
position_csv_path = 'posicao.csv'
new_complete = 'new_complete.csv'
with open(complete_csv_path, encoding='utf-8') as complete:
    with open(raw_csv_path) as raw:
        with open(position_csv_path, encoding='utf-8') as position:
            with open(new_complete, 'w+', encoding='utf-8') as new_complete:
                pos_reader = csv.DictReader(position, delimiter=';')
                raw_reader = csv.DictReader(raw, delimiter=';')
                complete_reader = csv.DictReader(complete, delimiter=',')
                new_header = complete_reader.fieldnames.copy()
                new_header = new_header + ['bandeja',\
                                           'coluna',\
                                           'estante']
                new_complete_csv = csv.DictWriter(new_complete, new_header)
                new_complete_csv.writeheader()
                used_cutters = []
                for row in complete_reader:
                    this_cutter = row['Cutter']
                    for raw_row in raw_reader:
                        if (this_cutter == raw_row['Cutter'] and not
                            any(this_cutter == x for x in used_cutters)):
                            this_cdd = raw_row['CDD']
                            used_cutters.append(this_cutter)
                            break
                    for pos_row in pos_reader:
                        start_cdd = list(filter(None, re.split("[A-Z]", pos_row['de'])))
                        end_cdd = list(filter(None, re.split("[A-Z]", pos_row['ate'])))
                        if (any([this_cdd >= x for x in start_cdd]) and
                            any([this_cdd >= x for x in end_cdd])):
                            row['bandeja'] = pos_row['bandeija']
                            row['coluna'] = pos_row['coluna']
                            row['estante'] = pos_row['estante']
                            new_complete_csv.writerow(row)
                            break
                    position.seek(0)
