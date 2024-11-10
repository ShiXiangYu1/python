content="""
买了1斤黄瓜花了8元;
买了3斤葡萄花了13.5元;
买了5斤白菜花了5.4元;
"""

import re

for line in content.split("\n"):
    pattern=re.compile(r"(\d)斤(.*)花了(\d+(\.\d+)?)元")
    match=re.search(pattern,line)
    if match is not None:
        print(f"{match.group(1)}\t{match.group(2)}\t{match.group(3)}\n")
        # print(match.groups())