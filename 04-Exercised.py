""" Exercises
1. Print a box like the one below"""
print('******************')
print('******************')
print('******************')
print('******************')

""" 2. Print a box like the one below."""
for rows in range(5):
    for columns in range(5):
        if (rows == 0 or rows == 5-1 or columns == 0 or columns == 5-1):
            print("*" , end="  ")

        else:
            print(" ", end="  ")

    print()

""" 3.a Print a triangle like the one below."""

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")

"""3.b Print a triangle like the one below.
*
**
***
****    """


for rows in range (5):
    for colums in range(rows):
        print("*", end=" ")

    print()



