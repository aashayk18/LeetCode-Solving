# Intuition
Create a dictionary, check values in input with values in dictionary.

# Approach
Create a dictionary to hold the Roman values and their corresponding integer values. Initialize a result variable with 0 value. Run a loop over the input, until its penultimate element. For each element in the input, check if its corresponding integer value in the dictionary is less than the integer value corresponding with the next Roman value. If it is less, subtract the integer value from the result variable, if not add it to the variable. In the end, return the result variable added with the integer value corresponding with the last element of the input.

# Complexity
Time complexity:

Space complexity:
