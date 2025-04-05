#1. Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string. Print the result. Try to identify the representation used.
#CODE:
def format_string(num, representation):
    # Using  format function to apply the representation
    formatted_string = "{:o}".format(num)  # 'o' is for octal representation
    return formatted_string
# Calling  function with 145 and 'o' as arguments         output: Simple Interest for 3 years is: 150.0
result = format_string(145, 'o')
print(result)
