#Author: 崔小葵
# Date: 2020-12-15 00:40:04
# Last Modified by:   崔小葵
# Last Modified time: 2020-12-15 00:40:04
while True:
    print('Who are you?')
    name = input()
    if name != 'Cui Lei':
        continue
    print('Hello, Cui Lei. what is the password? (It is a num.)')
    password = input()
    if password == '567902':
        break
print("Access granted.")
