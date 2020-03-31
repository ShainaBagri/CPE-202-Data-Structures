# int -> string
# Given integer (base 10), returns string representation of integer converted to base b
def convert(num, b):

    #Base case where given number in base 10 is 0
    if num==0:
        return ""

    #If base b is more than 10, adds the appropriate letters
    if num%b>9:
        return convert(num//b, b) + str(chr(55+num%b))

    #Recurses through divison and remainder, converting from base 10 to base b
    return convert(num//b, b) + str(num%b)
