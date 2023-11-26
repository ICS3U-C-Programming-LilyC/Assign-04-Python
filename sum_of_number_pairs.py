#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Nov/22/2023
# This program will generate all the positive 2 digit number pairs
# of the number chosen by the user.


def main():
    # Explaining my program to the user.
    print(
        "Welcome to my program in python. It will generate all the positive 2 digits number pairs that have a sum of a number of your choice between 20 and 100."
    )

    # Getting user number as a string.
    number_as_string = input("Please enter an integer of your choice: ")

    # Initiating try catch to catch any errors.
    try:
        # Converting the user's input variable from a string to an integer.
        number_as_integer = int(number_as_string)

        # If statement to verify that the number entered by the user is between the range 20 and 100.
        if number_as_integer >= 20 and number_as_integer <= 100:
            # Initializing counters.
            counter1 = 10
            counter2 = number_as_integer - counter1

            # First for loop which will increment counter1 (first number displayed).
            for counter1 in range(10, 101):
                # Second for loop (nested loop) which will increment counter2 (second number displayed).
                for counter2 in range(10, 101):
                    # If statement to see if both counter's added together equal the number the user inputs.
                    if counter1 + counter2 == number_as_integer:
                        print(
                            "{} + {} = {}".format(counter1, counter2, number_as_integer)
                        )
        # Else tell the user that their number is not within the range 20 to 100.
        else:
            print("This number is not within the range of numbers 20 to 100.")
    # Catching any errors.
    except:
        print("{} is an invalid input.".format(number_as_string))


if __name__ == "__main__":
    main()
