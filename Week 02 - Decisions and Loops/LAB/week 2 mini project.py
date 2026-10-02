"""
RECORD CHECK  -  my version
===========================

Name  :  Alisha Shaheen
Lane  :  AI 
Date  :  2/10/2026

Run it:   python template.py

"""



#THRESHOLD
# ==================================================================== 
record = input("Enter the record name: ")
used = int(input("Enter the used value: "))
total = int(input("Enter the total value: "))

if used > total :
    status = "OVER LIMIT"
else:
    status = "OK"

print('='*34)
print(f"  RECORD CHECK  -  {record}")
print('='*34)
print(' '*2 + f"Used: {used}")
print(' '*2 + f"Total: {total}")
print(' '*2 + f"Status: {status}")
print('='*34)
# ====================================================================






#TYPICAL
# ==================================================================== INPUT
record = input("Enter the record name: ")
used = float(input("Enter the used value: "))
total = float(input("Enter the total value: "))
# ================================================================== PROCESS
difference = total - used
percent = (used / total) * 100

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"
# =================================================================== OUTPUT
print('='*34)
print(f"  RECORD CHECK  -  {record}")
print('='*34)
print(' '*2 + f"Used      :  {used:>10.2f}")
print(' '*2 + f"Total     :  {total:>10.2f}")
print(' '*2 + f"Free      :  {difference:>10.2f}")
print(' '*2 + f"Percent   :  {percent:>10.2f}%")
print(' '*2 + f"Status    :  {status:>10}")
print('='*34)
# ====================================================================

  





#EXCELLENT
# ==================================================================== INPUT
count=0 
while True:
    record = input("Enter the record name: ")
    if record == "quit":
        break
    used = float(input("Enter the used value: "))
    total = float(input("Enter the total value: "))
# ================================================================== PROCESS
    difference = total - used
    percent = (used / total) * 100

    if percent >= 100:
        status = "OVER LIMIT"
        count+=1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
# =================================================================== OUTPUT
    print('='*34)
    print(f"  RECORD CHECK  -  {record}")
    print('='*34)
    print(' '*2 + f"Used      :  {used:>10.2f}")
    print(' '*2 + f"Total     :  {total:>10.2f}")
    print(' '*2 + f"Free      :  {difference:>10.2f}")
    print(' '*2 + f"Percent   :  {percent:>10.2f}%")
    print(' '*2 + f"Status    :  {status:>10}")
    print('='*34)

print(f"Total records OVER LIMIT: {count}")
# ==========================================================================

