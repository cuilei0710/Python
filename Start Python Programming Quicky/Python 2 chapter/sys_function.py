#Author: 崔小葵
# Date: 2020-12-16 15:35:50
# Last Modified by:   崔小葵
# Last Modified time: 2020-12-16 15:35:50
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
