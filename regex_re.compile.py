import re

p = re.compile('[a-e]')           # It is equivalent to (abcde)

print(p.findall('Aye, said Mr. Gibeson Stark'))