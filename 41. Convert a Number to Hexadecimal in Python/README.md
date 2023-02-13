# Intuition
Use the `format()` method of string to convert the number to hexadecimal, and check for negative values as well.
 
# Approach
Use the `format()` method of string to convert the number to hexadecimal using the `"{0:x}"` number format for hexadecimal conversion, if `num` is greater than 0. If `num` is negative, use the 2's complement method to convert it into an unsigned integer using the formula `(2^32 + num)`. Return the converted value.

# Complexity
- Time complexity:


- Space complexity:
