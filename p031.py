
content="""
    电磁阀的消防车GV你回家123456@qq.com重复VG不回你家
    重复VG不回你家模块cvbnc#vb.com就
    个python666@163com分割不能
    成功python_ant-666@sina.net侠盗飞车GV和,的消防车GV环境
"""

import re

pattern=re.compile(r"""
    [A-Za-z0-9_-]+
    @[A-Za-z0-9]+
    \.
    [A-Za-z]{2,4}
""",re.VERBOSE)

results=pattern.findall(content)
print(results)