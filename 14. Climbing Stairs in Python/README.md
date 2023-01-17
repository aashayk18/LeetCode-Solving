# Approach
Initialize two variables a and b with the value 1. These represent the first two terms of a Fibonacci series. Run a for loop in the range of (n-1) in which, we assign the value of a to a temporary variable before adding the value of b to a. The previously stored value of a now gets assigned to b. Finally, we return the value in a.
###### Let us understand with the help of an example. 
n = 3
We will run the loop 2 times.

**Iteration 1:**
First, tmp gets a i.e. 1
Then, a gets added with b as 1+1 = 2
Now, b gets the value in tmp i.e. 1

**Iteration 2:**
Now, tmp gets a i.e. 2
Then, a gets added with b as 2+1 = 3
Now, b gets the value in tmp i.e. 2

We return a i.e. 3
This is the Fibonacci value for 3, and also our answer.

The answer values for further values of n will be as per the Fibonacci series: 
5, 8, 13, ... ; for n = 4, 5, 6, ...

# Complexity
- Time complexity:


- Space complexity:
