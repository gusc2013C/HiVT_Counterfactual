import pandas as pd
import sys

df = pd.read_csv(sys.argv[1])
print(sys.argv[1])
print(df)
print(len(df))

for i in range(0,len(df)-2):
    df.loc[i+1,'X'] = (df.loc[i,'X'] + df.loc[i+1,'X']) / 2
    df.loc[i+1,'Y'] = (df.loc[i,'Y'] + df.loc[i+1,'Y']) / 2

df.to_csv("new_" + sys.argv[1], index = False)