#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()
print("Enter 5 test scores")
print("======================")

# get scores from the user
total_score = 0       # initialize the variable for accumulating scores
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))

# calculate average score
average_score = total_score / 5
             
# format and display the result
print("======================")
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score)
print()
print("Bye")


# Change the program such that it computes average (no rounding) 
# of exact five (instead of three) scores that a user enters.

#Q2: What happens if you remove the float() function?
#

