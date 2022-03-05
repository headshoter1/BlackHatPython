a = str(input("input number"))

def foo(num):
    return sum([int(x) for x in list(str(num))])



def my_func2(*args):
    print(args)

my_func2(1,3,5,6)

