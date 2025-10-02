import datetime as dt

## Display the Current Date and Time

def display_current_datetime():
    current_date = dt.datetime.now()

    format_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ",format_datetime)

display_current_datetime()


## Calculate a Future Date

number_of_days = int(input("Enter the number of days to add to the current date: "))
current_time = dt.datetime.now()

def calculate_future_date():
    future_date = current_time + dt.timedelta(days=number_of_days)
    print("Future date: ", future_date.strftime("%Y-%m-%d"))

calculate_future_date()

