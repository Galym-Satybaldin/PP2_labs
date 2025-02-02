input_str = input(" write down set of numbers separated by space")
numbers = [int(num) for num in input_str.split()]


def checker(numbers):
    prime_numbers = []
    for num in numbers:
        if num>1:
            is_prime = 1
            for i in range (2, int(num**0.5)+1):
                if num % i == 0:
                    is_prime = 0
                    break
                
            if is_prime:
                prime_numbers.append(num)
    return prime_numbers

                
prime_numbers = checker(numbers)

for num in prime_numbers:
    print (num)