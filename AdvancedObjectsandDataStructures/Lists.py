
def p(string):
    print(string)

list = [1, 2, 3]

list.append(4)
p(list)

p(list.count(1))

p("_" * 12)

x = [1, 2, 3]
x.append([4, 5])
p(x)

p("_" * 12)

y = [1, 2, 3]
y.extend([4, 5])
p(y)

p("_" * 12)

p(list.index(2))
list.insert(2, 'inserted')
p(list)

p("_" * 12)

#cheese = list.pop(2)
#p(cheese)

list.remove('inserted')
p(list)

p("_" * 12)

list.reverse()
p(list)
list.reverse()

p("_" * 12)

cheese = [5, 7, 4, 8, 1, 3, 6, 10, 8, 2, 9]
cheese.sort()
p(cheese)
