# === OLD LIST: ===
# friends = ["Aleks", "Sam", "Pete", "Noone else"]
# friends.sort() <--- Sorts alphabetical!
# print(friends)

lucky_numbers = [49, 8, 27, 16, 56, 42]
print("The winning lottery numbers are: " + str(lucky_numbers))
missing_number = int(input("What number did I forget? "))
lucky_numbers.append(missing_number)
print("The winning lottery numbers are actually: " + str(lucky_numbers))
lucky_numbers.insert(0, int(input("Oops, what should have been first? ")))
print("The winning lottery numbers are actually: " + str(lucky_numbers))
while True:
    remove_num = input("Ok, one number was wrong... which one? ")
    try:
        selected_num = int(remove_num)
        if selected_num in lucky_numbers:
            lucky_numbers.remove(selected_num)
            print("Thanks... For the final time, the winning lottery numbers are actually: " + str(lucky_numbers))
            break
        else:
            print("That wasn't one of the numbers in the list. Try again.")
    except ValueError:
        print("That wasn't one of the numbers in the list. Try again.")
last_num = lucky_numbers[-1]
lucky_numbers.pop()
print("I've decided I don't like the last number, " + str(last_num) + ". Get POPPED son. The REAL winning lottery numbers are: " + str(lucky_numbers) + " (until I decide to change them again!)")
lucky_numbers.sort()
print("It looks nicer in ascending order: " + str(lucky_numbers))