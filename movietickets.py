while True:
    age = input("How old are you? ")
    try:
        age = int(age)
        if age >= 0:
            break
        else:
            print("It's not possible to be younger than 0 years old. Try again.")
    except ValueError:
        print("That's not a number. Try again.")

if age < 12:
    ticket_price = 5
    print("You're a child, your ticket price is $" + str(ticket_price))
elif 12 <= age <= 17:
    ticket_price = 7
    print("You're a teenager, your ticket price is $" + str(ticket_price))
elif 18 <= age:
    while True:
        student = input("Are you a student? Y/N: ")
        student_true = ("y", "Y", "yes", "Yes")
        student_false = ("n", "N", "no", "No")
        if student in student_true:
            is_student = True
            break
        elif student in student_false:
            is_student = False
            break
        else:
            print("That's not a valid answer. Try again.")
    if is_student:
        ticket_price = 8
        print(f"You're an adult and a student, your ticket price is ${ticket_price}")
    elif not is_student:
        ticket_price = 10
        print(f"You're an adult but not a student, your ticket price is ${ticket_price}")