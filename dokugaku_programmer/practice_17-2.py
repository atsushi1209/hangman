import re


line = "Arizona 479, 501, 870. California 209, 213, 650."

match = re.findall("\d", line)

print(match)
