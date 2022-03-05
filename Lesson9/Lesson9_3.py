class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def set_coord(self, x, y):
        self.x = x
        self.y = y


"""
>>> import Lesson9_3
>>> Lesson9_3.Point(12,15)
<Lesson9_3.Point object at 0x7f47d0c15a90>
>>> p = Lesson9_3.Point(12,15)
>>> p.get_length()
19.209372712298546
>>> dir(p)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_length', 'set_coord', 'x', 'y']
>>> getattr(p, "set_coord")(1,2)
>>> getattr(p, "get_length")()
2.23606797749979
"""


def some_check(s):
    if s == "asdfasdfasd":
        return True
    return False

"""
>>> Lesson9_3.some_check("asdfasd")
False
>>> dir(Lesson9_3.some_check)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> print(Lesson9_3.some_check.__code__)
<code object some_check at 0x7f03cb5469d0, file "/home/kali/PycharmProjects/pythonProject1/Lesson9/Lesson9_3.py", line 29>
>>> print(Lesson9_3.some_check.__code__.co_code)
bite-code
>>> import dis
>>> dis.dis(Lesson9_3.some_check.__code__.co_code)
          0 LOAD_FAST                0 (0)
          2 LOAD_CONST               1 (1)
          4 COMPARE_OP               2 (==)
          6 POP_JUMP_IF_FALSE       12
          8 LOAD_CONST               2 (2)
         10 RETURN_VALUE
    >>   12 LOAD_CONST               3 (3)
         14 RETURN_VALUE
>>> print(Lesson9_3.some_check.__code__.co_consts)
(None, 'asdfasdfasd', True, False)
>>> print(Lesson9_3.some_check.__code__.co_filename)
/home/kali/PycharmProjects/pythonProject1/Lesson9/Lesson9_3.py
>>> print(Lesson9_3.some_check.__code__.co_varnames)
('s',)
"""