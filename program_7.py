# check the number is palindrome number or not 
number = ("Enter your number")
number = int(number)
r_number = int(str(number)[::-1])
if number == r_number:
    print("Given number is palindrome number")
else:
    print("Given number is not palindrome number")