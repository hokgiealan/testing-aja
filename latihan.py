# def sum67(nums):
#   total = 0
#   ignoreSection = False #kondisi tidak diabaikan
  
#   for i in nums:
#     if i == 6:
#       ignoreSection = True #kondisi diabaikan
#     elif i == 7 and ignoreSection:
#       ignoreSection = False
#     elif not ignoreSection:
#       total = total + i
      
#   return total

# nums = [66,4,12,23,50,-10,-7]
# sorting = sorted(nums)
# sorting.pop()

# print(sorted(nums))

# print(5//2)




# def centered_average(nums):
#   sorting = sorted(nums)
#   sorting.pop(0)
#   sorting.pop(-1)

#   print(sorting)
  
#   if len(sorting) % 2 != 0:
#     indexTengah = len(sorting)//2
#     value = sorting[indexTengah]
#     return value
#   else :
#     x = len(sorting)//2-1
#     y = len(sorting)//2
#     value = (sorting[x]+sorting[y])/2
#     return value


# jawaban = centered_average([1000, 0, 1, 99])

# print(jawaban)

# char = 'sdsadsadsa'

# for i in range(len(char)):
#     print(i)
# def least_difference(a, b, c):
#     """Return the smallest difference between any two numbers
#     among a, b and c.
#     """
#     diff1 = abs(a - b)
#     diff2 = abs(b - c)
#     diff3 = abs(a - c)
#     min(diff1, diff2, diff3)
    
# print(
#     least_difference(1, 10, 100),
#     least_difference(1, 10, 10),
#     least_difference(5, 6, 7),
# )

# def least_difference(a, b, c):
#     diff1 = abs(a - b)
#     diff2 = abs(b - c)
#     diff3 = abs(a - c)
#     return min(diff1, diff2, diff3)
    
# print(
#     least_difference(1, 10, 100),
#     least_difference(1, 10, 10),
#     least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
# )

# print(1, 2, 3, sep=' *() ')

# def mult_by_five(x):
#     return 5 * x

# def call(fn, arg):
#     """Call fn on arg"""
#     return fn(arg)

# def squared_call(fn, arg):
#     """Call fn on the result of calling fn on arg"""
#     return fn(fn(arg))

# print(
#     call(mult_by_five, 2),
#     squared_call(mult_by_five, 1), 
#     sep='\n', # '\n' is the newline character - it starts a new line
# )

# def kali(x):
#     return x * 10

# print(min(100,20,5, key=kali))


# def dikali_sepuluh(x, y, z):
#     return 10 ** x / y * z

# def pemanggilan(fn, *args):
#     return fn(*args)


# print(pemanggilan(dikali_sepuluh, 2, 5, 8))

# actual = not False
# print(actual)

# check = False or False
# print(check)

# def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
#     # Don't change this code. Our goal is just to find the bug, not fix it!
#     return have_umbrella or (rain_level < 5 and have_hood) or ((not rain_level > 0) and is_workday)

# have_umbrella = False
# rain_level = 0.0
# have_hood = False
# is_workday = False



# # Check what the function returns given the current values of the variables above
# actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
# print(actual)

# total_candies = 5
# print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")

# Contoh 1
# a = False
# b = False
# c = False
# result = a or b or c
# print(result)  # Output: True

# alphabet = [1,2,3][1:]

# alphabet[0], alphabet[-1] = alphabet[-1], alphabet[0]

# print(alphabet)
# arrivals = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']




# print(len(arrivals) - 1)
# print(b)

# def double_char(str):
#     x = 0
#     y = 0
#     cat = "cat"
#     dog = "dog"

#     for i in range(len(str)-1):
#         checking = str[i:i+3]
#         if checking == cat:
#             x += 1
#         elif checking == dog:
#             y += 1
    
#     if x == y:
#         return True
#     return False 

# def count_code(str):
#     x = 0
#     target = "code"
#     for i in range(len(str)-1):
#         checking = str[i:i+4]
#         if target == checking:
#             x += 1
#     return x


        

# a = count_code("code")
# print(a)

# x = (2,3,4,5,5,6,4,4)
# y = 1
# for i in x:
#     y = y ** i
# y

# print(y)

# def romanToInt(s):
#     roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
#     hasil = 0
#     i = 0
#     while i < len(s):
#         if i == len(s) - 1 or roman[s[i]] >= roman[s[i+1]]:
#             hasil += roman[s[i]]
#         else:
#             hasil += (roman[s[i+1]] - roman[s[i]])
#             i += 1
#         i += 1
#     return hasil

# angka = romanToInt("CMXCIX")
# print(angka)  # Output: 1994

import numpy

rolls = numpy.random.randint(2)
print(rolls)






