import time
import timeit

def func_one(n):
    print([str(num) for num in range(n)])

func_one(10)
time.sleep(1)

def func_two(n):
    print(list(map(str,range(n))))

func_two(10)
time.sleep(1)
#31.347748279571533
start_time = time.time()
result = func_two(10000000)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)


stmt = '''
func_one(100)
'''

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup, number=100000))


stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(n):
    return list(map(str, range(n)))'''

print(timeit.timeit(stmt2, setup2, number=100000))


