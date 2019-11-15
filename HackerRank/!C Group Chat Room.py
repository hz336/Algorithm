"""
1. 面试职位所在组的大boss，最开始聊了聊经历，然后出了一道题，内容如下：
有一个消息记录系统，每一条记录的形式如下：
sender ID, receiver ID, message, timestamp
然后如果是一个group chat，会有多条记录，然后sender是同一个人，receiver是group当中的每一个人，但是timestamp会稍有不同，要求寻找出所有的不重复的chat group
（两个人的一对一聊天也算一个group）。test case如下

1, 2, 'hey', 0
1, 5, 'hi', 1
1, 5, 'hello', 5
1, 2, 'hello', 5.0001
5, 1, 'bye', 6
5, 2, 'bye', 6.0002

结果是[(1,2), (1,5), (1,2,5)]
"""

import pandas as pd

sender_id = [5, 1, 1, 1, 1, 5, 4]
receiver_id = [1, 2, 5, 5, 2, 2, 7]
message = ['bye', 'hey', 'hi', 'hello', 'hello', 'bye', '?']
timestamp = [6, 0, 1, 5, 5.0001, 6.0002, 6.0001]

df = pd.DataFrame(list(zip(sender_id, receiver_id, message, timestamp)), columns=['sender', 'receiver', 'message', 'time'])
print(df)

df.sort_values(by=['time', 'sender'], inplace=True)
print(df)

df['time_prev'] = df.sort_values(by='time').groupby(['sender'])['time'].shift()
df['label'] = df.apply(lambda x: 1 if x['time'] - x['time_prev'] < 0.05 else 0, axis=1)






















