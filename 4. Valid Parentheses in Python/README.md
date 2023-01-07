# Intuition
Use a stack data structure and a dictionary of key-value pairs for different kinds of parentheses.

# Approach
Create a dictionary for valid opening and closing parentheses pairs. Initialize a stack data structure and push inputs into it if they are opening parentheses. If they are closing parentheses, check if the stack is empty or if the closing parentheses doesn't match the opening parentheses present in the stack, and return False in this case. In the end, return True if the stack is empty or False if it isn't.

# Complexity
Time complexity:

Space complexity:
