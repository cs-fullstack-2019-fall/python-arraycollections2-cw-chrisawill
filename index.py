#
# ### Problem 1:
# Create code and define the variable below outside of any function. After you create the list variable write a function called ```stupid_array_tricks``` that takes an array as a parameter, and performs the functions listed below in the instructions.
#
# ```
# person_array = ["Kenn", "Kevin", "Erin", "Autumn"]
# ```
# a) Print the 2nd and 3rd elements of the person_array using a *range*
#  b) Print the last 2 elements of the person_array using a *range*
   # c) Insert the new element ```Chuck``` between the 2nd (```Kevin```) and 3rd (```Erin```) elements
# d) Take out the 2nd element (```Kevin```) from the list
#
person_array = ["Kenn", "Kevin", "Erin", "Autumn"]

def stupidArrayTricks(person_array):
   texas = person_array[2:3]
   print(texas)
   return texas
stupidArrayTricks(person_array)
#

# ### Problem 2:

# user = input("")
# while user != "q":
#     user = input("try again")





# ### Problem 3:
# Create a function that uses the data list below.
# ```
# ['GOOD_DATA',
# 'DECENT_DATA',
# 'BAD_DATA',
# 'DECENT_DATA',
# 'GOOD_DATA'
# 'BAD_DATA',
# 'GOOD_DATA',
# 'DECENT_DATA',
# 'BAD_DATA',
# 'GOOD_DATA']
# ```
#
# Write the code to do the following:
#     * Print the length of the original DATA list/array (ex. ```Starting length of data list is 10```)
# * Remove all ```BAD_DATA``` from the DATA list/array
#                                           * Print the length of the final DATA list/array (ex. ```Ending length of data list is 7```)
#
# myArray = ['GOOD_DATA', 'DECENT_DATA', 'BAD_DATA', 'DECENT_DATA', 'GOOD_DATA', 'BAD_DATA', 'GOOD_DATA', 'DECENT_DATA', 'BAD_DATA', 'GOOD_DATA']
#
# print(f"Starting length of the DATA list is {len(myArray)}")
# myArray.pop(2:5:8)

# ### Problem 4:

# score_list = [21, 14, 6, 8, 28, 42, 21]
# print(f"Your scores are {score_list}")
# # for eachNum in score_list:
# print(f"The sum of the score list is {sum(score_list)}.")
# print(f"The maximun score is {max(score_list)}")




# ### Challenge:
# Create a program that will let the User build a list words. Prompt the User for a word. Add the word the User enters and add it to the list. Allow the User to keep entering words until they enter 'x' to exit the program.
#
# Print the final word list prior to exiting the program.

