def print_formatted(number):
    # your code goes here
    width = len(Binary(number))
    if number > 0:
        for i in range(1,number+1):
            decimal = str(i)
            octal = Octal(i)
            hexadecimal = HexaDecimal(i)
            binary = Binary(i)

            print(decimal.rjust(width), octal.rjust(width), hexadecimal.rjust(width), binary.rjust(width))

def Binary(n):
    bin_val = ""

    while n != 0:
        rem = n % 2
        bin_val = str(rem) + bin_val
        n = n // 2
    
    return bin_val

def Octal(n):
    oct_val = ""

    while n != 0:
        rem = n % 8
        oct_val = str(rem) + oct_val
        n = n // 8
    
    return oct_val

def HexaDecimal(n):
    hexa_val = ""

    while n != 0:
        rem = n % 16
        rem1 = gethexachar(rem)
        hexa_val = str(rem1) + hexa_val
        n = n // 16
    
    return hexa_val

def gethexachar(hex_val):
    if hex_val < 10:
        return hex_val
    elif hex_val == 10:
        return 'A'
    elif hex_val == 11:
        return 'B'
    elif hex_val == 12:
        return 'C'
    elif hex_val == 13:
        return 'D'
    elif hex_val == 14:
        return 'E'
    elif hex_val == 15:
        return 'F'
            
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)