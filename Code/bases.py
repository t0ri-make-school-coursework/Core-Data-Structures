#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

def is_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def old_decode(digits, base):
    pass
    # Decode digits from binary (base 2)
    # if base == 2:
    #     accumulator = 0
    #     bit_place = len(digit_list) - 1      # holds place in bits, counts backwards
    #     for num in digit_list:
    #        if num == '1':
    #            accumulator += 2 ** bit_place
    #        bit_place -= 1
    
    #     return accumulator
    
    # Decode digits from hexadecimal (base 16)
    # if base == 16:
    #     accumulator = 0
    #     for num in digit_list:
    #         if is_number(num):
    #             accumulator += int(num)
    #         else:
    #             values = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    #             accumulator += int(values.get(num.upper()))
                
    #     return accumulator

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""

    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    
    # Decode digits from any base (2 up to 36)
    digit_list = list(digits)
    numbers = list(string.digits + string.ascii_lowercase)
    
    result = 0
    
    bit_place = len(digit_list) - 1
    for num in digit_list:
        value = numbers.index(num)
        result += value * (base ** bit_place)

        bit_place -= 1
    
    return result

def old_encode(number, base):
    pass
    # Encode number in binary (base 2)
    # if base == 2:
    #     result = list()
    #     bit_place = 7
    #     current_num = number

    #     while len(result) <= 7:
    #         fit = 2 ** bit_place
    #         if current_num - fit >= 0:
    #             current_num -= fit
    #             result.append('1')
    #         else:
    #             result.append('0')
            
    #         bit_place -= 1
        
    #     return ''.join(result)


    # while number >= base:
    # remainder = int(number % base)
    # quotient = int(number / base)
    # converted = numbers[remainder]
    # result.append(converted)
    # number = quotient

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    # If base 10, do nothing
    if base == 10:
        return number

    number = int(number)
    numbers = list(string.digits + string.ascii_lowercase)
    result = list()
    while number >= base:
        result.append(numbers[int(number % base)])
        number = int(number / base)
    
    result.append(numbers[number])
    result.reverse()
    return ''.join(result)


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # Convert digits from any base to any base (2 up to 36)
    if base1 == '10':
        return encode(digits, base2)
    else:
        num = decode(digits, base1)
        return encode(num, base2)
    
def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')

if __name__ == '__main__':
    main()
