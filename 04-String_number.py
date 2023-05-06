# commments(註解)
print("Hello") #string 字串
print('hello') #string 字串

# Arithemtic operator 運算符號
print(7+7) # 加
print(7-7) # 減
print(7*7) # 乘
print(7/7) # 除
print(7%7) # 餘數
print(7**2) # 指數

# Floor division
x = 15
y = 2

print(x // y)

#the floor division // rounds the result down to the nearest whole number


""" The First Argument: expression
The first argument to eval() is called expression. 
Its a required argument that holds the string-based or compiled-code-based input to the function. 
When you call eval(), the content of expression is evaluated as a Python expression. 
Check out the following examples that use string-based input:"""

num = eval("2 ** 8") # 2指數 8 
print(num) # = 256

num1 = eval("1024+1024") # 1024 + 1024
print(num1) # = 2048

num2 = eval("sum([8,16,32])")
print(num2) # = 56

x = 100
num3 = eval("x * 2") # 100 * 2
print(num3) # =200


"""The input function is a simple way for your program to get information from people using your
program. Here is an example: """

name = input('Enter your name: ')
print('Hello, ', name)

# The basic structure is variable name = input(message to user)

""" The above works for getting text from the user. To get numbers from the user to use in calculations,
we need to do something extra. Here is an example: """

num = eval(input('Enter a number: '))
print('Your number squared:', num*num)

""" The eval function converts the text entered by the user into a number. One nice feature of this is
you can enter expressions, like 3*12+5, and eval will compute them for you. """




