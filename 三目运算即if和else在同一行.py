# PS:问题没有解决，注意注意注意

# 三目运算,也是if和else写一行上
# 格式为：True_statements if expression else False_statements
# 三目运算的规则是：先对逻辑表达式 expression 求值，如果逻辑表达式返回 True，则执行并返回 True_statements 的值；如果逻辑表达式返回 False，则执行并返回 False_statements 的值

a = 2
b = 3

# 例子一
str = "a小于b" if a<b else "a大于b"
print(str)
# 输出
# a小于b

# 三目运算中允许在True_statements和False_statements中写入多条语句
# 有两种写入方式
# 方式一：多条语句以英文逗号隔开：每条语句都会执行，程序返回多条语句的返回值组成的元组。
# 方式二：多条语句以英文分号隔开：每条语句都会执行，程序只返回第一条语句的返回值。

# 例子二
x=20,'a大于b' if a > b else "a不大于b",print("cceshiushishishsi")
print(x)
# 输出
# cceshiushishishsi
# (20, 'a不大于b', None)
# None是因为print的返回值是None
# 问题：为什么20也输出出来了？

# 我的理解：
# 这里要注意程序的执行顺序，x = 20写在最开始就相当于把式子本身拆成了两部分x = 20 和 'a大于b' if a > b else  "a不大于b",print("cceshiushishishsi")
# x = 20,     这个语句本身会把 x当成tuple元组
# 希望之后能查到具体原因

# 例子三
x=(20,'a大于b') if a > b else "a不大于b",print("cceshiushishishsi")
# 输出
# cceshiushishishsi
# ('a不大于b', None)
# None是因为print()函数没有返回值

# 例子四
hhh=20,'aaaaa'
print(hhh)
# 输出
# (20, 'aaaaa')

# 例子五
st = print("aaaaaa"); x = 20 if a > b else  "a不大于b"
print(st)
print(x)
# 输出
# aaaaaa
# None
# a不大于b

# 问题：为什么这个会输出一个aaaaaa，而a>b的条件不成立，会走入else里面？
# 问题：为什么st输出为None？
# 问题：为什么x会输出a不大于b？因为x=20这个条件，只有在a>b这个条件成立的情况下，才会执行。条件不成立的时候走到后面"a不大于b"。但是为什么x的值会输出？

# 例子六
x = 20;st = print("aaaaaa") if a < b else  "a不大于b"
print(x)
print(st)
# 输出
# aaaaaa
# 20
# None
