"""
RECORD CHECK  -  my version
===========================

Name  :  Alisha Shaheen
Lane  :  AI      
Date  :  6/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


# ==================================================================== LOAD
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("records_sample.csv") 

# ==================================================================== PROCESS
df['percent'] = (df['value'] / df['limit']) * 100
df['status'] = df['percent'].apply(lambda x: "OVER LIMIT" if x > 100 else "WARNING" if x >= 90 else "OK")

# =================================================================OUTPUT
print('Dataframe:')
print (df)
print('='*50)
print ("Dataframe after Filtering: ")
print(df[df['status' ] != 'OK'])
print('='*50)
grouped = df.groupby('status')['status'].size()
print (grouped)
df.to_csv('my_records.csv', index = False)
grouped.plot(kind='bar',title = 'Count of Status' ,color = 'blue')

plt.xlabel('Status')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# ================================================================== OUTPUT

