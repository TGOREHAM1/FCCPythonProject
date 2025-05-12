while True:
    try:
        number = int(input("Enter a number: "))
        print(number)
        break
    except ValueError:
        print ("Invalid input.")
    except ZeroDivisionError:
        print("You can't divide by zero you dumb dummie.")