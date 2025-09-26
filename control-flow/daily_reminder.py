## simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

# Get user input for the task details
task = input("Task: ")
time_bound = input("Time Bound: ")
priority = input("Priority (high/medium/low): ")

# task = input("Enter your task: ")
# priority = input("Priority (high, medium, low): ").lower()
# time_bound = input("Is it time-bound? (yes/no): ").lower()

# Using a Match Case statement to react differently based on the task’s priority.
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task and not time-bound.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that is time-bound.")
        else:
            print(f"Reminder: '{task}' is a medium priority task and not time-bound.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task that is time-bound.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("No specific reminders for this task.")

        
