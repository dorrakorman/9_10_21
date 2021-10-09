#targil 10 page 25  find right digit
 num = int(input('enter num='))
 a = num // 10
 b = 1
 while a > 0:
       b = a
       a //= 10
 print(b)
