# Intuition
Check the sum of the digits of the number, see if it goes to 1 or ends up looping continuously.

# Approach
Create a function to check the sum of the digits of the number, and return that sum. Create an empty set. 
Create a while loop, and:
1. Check if the value of n is equal to 1 in which case return True (which is one of the expected outputs). 
2. If the value of n is already in the set (since a set stores unique values), we understand that we are in fact in a loop and we can return False (which is another expected output). 
3. Add the value of n to the set, inside the loop. 
4. Make the value of n equal to the value returned by the sum function we created earlier, i.e. the sum of its digits.

# Complexity
- Time complexity:


- Space complexity:
