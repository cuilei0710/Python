#Author: 崔小葵
#Date: 2020-12-16 01:31:04
#Last Modified by:   崔小葵
#Last Modified time: 2020-12-16 01:31:04
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop()  # function.pop()在列表中删除最后一个元素，将数组看作一个栈表
print(motorcycles)

first_owned = motorcycles.pop(0)
# function.pop(place)弹出栈表中在place上的元素
print('The first motorcycle I owened was a ' + first_owned.title() + '.')
