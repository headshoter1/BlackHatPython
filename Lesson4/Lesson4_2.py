
def foo(a):
    a[0] = 5
    return None
    # print("Hello, from foo")

my_list = [1, 2, 3]
print(my_list)
a = foo(my_list)

print (my_list)