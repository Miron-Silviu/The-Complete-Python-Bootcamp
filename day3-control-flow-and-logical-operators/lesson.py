

#CHALLENGE Even Odd number

# Write a program that works out whether if a given number is an odd or even number

# number = int(input("Which number do you want to check?"))
#
# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")


#CHALLENGE  Exercise BMI Calculator

# Write a program that interprets the Body Mass Index (BMI)
#based on a user's weight and height
#It should tell them the interpretation of their BMI based
#on the BMI value

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
#
#
# bmi = round(float(weight) / float(height )** 2)
# print(int(bmi))
#
# if bmi < 18.5:
#    print(f"Your bmi is {bmi},your are underweight.")
# elif bmi <25:
#     print(f"Your bmi is {bmi},your are normal weight.")
# elif bmi > 25:
#     print(f"Your bmi is {bmi},your are overweight.")
#
# elif bmi < 30:
#     print(f"Your bmi is {bmi},your are overweight.")
#
# elif bmi > 30:
#     print(f"Your bmi is {bmi},your are obese.")
# elif bmi < 35:
#     print(f"Your bmi is {bmi},your are obese.")
# elif bmi > 35:
#     print(f"Your bmi is {bmi},your are clinically obese.")
# else:
#     print(f"Your bmi is {bmi},your are clinically obese.")

# CHALLENGE Leap Year

# Write a program that works out whether if a given year is a lea year.
#A normal year has 365 days leap year have 366, with an extra day In
#February. The reason why we have leap year is really fascinating,



year = int(input("Enter your year: "))


if year % 4 != 0:
   print("Not a leap Year")
elif year % 100 != 0:
    print("Leap Year")
elif year % 400 !=0:
    print("Not leap Year")
else:
    print("Leap Year")




