motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop() #function.pop()在列表中删除最后一个元素，将数组看作一个栈表
print(motorcycles)

first_owned = motorcycles.pop(0)
print('The first motorcycle I owened was a ' + first_owned.title() + '.') #function.pop(place)弹出栈表中在place上的元素