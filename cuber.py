def cube(num):
    num_int = int(num)
    cubed_num = num_int*num_int*num_int
    print("Cubed number: " + str(cubed_num))

cube(input("Input a number to cube: "))

def efficient_cube():
    while True:
        num = input("Input a number to EFFICIENTLY cube: ")
        try:
            num_int = int(num)
            result = num_int*num_int*num_int
            print(str(result))
            break
        except ValueError:
            print("That's not a number. Try again.")

efficient_cube()
