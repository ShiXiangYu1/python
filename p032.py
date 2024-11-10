import re
def check_password(password):
    if not 6<=len(password)<=20:
        return False,"Password must be6~20 characters"
    if not re.search(r'[a-z]',password):
        return False,"至少一个小写的字母"
    if not re.search(r'[A-Z]',password):
        return False,"至少一个小写的字母"
    if not re.search(r'[0-9]',password):
        return False,"至少一个1个的数字"
    if not re.search(r'[^0-9a-zA-Z]',password):
        return False,"至少一个1个的特殊字符"
    return True,None
print("Hello666World!",check_password("Hello666World!"))
print("ello666orld!",check_password("ello666orld!"))
print("HelloWorld!",check_password("HelloWorld!"))
print("Hello666World",check_password("Hello666World"))