0b1 + 0b11 
# bitwise numbers from one to twelve
one = 0b1
two = 0b10
three = 0b11
four = 0b100    
five = 0b101
six = 0b110    
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

# Print out the decimal equivalent of the binary 11001001.
print( int('11001001', 2))

# chECK TO SEE IF the fourth bit is on
def check_bit4(input):
    mask = 0b1000
    desired = input & mask
    if desired > 0:
        return "on"
    else:
        return "off"

#use a bitmaks to turn the third bit from the right on
a = 0b10111011
mask = 0b100
d = a | mask


#use a biask to flip all the bits in a
a = 0b11101110
mask = 0b11111111
result = a ^ mask

def flip_bit(number, n):
    mask = (0b1 << (n-1))
    result = number ^ mask
    return bin(result)
