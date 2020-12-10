def fizzbuzz(x):
    r1 = "FizzBuzz"
    r2 = "Fizz"
    r3 = 'Buzz'
    if x%3 == 0 and x%5 == 0:
        return r1
    elif x%3 == 0 and not x%5 ==0:
        return r2
    elif x%5 ==0 and not x%3 ==0:
        return r3
    else:
        return x
