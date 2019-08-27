import csv
import re

complete_csv_path = 'complete_utf.csv'
raw_csv_path = 'exemplares.csv'
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
                                           'estante',
                                           'lado']
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
                            # raw.seek(0)
                            break
                    for pos_row in pos_reader:
                        letters = re.findall('[A-Z]', this_cdd)
                        if (pos_row['de'] == '' or pos_row['ate'] == ''):
                            continue
                        start_cdd = re.findall("[0-9.0-9]+", pos_row['de'])
                        try:
                            start_cdd_float = float(start_cdd[0])
                        except Exception:
                            continue
                        end_cdd = re.findall("[0-9.0-9]+", pos_row['ate'])
                        try:
                            end_cdd_float = float(end_cdd[0])
                        except Exception:
                            continue
                        try:
                            this_cdd_float = float(this_cdd)
                        except Exception:
                            continue
                        if (this_cdd_float >= start_cdd_float and
                            this_cdd_float <= end_cdd_float and
                            (any([x in pos_row['de'] or x in pos_row['ate'] for x in letters]) or len(letters) == 0)):
                            row['bandeja'] = pos_row['bandeija']
                            row['coluna'] = pos_row['coluna']
                            row['estante'] = pos_row['estante']
                            row['lado'] = pos_row['lado']
                            new_complete_csv.writerow(row)
                            break
                    pos_reader.line_num = 0
                    position.seek(0)
