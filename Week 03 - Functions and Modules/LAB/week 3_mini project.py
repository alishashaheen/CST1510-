"""
RECORD CHECK  -  my version
===========================

Name  :  Alisha Shaheen
Lane  :  AI 
Date  :  8/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""




#THRESHOLD

# =================================================================== FUNCTIONS
def status_of(percent):
    if percent >= 100:
        return 'OVER LIMIT'
    elif percent >=90:
        return 'WARNING'
    else:
        return 'OK'
# ==================================================================== INPUT
label = input('enter the record name :')
value = float(input('enter the used value :'))
limit = float(input('enter the total value :'))
# ================================================================== PROCESS
difference = limit - value 
percent = (value/limit) * 100
status = status_of(percent)
# =================================================================== OUTPUT
print('=' * 34)
print(f'  RECORD CHECK  -  {label}')
print('=' * 34)
print(f'  Used      :  {value}')
print(f'  Total     :  {limit}')
print(f'  Status    :  {status}')
print('=' * 34)






#TYPICAL

# =================================================================== FUNCTIONS
def status_of(percent):
    if percent >= 100:
        return 'OVER LIMIT'
    elif percent >= 90:
        return 'WARNING'
    else:
        return 'OK'

def check(value,limit):
    difference = limit - value 
    percent = (value/limit) * 100
    return difference, percent
# ==================================================================== INPUT
label = input('enter the record name :')
value = float(input('enter the used value :'))
limit = float(input('enter the total value :'))
# ================================================================== PROCESS
difference, percent = check(value, limit)
status = status_of(percent)
# =================================================================== OUTPUT
print('=' * 34)
print(f'  RECORD CHECK  -  {label}')
print('=' * 34)
print(f'  Used      :  {value:>10.2f}')
print(f'  Total     :  {limit:>10.2f}')
print(f'  Free      :  {difference:>10.2f}')
print(f'  Percent   :  {percent:>10.2f}')
print(f'  Status    :  {status}')
print('=' * 34)







#EXCELLENT

# =================================================================== FUNCTIONS
def status_of(percent):
    if percent >= 100:
        return 'OVER LIMIT'
    elif percent >= 90:
        return 'WARNING'
    else:
        return 'OK'

def check(value,limit):
    difference = limit - value 
    percent = (value/limit) * 100
    return difference, percent

def print_report(label,value,limit,difference,percent,status):
    print('=' * 34)
    print(f'  RECORD CHECK  -  {label}')
    print('=' * 34)
    print(f'  Used      :  {value:>10.2f}')
    print(f'  Total     :  {limit:>10.2f}')
    print(f'  Free      :  {difference:>10.2f}')
    print(f'  Percent   :  {percent:>10.2f}')
    print(f'  Status    :  {status}')
    print('=' * 34)

# ================================================================== PROCESS
count = 0

while True:
    label = input("Enter record name (quit to stop): ")

    if label == "quit":
        break

# ==================================================================== INPUT
    value = float(input("Enter used value: "))
    limit = float(input("Enter total value: "))
# ================================================================== PROCESS

    difference, percent = check(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        count += 1
# =================================================================== OUTPUT
print('over limit records :  ', count)







'''
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# your function(s) go here


# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = ""      # replace with an input() call
value = 0.0     # replace with an input() call, converted
limit = 0.0     # replace with an input() call, converted


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.

difference = 0.0   # replace with your code
percent = 0.0       # replace with your code
status = ""          # replace with your code


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
'''