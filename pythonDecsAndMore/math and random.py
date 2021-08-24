import math
import random

#help(math)

value = 4.35

print(math.floor(value))
print(math.ceil(value))

print(math.log(math.e))
print(math.log(100, 10))
print(math.sin(10))
print(math.degrees(math.pi / 2))
print(math.radians(180))

print("____________")

print(random.randint(0, 100))

list = list(range(0, 20))
choices = random.choices(population=list, k=10000)
print(choices)
samples = random.sample(population=list, k=10)
print(samples)

print("_______-")
random.shuffle()
random.uniform(a=0, b=100)