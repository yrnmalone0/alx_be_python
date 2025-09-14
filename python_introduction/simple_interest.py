#SIMPLE INTEREST CALCULATOR

#Defining three(3) variables with values
principal = 1000
rate = 0.05
time = 3

P = int(principal)
R = float(rate)
T = int(time) 


#Calculating simple interest
interest = (P * R * T)

print("The simple interest is: " + str(interest))