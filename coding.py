print(ord('a'), ord('姜'))
print(chr(97) + chr(23004))

print('\u4e2d\u6587')

C = b'abc'
c = 'abc'
print(type(C), type(c))

x = 'ABC'.encode('ascii')
y = '姜博文'.encode('utf-8')
#x = '姜博文'.encode('ascii')   会报错！！因为ascii码中不包含中文
z = b'\xe5\xa7\x9c\xe5\x8d\x9a\xe6\x96\x87'.decode('utf-8')

print(x, y, z)

z = b'\xe5\xa7\x9c\xff\xe5\x8d\x9a\xa6\xe6\x96\x87'.decode('utf-8', errors='ignore')
print(z)

l = len(b'ABC')
print(l)

l = len('姜博文')
L = len(b'\xe5\xa7\x9c\xe5\x8d\x9a\xe6\x96\x87')
print(l, L)

l = len(y)
print(l)

print('%5s，你的最高分是%d，平均分是%.2f，超过了%d%%的同学！' % ('姜博文', 100, 98.5, 99))