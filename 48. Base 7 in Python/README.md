# Intuition
Recursively floor divide the number by 7 and concatenate it with the remainder left when dividing it by 7.

# Approach
Check to see if the number is negative, and return "-" concatenated with the base 7 version of the negative of the number. (Double negative would make positive whose base 7 representation can be recursively calculated by calling the function, and the "-" sign would represent the negative part.) 
Next up, check if the number is less than 7 and if so just return the same number in a string format.
Finally, for the actual function logic. Recursively call the function on the value obtained when floor dividing the number by 7 (this gives the integral value obtained as the quotient upon dividng the number by 7). Concatenate this value with the remainder obtained when dividing the number by 7. This gives us the final base 7 representation of the number, which can be returned.

For example, if num = 9:

9//7 = 1
9%7 = 2
Therefore, the base 7 representation of 9 is 12

For example, if num = 18:

18//7 = 2
18%7 = 4
Therefore, the base 7 representation of 18 is 24

# Complexity
- Time complexity:


- Space complexity:
