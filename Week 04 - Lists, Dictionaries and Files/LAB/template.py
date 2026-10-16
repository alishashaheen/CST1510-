"""
RECORD CHECK  -  my version
===========================

Name  :  Alisha Shaheen
Lane  :  AI      (delete two)
Date  :  16/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

#THRESHOLD
# =================================================================== FUNCTIONS

def check_record(value,limit):
    '''Return difference, percent and status'''
    difference = limit - value
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, used, total, free, percent, status):
    '''Print the record check report'''
    print("-" * 30)
    print(f'RECORD CHECK - {label}')
    print("-" * 30)
    print(f'Used    : {used:10.2f}')
    print(f'Total   : {total:10.2f}')
    print(f'Free    : {free:10.2f}')
    print(f'Percent : {percent:10.2f} %')
    print(f'Status  : {status}')
    print("-" * 30)

# ====================================================================== STORE

records = [
    {"label": "R-001", "value": 87, "limit": 100},
    {"label": "R-002", "value": 120, "limit": 100},
    {"label": "R-003", "value": 95, "limit": 100}
]

# =============================================================== PROCESS + OUTPUT

for record in records:
    difference, percent, status = check_record(record['value'], record['limit'])
    print_report(record['label'],record['value'],record['limit'],difference,percent,status)






#TYPICAL

# =================================================================== FUNCTIONS

def check_record(value, limit):
    '''Return difference, percent and status'''
    difference = limit - value
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, used, total, free, percent, status):
    '''Print the record check report'''
    print("-" * 30)
    print(f'RECORD CHECK - {label}')
    print("-" * 30)
    print(f'Used    : {used:10.2f}')
    print(f'Total   : {total:10.2f}')
    print(f'Free    : {free:10.2f}')
    print(f'Percent : {percent:10.2f} %')
    print(f'Status  : {status}')
    print("-" * 30)

# ====================================================================== STORE

def load_records(path):
    '''load records from text file'''

    records = []

    with open(path) as f:
        for line in f :
            label,value,limit=line.strip().split(',')

            value = float(value)
            limit = float(limit)

            record = {'label': label,'value': value,'limit': limit}

            records.append(record)

    return records

# PROCESS + OUTPUT

records = load_records('records_sample.txt')
for record in records:
    difference, percent, status = check_record(record['value'], record['limit'])

    print_report(record['label'],record['value'],record['limit'],difference,percent,status







# =============================================================== PROCESS + OUTPUT

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = []   # replace with your code


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
