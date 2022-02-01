import os
import pandas as pd

cwd = os.path.abspath('')
files = os.listdir(cwd)
files.sort()

df = pd.DataFrame()
for file in files:
    if file.endswith('.xls'):
        (xls, ) = pd.read_html(file)
        df = df.append(xls, ignore_index=True) 
df.to_excel('tse.xlsx')