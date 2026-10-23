"""
RECORD CHECK  -  my version
===========================

Name  :  Alisha Shaheen Uppatte
Lane  :  AI 
Date  :  22/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
class Record:
    over_limit_count = 0

    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        '''Returns the status of the record'''
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return 'OVER LIMIT'
        elif percent >= 90:
            return 'WARNING'
        else:
            return 'OK'


# ==================================================================== RECORDS

with open('records.txt', 'w') as f:
    f.write('R-001,80.0,100.0\nR-002,140.0,100.0')


def load_records(path):
    '''Reads the file and returns a list of Record objects'''
    records = []

    with open(path) as f:
        for rec in f:
            label, value, limit = rec.strip().split(',')
            records.append(Record(label, float(value), float(limit)))

    return records


records = load_records('records.txt')


# ==================================================================== OUTPUT

for record in records:
    print('=' * 34)
    print(f'label     : {record.label}')
    print('=' * 34)
    print(f'value     : {record.value:>10.2f}')
    print(f'limit     : {record.limit:>10.2f}')
    print(f'status    : {record.status():>10}')
    print('=' * 34)

    if record.status() == 'OVER LIMIT':
        Record.over_limit_count += 1

print('Number of overlimit records are :', Record.over_limit_count)

