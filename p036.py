import re
with open('./datas/word.txt', 'r') as fin:
    content=fin.read()

# print(content.split())

words=re.split(r'[\s.()-?]+',content)

import pandas as pd
print(pd.Series(words).value_counts()[:20])