# Boolean Condition
"""
print(1==1)
print(1>5)
"""

# Comparison Operatar
# == equal to
# != not equal to
# > large to
# < smaill to
# >= large or equal to
# <= small or equal to

"""
print(1!=1)
print(1>5)
"""

# condition
"""fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
"""
"""
# Example 1 The following program will print Hello ten times:_A_Practical_Introduction_to_Python_Programming_Heinold 
for i in range(10):
    print('hello')  
    
"""

# Example 2 The program below asks the user for a number and prints its square, then asks for
# another number and prints its square, etc. It does this two times and then prints that the loop is
#done. p.12 _A_Practical_Introduction_to_Python_Programming_Heinold 
"""
for i in range(3):
    num = eval(input('Enter a number: '))
   print ('The square of your number is', num*num)
   print('The loop is now done.') 
"""

# Example 3 The program below will print A, then B, then it will alternate C’s and D’s five times
# and then finish with the letter E once._A_Practical_Introduction_to_Python_Programming_Heinold
"""
print('A')
print('B')
for i in range(5):
    print('C')
    print('D')
print('E')  
"""
# Example 4 If we wanted the above program to print five C’s followed by five D’s, instead of
# alternating C’s and D’s, we could do the following. p.12 _A_Practical_Introduction_to_Python_Programming_Heinold
"""
print('A')
print('B')
for i in range(5):
  print('C')
for i in range(5):
  print('D')
print('E')

"""
# Since the loop variable, i, gets increased by 1 each time through the loop, it can be used to keep
# track of where we are in the looping process. Consider the example below: p.13_A_Practical_Introduction_to_Python_Programming_Heinold
"""
for i in range(3):
  print(i+1, '-- Hello')
"""

# To get the list of values to go backwards, we can use a step of -1. For instance, range(5,0,-1)
# will produce the values 5, 4, 3, 2,1 in that order. (Note that the range function stops one short of the
# ending value 0). Here is an example program that counts down from 5 and then prints a message. p.14
# _A_Practical_Introduction_to_Python_Programming_Heinold

"""
for i in range(5,0,-1):
  print(i, end=' ')
print('Blast off!!')
"""

# #1 Effective Python 59 Specific Ways to Write Better Python@@@@#2
# p.53
"""
def log(message, values):
  if not values:
      print(message)
  else:
      values_str = ", ".join(str(x) for x in values)
      print("%s: %s" % (message, values_str))
log("My numbers are", [1, 2])
log("Hi there", [])
"""