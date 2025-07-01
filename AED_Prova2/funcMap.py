def __sum (values):
   calc = 0
   for i in values:
      calc += i
   return calc

nums = [3, 2, 4], (8, 4, 3) , [2, 4, 6], (10, 5, 1)

result = map(__sum, nums)
print( list(result))