import re

name = "My number  is 0697890\n"

digitcount = re.sub("[^0-9]","",name)
lettercount = re.sub("[^a-zA-Z]","",name)
spacecount = re.findall("[\n]", name)
print(len(digitcount))
print(len(lettercount))
print(len(spacecount))