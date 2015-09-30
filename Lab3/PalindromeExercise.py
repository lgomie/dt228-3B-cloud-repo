# Asks the user for input of the word and makes it lower case.
normStr = raw_input("Enter the word:\n").lower();

# Tests if the string is a palindrome, inverting the input. If so, it prints True. Else, prints False.
if normStr == normStr[::-1]:
  print 'True';
else:
  print 'False';
