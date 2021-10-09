#targil 3 page 29
num = int(input('enter num='))

while num > 0:

      b = num
      a = num
      c = 0
      while b != 0:
           a = b % 10
           b = b // 10
           c += a
      print(c)
      num = int(input('enter num='))

print("finish")
