import pandas as pd

df1 = pd.DataFrame({"HPI": [80, 90, 70, 60],
                    "int Rate": [2, 3, 1, 2],
                    "IND GDP": [50, 45, 45, 70]
                    },
                   index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({"HPI": [80, 90, 70, 60],
                    "int Rate": [2, 3, 1, 2],
                    "IND GDP": [50, 45, 45, 70]
                    },
                   index=[2005, 2006, 2007, 2007])


'''
#merge = pd.merge(df1, df2)                          #merge same data
merge = pd.merge(df1, df2, on= "HPI")              #keeps only 'on' column common
print(merge)
'''

joined = df1.join(df2, how='left', lsuffix='_left', rsuffix='_right')

print(joined)
