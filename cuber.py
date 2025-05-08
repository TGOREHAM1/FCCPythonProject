def cube():
    while True:
        num = input("Input a number to cube: ")
        try:
            num_int = int(num)
            result = num_int*num_int*num_int
            print(str(result))
            break
        except ValueError:
            print("That's not a number. Try again.")

cube()
