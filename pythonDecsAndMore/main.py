

def hello(name='John'):
    print('the hello() function has been executed')

    def greet():
        return '\t this is the greet() func inside hello!'

    def welcome():
        return '\t This is welcome() inside hello'

    print("im going to return a function: ")

    if name == 'John':
        return greet
    else:
        return welcome

new_func = hello('John')

def cool():

    def super_cool():
        return 'I am very cool'

    return super_cool

another_func = cool()

def hello():
    return 'Hi John'

def other(another_def_func):
    print('Other code runs here!')
    print(some_def_func())

other(hello)

def new_decorator(original_func):

    def wrap_func():
        print('some extra code, before the original function')

        original_func()

        print('some extra code, after the original function')

    return wrap_func()

func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)

decorated_func()