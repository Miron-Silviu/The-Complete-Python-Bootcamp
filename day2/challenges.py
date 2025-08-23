

# Write a program that adds the digits in a 2 digit number.e.g
# If the input was 35, then the output should be 3 + 5 = 8

two_digit_number=input("Type a two digit numbers: ")

# print(str(two_digit_number)[0])
# print(str(two_digit_number) [1])

first_str = int( two_digit_number[0] )
second_str = int( two_digit_number[1] )
mark = "+"
second_mark = "="
print(first_str,mark,second_str,second_mark,first_str + second_str)
