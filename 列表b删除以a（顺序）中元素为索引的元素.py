# Author:Y
# 列表b删除以a中元素为索引的元素,a为顺序不重复

a = [0,1,3]
b = ["a","b","c","d","e","f"]
count = 0

for i in range(len(a)):
    del b[a[i]-count]
    count+=1
print(b)
