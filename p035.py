content="""
    白日依山2021/05/26，黄河2021.05.27。
    玉琼05-28-2020，更上5/29/2020。
"""

import re
content=re.sub(r"(\d{4})/(\d{2})/(\d{2})",r"\1-\2-\3",content)
print(content)
content=re.sub(r"(\d{4})\.(\d{2})\.(\d{2})",r"\1-\2-\3",content)
print(content)
content=re.sub(r"(\d{2})-(\d{2})-(\d{4})",r"\3-\2-\1",content)
print(content)
content=re.sub(r"(\d{1})/(\d{2})/(\d{4})",r"\3-\2-0\1",content)
print(content)