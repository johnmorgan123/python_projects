from collections import Counter, defaultdict

list = [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
print(Counter(list))

list2 = ['a','a',420,420,420]
print(Counter(list2))

insult = "Fuck you dirty chelsea pig fucker donkey raping shit eater horse fucker"
def count_insult():

    print(Counter(insult.lower().split()))

count_insult()

letters = 'aaaaaaaaaabbbbbbbcccccccccccddddddddd'
c = Counter(letters)
print(c.most_common())


