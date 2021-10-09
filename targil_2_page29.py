# targil 2 page 29 - what will be the output 3 , 4 and 4 , 3?
num1 = int(input('enter num1='))
num2 = int(input('enter num2='))
p = 1
t = 0
while num2 > 0:
     m = 0
     t = num1
     while t > 0:
           m = m + p
           t = t - 1
     p = m
     num2 = num2 - 1
print(p)
# output 81 for inputs  3,4
# output 64 for inputs 4,3