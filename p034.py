content="""
    白日依山18267219234，黄河34567345678934567.
    玉琼12345，更上17352637846
"""
import re
pattern=r"(1[3-9])\d{9}"

print(re.sub(pattern,r"\1############",content))