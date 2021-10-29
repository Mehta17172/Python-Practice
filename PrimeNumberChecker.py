my_numbers = []
for number in range(-10,10):
    my_numbers.append(number)


for number in my_numbers:
    if number >=2:
        divisors = []
        for divisor in range(2,number ):
            if number % divisor == 0:
                divisors.append(divisor)

        if len(divisors) == 0:
            print("{:d} is a prime number".format(number))
        else:
            print("{:d} is not a prime number because it has {:} divisors.".format(number, str(divisors)))
    else:
        print("{:d} is a not a prime number".format(number))
    



