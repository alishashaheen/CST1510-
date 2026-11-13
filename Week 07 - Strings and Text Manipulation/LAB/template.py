"""
RECORD CHECK  -  my version
===========================

Name  :  Alisha Shaheen
Lane  :  AI 
Date  :  12/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line(raw_line):
  '''turn messy line into a clean line'''
  line = raw_line.strip()
  hostname_part, rest = line.split(',',1)
  hostname=hostname_part.strip().lower()

  field={}
  for pair in rest.split(','):
    key,value=pair.split('=')
    field[key.strip().lower()] = float(value.strip())
  return {'hostname': hostname, 'used': field['used'], 'total':field['total']}

def status(used,total):
  percent=(used/total)*100
  if percent >=100:
    return "OVER LIMIT"
  elif percent >=90:
    return "WARNING"
  else:
    return "OK"

# ====================================================================== INPUT

raw_records = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,USED=95,TOTAL=100",
    "  Srv-03, used = 45, total = 100 ",
    "srv-04 , USED=100 , TOTAL=100",
    "  SRV-05 , used=70 , total=100  "
]

with open("messy_lines.txt", "w") as f:
    for line in raw_records:
        f.write(line + "\n")

# =============================================================== PROCESS + OUTPUT

count = 0
flagged = 0

print("CLEANED RECORDS:")

with open("messy_lines.txt", "r") as f:
    for raw_line in f:
        try:
            record = parse_line(raw_line)
            current_status = status(record["used"], record["total"])
            print(record, current_status)

            count += 1
            if current_status != "OK":
                flagged += 1
        except ValueError as e:
            print("Invalid number:", e)

print("\nSummary")
print("Total records:", count)
print("Flagged records:", flagged)