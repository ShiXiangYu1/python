# content="李明喜欢韩梅梅，他俩早恋"
with open("./datas/鹿鼎记.txt") as fin:
    content=fin.read()
import jieba.posseg as posseg
words=[]
for word,flag in posseg.cut(content):
    if flag=="nr":
        # print(word,flag)
        words.append(word)

import pandas as pd
print(pd.Series(words).value_counts()[:20])