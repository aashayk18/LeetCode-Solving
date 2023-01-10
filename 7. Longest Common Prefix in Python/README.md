# Intuition
Compare each letter of each word to check if they match, and add them to an empty string until you hit a character that doesn't match. Return the string obtained so far.

# Approach
Initialize an empty string. Zip the list, so you get the first characters of each word together in a tuple, the second letters in another tuple, and so on. Convert each such tuple into a set, and check if the length of the set is 1 - to understand if the elements were same (as sets store only 1 instance of a repeated element). If the length of the set is 1, add the first element of the tuple (any element is fine, as all elements are same but we take the first element just to be cautious) to the empty string. If the length of a set is not 1, return the string as is. Finally, return the string obtained thus far.

# Complexity
Time complexity:

Space complexity:
