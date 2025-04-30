from random import choice

li = [23, 56, 12, 67, 23, 90, 12, 31, 54, 87, 83, 52, 81, 95, 59]
num = choice(li)
while (True):

    ch = input("Want to guess the number again !!! : A for 'yes' and B for 'no'\n")
    ch = ch.upper()
    if (ch == 'A'):
        print(li)
        n = int(input("guess the number from the given list : "))
        if n == num:
            print("Bravo....\n")
            print("You gussed it right.")
        else:
            print("Oops!!! You gussed it wrong....No worries!!!Better Luck, Next Time...")

    else:
        break
