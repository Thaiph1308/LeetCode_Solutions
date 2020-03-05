array = 510
def make_smallest(num):
    digits = sorted([int(digit) for digit in str(num)])
    print(digits)
    for idx,value in enumerate(digits):
        if (value != 0):
            print(value,idx)
            digits[0] , digits[idx] = digits[idx] , digits[0]
            break
    digits =int(''.join(str(x) for x in digits))
    print(digits)
make_smallest(array)
