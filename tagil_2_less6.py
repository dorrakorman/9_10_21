# targil 2 less. 6 - intput 2  - find whos bigger, break
num1 = int(input('enter num1='))
num2 = int(input('enter num2='))
while num1 != 0 and num2 != 0:

      if num1 > num2:
          print('bigger',num1)
      else:

          print('bigger',num2)
      num1 = int(input('enter num1='))
      num2 = int(input('enter num2='))
      if (num1 or num2) == 0:
           break

print("break")
