# x = "asdasd143"
# y = "SFSADF$#@WRWER32"
# print(x.isalnum())
# print(y.isalnum())

import re
print(bool(re.match('[A-Za-z0-9]+$','abdc1321'))) # Output: True
print(bool(re.match('[A-Za-z0-9]+$','xyz@123$'))) #