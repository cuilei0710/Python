# Author: 崔小葵
# Date: 2020-12-27 23:49:41
# Last Modified by:   崔小葵
# Last Modified time: 2020-12-27 23:49:41
squares = []
print('Table #1: ')
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(squares)
print('Table #2: ')
print(squares)

# '**'表示乘方运算
# 如果想使代码更加简洁，我们可以这样写
# squares = []
# for value in range(1, 11):
#   squares.append(value**2)
#   print(squares)
