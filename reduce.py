#reduce(fution,sequence)
from functools import reduce
array=reduce(lambda x,y: x+y, list(range(0,5)))
print(array)
print()
array=reduce(lambda x,y: y+x, 'abcde')
print(array)
