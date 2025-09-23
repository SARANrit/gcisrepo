#Defining Funtion for even or odd, positive or negative, square, cube
def even_odd(num):
    ''' Checks if the number is odd or even'''
    if num % 2 == 0:
        print(num,"is Even")
    else:
        print(num,"is Odd")

def pn(num):
    '''Checks if the number is positive or negative'''
    if num < 0:
        print(num, "is negative")
    elif num > 0:
        print(num, "is positive")
    else:
        print(num, "is 0")

def square(num):
    '''Squares the number'''
    print("The square is:", num ** 2)

def cube(num):
    '''Cubes the number'''
    print("The cube is: ", num ** 3)

#Creating a main function
def main():
    '''Contains the main block pf the program'''
    number = int(input("Enter a number: "))
    even_odd(number)                            #Calling all the function
    pn(number)
    square(number)
    cube(number)

main() 