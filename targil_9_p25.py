#targil 9 page 25 - find num sidori of the lowest

num = int(input('enter num ='))
i = 1
_index = 1
_val = 1000
while i <= 9:
    if num < _val:
        _val = num
        _index = i

    else:
     num = int(input('enter num ='))
     i = i + 1

print('_val', _val , "index",_index )
