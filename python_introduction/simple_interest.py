#SIMPLE INTEREST CALCULATOR

#Defining three(3) variables with values
principal = int(1000)
rate = float(0.05)
time = int(3)

P = principal
R = rate
T = time 

#Calculating simple interest
interest = (P * R * T)
#(int(principal) * float(rate) * int(time))
print("The simple interest is: " + str(interest))