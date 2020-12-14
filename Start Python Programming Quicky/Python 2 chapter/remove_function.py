#Author: 崔小葵
# Date: 2020-12-13 17:48:24
# Last Modified by:   崔小葵
# Last Modified time: 2020-12-13 17:48:24
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducats']
print(motorcycles)

motorcycles.remove('ducats')
print(motorcycles)

too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
