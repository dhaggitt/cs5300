def check_sign(x: int):
    sign = ""
    if (x < 0):
        sign = "negative"
    elif (x > 0):
        sign = "positive"
    else:
        sign = "zero"
    return sign
""" This function checks if a number is positive, negative, or zero"""


def calc_prime(limit: int):
    count = 0
    number = 1
    primes = []
    while(count < limit):
        prime_flag = True
        for n in range(2, int(math.sqrt(number)) + 1):
            if number % n == 0:
                prime_flag = False
        if prime_flag:
            primes.append(number)
            count += 1
        number += 1
    return primes
""" This function will calculate the first n primes
    This is separated to maintain ability for refactoring """


def first_ten_prime():
    ten_primes = calc_prime(10)
    for p in ten_primes:
        print(p)
""" This function will print out the first 10 prime numbers """


def century_sum():
    LIMIT = 100
    number = 1
    total_sum = 0
    while(number <= LIMIT):
        total_sum += number
        number += 1
    return total_sum
""" This function will find the sum of all numbers (assuming whole)
    from 1 to 100 """


def main():

    # Checks the output of the check_sign function
    variables = [5, -5, 0, 1, -1]
    for x in variables:
        print(x, "is", check_sign(x))
    
    # Calls first ten prime function
    first_ten_prime()

    # Calls the century sum function
    print("The sum of numbers 1-100 (inclusive) is", century_sum())
""" Main declared for debugging """


if __name__ == "__main__":
    main()