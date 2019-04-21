"""
This code compare each integer representation against lowercase and uppercase letters
then subtract or add 13 to shift characters
"""
def rot13(s):
    result = ""

    for x in s:  # Loop over every character in the string s.

        d = ord(x) # Convert the letter in the string to a number in the ascii table
        # d refers to the first later of the name valery .....number with ord  which refers to the returns and integer from the ascii table

        # Shift number back or forward checking in its lover case
        if d >= ord('a') and d <= ord('z'):
            if d > ord('m'): # if the first letter of the chosen name is greater than the (109)ASCII TABLE  M
                d -= 13 #  then it should take away 13 characters

            else: # if the character is less than M
                d += 13 # If the ascii character is less than M  it should add character unto it
        elif d >= ord('A') and d <= ord('Z'): # This is looking at the upper case
            if d > ord('M'): # if upper case D
                d -= 13 #
            else:
                d += 13

        # Append to result.
        result += chr(d)  #

    # Return transformation.
    return result

# Test method.
print(rot13("VaLeRY")) #
print(rot13(rot13("valery")))
