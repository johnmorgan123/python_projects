import re

text = "Weed Man's phone number is 657-635-587."
'phone' in text

pattern = 'phone'

print(re.search(pattern, text))

pattern = 'NOT IN TEXT'

re.search(pattern, text)

pattern = 'phone'

match = re.search(pattern, text)
print(match.span())
print(match.start())
print(match.end())

text2 = 'my phone once, my phone twice'
match = re.search('phone', text)
matches = re.findall('phone', text)
print(len(matches))

for match in re.findinter('phone', text):
    print(match.group())