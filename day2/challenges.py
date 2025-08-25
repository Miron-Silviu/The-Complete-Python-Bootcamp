

# Write a program that adds the digits in a 2 digit number.e.g
# If the input was 35, then the output should be 3 + 5 = 8

# two_digit_number=input("Type a two digit numbers: ")

# print(str(two_digit_number)[0])
# print(str(two_digit_number) [1])

# first_str = int( two_digit_number[0] )
# second_str = int( two_digit_number[1] )
# mark = "+"
# second_mark = "="
# print(first_str,mark,second_str,second_mark,first_str + second_str)


# CHALLENGE BMI CALCULATOR
#
# Instructions
# Write a program that calculate the Body Mass Index(BMI)
#from a user's weight and height
#The BMI is a measure of some's weight taking into account
#their height. e.g. If a tall person and a short person both
#weight the same amount, the short person usually more overweight
#The BMI is calculated by dividing a person's weight (in kg) by
#the square of their heigh(in m)


# height = input ("Enter your heigh in m:")
# weight=input("Enter your weight in kg:  ")
#
# bmi = float(weight) / float(height )** 2
#
# print(int(bmi))

#CHALLENGE

#INSTRUCTIONS

#Create a program using maths and f-Strings that tells us how many day,weeks,
#and months we have left if we live until 90 years old
# It will take your current age as the input and output a message with our time
#left in this format .

# age=input("What is your current age?")
#
# final_age = 90
#
# months = 12
# weeks  = 52
# days = 365
#
# total_years = final_age - int(age)
# total_months = total_years * months
# total_weeks = total_years * weeks
# total_days = total_years *days
#
# message = f"You have {total_days} days, {total_weeks} weeks, and {total_months} months left."
# print(message)

# CHALLENGE

#INSTRUCTIONS

#Create a tip calculator

print("Welcome to tip calculator.")

total_bill = input("What was the total bill? $")
percentage_tip = input("What percentage tip would you like to give? 10,12,or 15 ?")
total_people = input("How many people to split the bill?")


tip = float(total_bill) * float(percentage_tip) / 100
total_tip_and_bill = float(total_bill) + tip
each_person_payment = total_tip_and_bill / int(total_people)
final_amount = round(each_person_payment, 2)
total ="{:.2f}".format(final_amount)
print(f"Each person should pay: {total}")