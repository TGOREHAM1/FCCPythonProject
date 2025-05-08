def cube():
    while True:
        num = input("Input a number to cube: ")
        try:
            num_float = float(num)
            result = num_float ** 3
            print("Result of " + num + " cubed: " + str(result))
            break
        except ValueError:
            print("That's not a number. Try again.")

cube()
