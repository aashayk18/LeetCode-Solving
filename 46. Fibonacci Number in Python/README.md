# Intuition
Create an array with the first two known elements of the Fibonacci series, and then recursively add new elements to it.

# Approach
Create the `fibn` array with the first two known elements of the Fibonacci series - 0 and 1. Run a for loop in the range of 2 to (n+1), for the further terms in the series. Recursively add the last two elements of the `fibn` array with each other and append the sum to the array. Finally, return the `fibn` array.

### Let us understand with the help of an example.

For n = 2, 

we add the last two elements of the array i.e. 0 + 1 = 1, and append this to the array

For n = 3, 

we add the last two elements of the array i.e. 1 + 1 = 2, and append this to the array

For n = 4, 

we add the last two elements of the array i.e. 2 + 1 = 3, and append this to the array

For n = 5, 

we add the last two elements of the array i.e. 3 + 2 = 5, and append this to the array

And so on.

# Complexity
- Time complexity:


- Space complexity:
