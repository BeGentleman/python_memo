# *args会存放所有未命名的变量参数，args元组
# **kwargs会存放命名参数，即形如 key = value的参数,kwargsin字典

def add(a,b,*args,**kwargs):
    print("a=",a)
    print("b=",b)
    print("args=",args)
    print("kwargs=",kwargs)

add(1,2,3,4,5,6,m=7,n=8,p=9)
# 输出

# a= 1
# b= 2
# args= (3, 4, 5, 6)
# kwargs= {'m': 7, 'n': 8, 'p': 9}
# ------------------------------------------------------------

# 运算中 ** 代表乘方
# 2**3 会输出8，表示2的3次方
# *如果是字符串、列表、元组与一个整数N相乘，返回一个其所有元素重复N次的同类型对象，比如"str"*3将返回字符串"strstrstr"

s=(1,2)
print(s*3)
# 输出(1, 2, 1, 2, 1, 2)
