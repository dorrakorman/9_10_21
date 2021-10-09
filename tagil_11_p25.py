#targil 11 page 25 num shalem find sfarot


num = int(input('enter num='))
a = num // 10
_sum = 1
while a > 0:
      _sum = _sum + 1
      a //= 10
print("sum_of_digitds",_sum)