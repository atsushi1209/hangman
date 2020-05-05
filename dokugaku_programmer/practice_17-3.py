import re


line = "The ghost that says boo haunts th loo"


match = re.findall(".oo", line)

print(match)
