import re

string = 'B A T T L E'
spaces = re.compile(r'\s+')
result = re.sub(spaces,'',string)
print(result)

