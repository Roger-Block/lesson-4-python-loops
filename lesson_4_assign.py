#Lesson 4: Assignments | Python Loop Statements
#============================================

print("="*50)
print("\nLesson 4: Assignments | Python Loop Statements\n")
print("="*50)

print("\nThe Range Riddle")
print("Task 1\n\n")

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for index, day in enumerate(days_of_week):
    if index % 2 == 0:
        print(day,)
print("\n","="*50)

#============================================


print("\n2. Loop Condition Logic\nObjective: The aim of this assignment is to explore the importance of the loop condition in while loops. You will create loops with different conditions to see how they influence the behavior of the loop.\n\n")

print("\tTask 1: Loop Condition Exploration Write a while loop with a condition that will never be true (an infinite loop). Ask the user a question until their answer triggers a break statement.\n")

#Task 1

#!!!UNCOMMENT TO TEST!!!
# While True:
#     answer = input("Do you want to continue? (yes/no): ")
#     if answer.lower() == "no":
#         break



print("\tTask 2: Conditional Exit Create a while loop that will terminate after 5 iterations, and each iteration you print which iteration it is on.\n")

#Task 2

iteration = 1

while iteration <= 5:
    print(f"Iteration: {iteration}")
    iteration += 1

print("\n","="*50)

print("BONUS ROUND: \nRandom Choice Game Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not keep them playing until they guess correctly.")
pass