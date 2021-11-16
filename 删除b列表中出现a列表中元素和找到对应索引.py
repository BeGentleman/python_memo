# Author: Y
# 从列表b中删除a中出现的所有元素并统计索引

from collections import Counter

a = [1,2,99]
b = [1,1,1,2,2,5,7,98,99]

'''
nums = dict(Counter(b))

# 删除b中所有出现a的元素
for i in range(len(a)):
    if a[i] in b:
        for j in range(nums[a[i]]):
            b.remove(a[i])
            
print(b)
'''
# 找到b中所有出现a的索引
nums = dict(Counter(b))
index_list = []
index = -1

# 通过list.index()方法的__start参数，指定起始索引
for i in range(len(a)):
    if a[i] in b:
        for j in range(0, nums[a[i]]):
            index = b.index(a[i], index + 1)
            index_list.append(index)

print(index_list)
