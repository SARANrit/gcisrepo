def tri(a, b, c,):
    try:
        if a + b > c or a + c > b or b + c > a:
            print("Its a triangle")

        else :
            print("Its not a triangle")
    except ValueError:
        print("One of the side length is invalid")

def main():
    side1 = float(input("Enter length 1: "))
    side2 = float(input("Enter length 2: "))
    side3 = float(input("Enter length 3: "))

    tri(side1, side2, side3)

main()