import re
jokerfinder = r".*[J]\0{0,}.*"
test = "DJSJE"
print(str(re.search(jokerfinder, test)))