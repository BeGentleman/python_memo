# 产生原因
父类中的方法，没有在子类当中重写，就被使用了，就会报这个错误

举例子：
~~~python
>>> class baba(object):
...     def method(self):
...         raise NotImplementedError
... 
>>> class haizi(baba):
...     def method2(self):
...         print("wo shi hai zi")
... 
>>> a = haizi()
>>> a.method()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in method
NotImplementedError
>>> 
~~~

~~~python
>>> class baba(object):
...     def method(self):
...         raise NotImplementedError
... 
>>> class haizi(baba):
...     def method(self):
...         print("wo shi hai zi")
... 
>>> b = haizi()
>>> b.method()
wo shi hai zi
>>> 

~~~
