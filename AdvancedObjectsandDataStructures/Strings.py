
def p(string):
    print(string)

s = 'cheesy chunkz'

p(s.capitalize())
p(s.upper())
p("_" * 12)
p(s.count('c'))
p(s.find('u'))

p(s.center(50, '-'))

p(s.isalpha())
p(s.isascii())
p(s.isalnum())
p(s.islower())
p(s)
p('CHeESE'.isupper())

p(s.split('e'))
