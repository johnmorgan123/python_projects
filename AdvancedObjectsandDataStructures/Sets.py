
def p(string):
    print(string)

s = set()

s.add(1)
s.add(2)
p(s)

s.clear()
p(s)

s = {1, 2, 3, 4}

sc = s.copy()
s.add(4)

p(s.difference(sc))

s1 = {1, 2, 3}
s2 = [1, 4, 5]

s1.difference_update(s2)
p(s1)


set1 = {1, 2, 3}
set2 = {1, 2, 4}

p(set1.intersection(set2))

set1.intersection_update(set2)
p(set1)

new1 = {1, 2}
new2 = {1, 2, 4}
new3 = {5}

p(new1.isdisjoint(new2))
p(new1.isdisjoint(new3))

p(new1.issubset(new2))
p(new2.issuperset(new1))

p(new1.symmetric_difference(new2))

p(new1.union(new2))

new1.update(new2)
p(new1)