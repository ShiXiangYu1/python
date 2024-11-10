content="""
    譬如有一次，我偶然在一本课外读物中看到一篇描写父爱的文章，
    作者是朱自清先生，题目叫《背影》。读了这篇文章后，
    我顿时有了一番“用语文的文字记录生活”的领悟，
    我深深地感受到了作者用语文文字对父爱的动人诠释。
    读着读着，仿佛朱自清先生亲自在向我讲述他父亲送他去车站的真实情景和当时他的内心感受。
    从中，使我真真切切地体会到了文字的魅力和语文的重要性。
"""

import jieba
import re
content=re.sub('[\s。》...，、]','',content)
word_list=jieba.cut(content)

print(list(word_list))