## simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

# Get user input for the task details
Task = input("Enter your task: ")
Priority = input("Priority (high, medium, low): ")
Time_bound = input("Is it time-bound? (yes/no): ")

# Using a Match Case statement to react differently based on the task’s priority.
match task:
    case _ if priority.lower() == "high" and time_bound.lower() == "yes":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case _ if priority.lower() == "low" and time_bound.lower() == "no":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _ if priority.lower() == "high":
        print(f"Reminder: '{task}' is a high priority task. Treat it with urgency.")
    case _ if priority.lower() == "medium":
        print(f"Reminder: '{task}' is a medium priority task. Plan to complete it soon.")
    case _ if priority.lower() == "low":
        print(f"Reminder: '{task}' is a low priority task. You can do it when you have time.")
    
    case _:
        print("No specific reminders for this task.")

        
