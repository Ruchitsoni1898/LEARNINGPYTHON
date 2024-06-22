import re

chars = "Hello Gujarat!1234"

count = re.sub("[w]+","",chars)
print(len(count))