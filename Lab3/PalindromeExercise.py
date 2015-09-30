# Asks the user for input of the word and makes it lower case.
normStr = raw_input("Enter the word:\n").lower();
# Inverts the string so it can compare it with the original input.


# Tests if the string is a palindrome. If so, it prints True. Else, prints False.
if normStr == normStr[::-1]:
  print 'True';
else:
  print 'False';
