#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()
print("Enter 999 to end input")
print("======================")


# Modify the program such that it asks the user to enter the number of subjects, 
# followed by score in each subject, and compute the average score accordingly.

# initialize variables
counter = 0
score_total = 0
test_score = 0
loop = True

inputs = int(input("Enter how many subjects there is: "))
while loop:
    test_score = int(input("Enter test score: "))
    if inputs >0:
        score_total += test_score
        counter += 1
        inputs -= 1
        if inputs == 0:
            loop = False

    elif test_score == 999:
        break
    else:
        print("Test score must be from 0 through 100.",
              "Score discarded. Try again.")

# calculate average score
average_score = round(score_total / counter)
                
# format and display the result
print("======================")
print(f"Total Score: {score_total}"
      f"\nAverage Score: {average_score}")
print()
print("Bye!")


