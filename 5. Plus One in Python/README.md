# Intuition
Convert the array elements into an integer, add 1, and convert back to an array.

# Approach
Iterate over the array to convert each element into a string and concatenate them using the join() method. Convert the resulting string into an integer and add 1 to it. Convert this integer into a string, then run a map() function over it to convert each of its elements into an integer. Pass this map() function to a list() function to get the desired output.

# Complexity
Time complexity:

Space complexity:
