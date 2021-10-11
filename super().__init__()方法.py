>>> class baba(object):
...     def __init__(self):
...         self.name = "father"
...     def print_name(self):
...         print(self.name)
... 
>>> f1 = baba()
>>> f1.print_name()
father
>>> class haizi(baba):
...     def __init__(self):
...         print("wo shi hai zi")
...     def print_name(self):
...         print("haizi")
...     def print_name_2(self):
...         print("haizi2")
... 
>>> c1 = haizi()
wo shi hai zi
>>> c1.print_name()
haizi
>>> c1.print_name_2()
haizi2
>>> class child(baba):
...     def __init__():
...         print("I am a child")
... 
>>> child1 = child()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() takes 0 positional arguments but 1 was given
>>> class child(baba):
...     def __init__(self):
...         print("I am a child")
... 
>>> child1 = child()
I am a child
>>> child1.print_name()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in print_name
AttributeError: 'child' object has no attribute 'name'
>>> 
