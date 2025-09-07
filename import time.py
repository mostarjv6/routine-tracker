#  to do list

morning_routine = [
    "wack up ", "breakfast", "brush teeth", "get dressed", " go to school/ clg"
]

input = input("do you want to see your morning routine? (yes/no): ")
if input.lower() == "yes":
    print(morning_routine)

elif input.lower() == "no":
    print("Okay, have a great day!")
else:
    print("invalid input please enter yes or no")
