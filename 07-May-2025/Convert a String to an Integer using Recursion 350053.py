# Problem: Convert a String to an Integer using Recursion - https://www.geeksforgeeks.org/convert-a-string-to-an-integer-using-recursion/

def stringToIntHelper(str, index):
    if index == len(str):
        return 0

    # Convert current character to digit
    digit = int(str[index])

    # Recursively compute the rest of the number
    return digit * (10 ** (len(str) - index - 1)) + stringToIntHelper(str, index + 1)

# Wrapper function
def stringToInt(str):
    return stringToIntHelper(str, 0)

# Driver code
str_value = "1235"
print(stringToInt(str_value))