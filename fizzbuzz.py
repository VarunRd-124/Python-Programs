# Write a python program that prints the numbers from 1 to 100. 
# But for multiples of seven, print "Fizz" instead of the number, and for the multiples of three,
# print "Buzz". For numbers which are multiples of both three and seven, print "FizzBuzz".

for number in range(1, 101):
    if number % 3 == 0 and number % 7 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Buzz")
    elif number % 7 == 0:
        print("Fizz")
    else:
        print(number)