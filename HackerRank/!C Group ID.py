"""
有一个500w的数据，三列id（用户id，身份id啥之类的），只要有一种id相同的就可以看成是一个人，最后需要对每行数据输出一个标签，相同的人标签要是一个。
例如：

         a        b         c          label
0        1        33        555        0
1        1        44        666        0
2        2        44        777        0
3        3        55        777        0
4        3        66        888        0
5        4        77        999        1
"""

import pandas as pd

a = [1, 1, 2, 3, 3, 4, 5]
b = [33, 44, 44, 55, 66, 77, 33]
c = [555, 666, 777, 777, 888, 999, 888]
df = pd.DataFrame(list(zip(a, b, c)), columns=['a', 'b', 'c'])
print(df)

df['a'].sort()

a_dict = df.groupby('a').indices.values()
b_dict = df.groupby('b').indices.values()
c_dict = df.groupby('c').indices.values()
print(a_dict, b_dict, c_dict)

test1 = {1, 2}
test2 = {2, 3}
test3 = test1.union(test2)
print(test3)

final_item = []
for a_item in a_dict:
    for b_item in b_dict:
        final_item.append(set(a_item).union(set(b_item)))

print(final_item)













