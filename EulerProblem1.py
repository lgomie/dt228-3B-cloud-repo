# Euler problem 1 archive created

# Here I set the range for the sum operation
for i in range(0,1000):

  # The logic behind this part is that, if the remainder of a
  # division of a number by 3 or 5 is 0, then this number is a
  # multiple of either one.
  if i%3==0 or i%5==0:

    # This part of the code sums the multiples
    sum += i;

# Here the result is printed out
print sum;