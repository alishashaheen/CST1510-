"""
RECORD CHECK  -  my version
===========================

Name  :  Alisha Shaheen
Lane  :  AI      (delete two)
Date  :  27/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


# THRESHOLD

hostname = input('enter host name :')
used = int(input('enter used gb :'))
total = int(input('enter total gb :'))

print('='*34)
print(' '*2,'RECORD CHECK','-',hostname)
print('='*34)
print(' '*2,'Used      :',used)
print(' '*2,'total     :',total)
print('='*34)



#TYPICAL

# ==================================================================== INPUT
hostname = input('enter host name :')
used = float(input('enter used gb :'))
total = float(input('enter total gb :'))
# ================================================================== PROCESS
differance = total- used 
percentage = (used/total)*100
# =================================================================== OUTPUT
print('='*34)
print(f'RECORD CHECK - {hostname}')
print('='*34)
print(f'used       :  {used:>10.2f}')
print(f'total      :  {total:>10.2f}')
print(f'differance      :  {differance:>10.2f}')
print(f'percentage      :  {percentage:>10.2f}')
print('='*34)



#EXCELLENT

# ==================================================================== INPUT
hostname = input('enter host name :')
used = float(input('enter used gb :'))
total = float(input('enter total gb :'))
# ================================================================== PROCESS
differance = total- used 
percentage = (used/total)*100
free_gb = total- used 
# =================================================================== OUTPUT
print('='*34)
print(f'RECORD CHECK - {hostname}')
print('='*34)
print(f'used       :  {used:>10.2f}')
print(f'total      :  {total:>10.2f}')
print(f'differance      :  {differance:>+10.2f}')
print(f'percentage      :  {percentage:>10.2f}')
print(f'free gb      :  {free_gb:>10.2f}')
print('='*34)

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
