# Euler problem 2 archive created

#In this part the variables are initialized, with a and b receiving the values of the first and second numbers of the fib sequence, respectively.
i = 0;
nA = 0;
nB = 1;
fibSum = 0;

# This iterator goes as far as the number entered. In this case, 4000000.
while i <= 4000000:

    # Yhe variable nC receives the sum of the previous 2 numbers.
    nC = nA + nB;
    # The variable nA receives the value of current nB.
    nA = nB;
    # The variable nB receives the value of current nC, which in the next iteration will add with the current nA value.
    nB = nC;

    # This part of the code tests if the current value of nC is divisible by 2. If so, it adds its value to the fibSum variable.
    if nC%2==0:
        fibSum += nC;
    i += 1;

# Prints the final value of fibSum.
print fibSum;