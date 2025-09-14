monthly_income = input("Enter your monthly income: ")
total_monthly_expenses = input("Enter your total monthly expenses: ")
annual_interest_rate = 0.05

#calculate monthly savings
monthly_savings = int(monthly_income) - int(total_monthly_expenses)


#calculate annual savings
project_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * int(annual_interest_rate))

print("Your monthly savings are: " + "$"+str(monthly_savings)+".")
print("Projected savings after one year, with interest, is: " + "$"+str(project_annual_savings)+".")