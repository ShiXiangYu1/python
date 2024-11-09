content="""
    白日依山18267219234，黄河34567345678934567.
    玉琼12345，更上17352637846
"""
import re
pattern=(r'1[3-9]\d{9}')

results=re.findall(pattern,content)

for result in results:
    print(result)