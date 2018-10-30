# 1
long_phrase = input()
short_phrase = input()

if len(long_phrase) > len(short_phrase):
    print('True')
else:
    print('False')

# 2
text = input()
letter1 = "а"
letter2 = "и"

print(text.count(letter1))
print(text.count(letter2))

# 3
file = int(input("Введите вес файла: ")) / 1000000
print("Объем файла равен {}Mb".format(file))

# 4
import math

print(math.sin(0.523599))

# 5
print(0.1 + 0.2)

# 6
a = input()
b = input()

a, b = b, a
print(a)
print(b)

#7
num = input()
ten = 0
for n in range(0, len(num)):
    ten = ten + int(num[n]) * (2 ** int(len(num) - 1 - n))

print(ten)
