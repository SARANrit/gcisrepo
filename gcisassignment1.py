#Name: Saransaai , UID = 434000016 

#Creating the function
def triangle_type_checker(length1, length2, length3):
    """This function is used to check the type of a triangle whether it is scalene, equilateral or iscoceles, it takes the 3 lengths of triangle as the parameter in function defenition and take 3 arguments in function call, it returns the type in a string"""
    #Checking Condition for equilateral triangle
    if length1 == length2 == length3:
        return "The triange is a equilateral triangle"
    # Checking Condition for iscoceles triangle
    elif length1 == length2 or length2 == length3 or length1 == length3:
        return "The triangle is an iscoceles triangle"
    # Checking Condition for scalene triangle
    else:
        return "The tringle is a scalene triangle"

#Creating main function
def main():
    """Main function takes asks the user for the input and uses triangle_type_checker function to check the type of triangle"""
    length1 = float(input("Enter length of first side of triangle: "))
    length2 = float(input("Enter the length of second side of triangle: "))
    length3 = float(input("Enter the length of third side of triangle: "))
    type = triangle_type_checker(length1, length2, length3) #Calling triangle type checker

    print(type)

#calling main function
main()
