#Author: 崔小葵
# Date: 2020-12-29 00:18:00
# Last Modified by:   崔小葵
# Last Modified time: 2020-12-29 00:18:00
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite food:")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

#friend_foods = my_foods
# 这样的做法是直接将my_foods赋给friends_foods，而不是将my_foods的副本存储在friend_foods
# 这种语法实际上让python将新变量friend_foods关联到包含在my_foods中的列表
