#Problem 1: Convert 1024 to binary and hexadecimal representation

def p(string):
    print(string)

p(bin(1024))
p(hex(1024))

p("_" * 12)
#Problem 2: Round 5.23222 to two decimal places

answer = round(5.23222, 2)
p(answer)

p("_" * 12)
#Problem 3: Check if every letter in the string s is lower case

s = 'hello how are you Mary, are you feeling okay?'

p(s.islower())

p("_" * 12)
#Problem 4: How many times does the letter 'w' show up in the string below?

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
p(s.count('w'))

p("_" * 12)
#Problem 5: Find the elements in set1 that are not in set2:

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

p(set1.difference(set2))

p("_" * 12)
#Problem 6: Find all elements that are in either set:

p(set1.union(set2))

p("_" * 12)
#Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension.

d ={x:x**3 for x in range(5)}
p(d)

p("_" * 12)
#Problem 8: Reverse the list below:

list1 = [1,2,3,4]

list1.reverse()

p(list1)

p("_" * 12)
#Problem 9: Sort the list below:

list2 = [3,4,2,5,1]

list2.sort()

p(list2)
