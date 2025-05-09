# FCC lecture code:
#is_male = True
#is_tall = True

#if is_male or is_tall:
#    print("Male or tall or both")
#elif is_male and not(is_tall):
#    print("Male but not tall")
#elif not(is_male) and is_tall:
#    print("Not male but tall")
#else:
#    print("Not male or not tall or both")

# My 'more fun' code:
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

if age < 13:
    print("You're a child.")
elif 13 <= age <= 19:
    print("You're a teenager.")
elif 20 <= age:
    print("You're an adult.")


