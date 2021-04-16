# Author: 崔小葵
# Date: 2020-12-28 00:06:18
# Last Modified by:   崔小葵
# Last Modified time: 2020-12-28 00:06:18
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# print(players[0:3])中指定索引0-3，这将输出分别为0、1和2的元素
# 实际上处理列表中部分元素---python称之为切片
# print(players[:4])如果你没有指定起始索引，python会自动从列表开头开始
# print(players[2:])如果你没有指定终止索引，python会自动从起始索引开始到列表末尾
# print(players[-3:])如果你要输出名单上最后三名队员的名字，负数索引返回离列表末尾相应距离的元素
