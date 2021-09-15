int_1 = int(input("Set the first digit of the lock: "))
print("first digit:", int_1)
int_2 = int(input("Set the second digit of the lock: "))
print("second digit:", int_2)
int_3 = int(input("Set the third digit of the lock: "))
print("third digit:", int_3)

lock_combination = int_1*100 + int_2*10 + int_3
print("You have entered", lock_combination)
print("The password has been saved")
lock_guess = int(input("Please enter a 3 digit combination "))

max_guess_number = 3
guesses = 0

while lock_guess != lock_combination and guesses <= max_guess_number:
    print("You have entered", lock_guess)
    print("Wrong combination!")
    if lock_guess < lock_combination:
        print("The lock combination is bigger")
    elif lock_guess > lock_combination:
        print("The lock combination is smaller")
    guesses += 1
    print(f"You have {max_guess_number-guesses} attempts remaining")
    lock_guess = int(input("Please enter a 3 digit combination "))
else:
    print("You have reached the maximum number of guesses")
    print("The lock will now undergo auto-destruction")

print("You have entered", lock_guess)
print("Lock opened successfully")
