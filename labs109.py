def is_ascending(items):
    #Check empty lists
    if not items:
        return True
    for i in range(len(items) - 1):
        if items[i] >= items[i+1]:
            return False
    return True

def riffle(items, out=True):
    # Check empty list case
    if not items:
        return []
    # create left and right shuffles
    left = items[:len(items) // 2]
    right = items[len(items) // 2:]
    final = []

    for i in range(len(items) // 2):
        if(out):
            final.append(left[i])
            final.append(right[i])
        else:
            final.append(right[i])
            final.append(left[i])

    return final

def only_odd_digits(n):
    # check 0.
    if (n == 0):
        return False
    elif(n < 0):
        return false
    
    # Run a loop until n reaches 0
    # if loop completes all digits are odd
    while (n > 0):
        digit = n % 10
        if(digit % 2 == 0):
            return False
        n = n // 10
    return True

def is_cyclops(n):
    # check 0
    if (n == 0):
        return True
    
    # Loop the digits.
    # figure out where 0s are in the digits
    # figure out if number of digits are odd
    # if there is multiple 0s and number of digits are odd its false
    i = 0 # count how many digits
    hasZero = False
    num = n
    while (num > 0):
        digit = num % 10
        if(digit == 0 and not hasZero):
            hasZero = True
        elif (digit == 0 and hasZero):
            return False
        i += 1
        num = num // 10
    #check single digit numbers
    if(i <= 1 and n != 0 ):
        return False

    # if i is an odd number the num of digits is odd.
    if (i % 2 == 0):
        return False
    # get middle number
    middledigit = (n // (10 ** ((i // 2)))) % 10
    if(i % 2 == 1 and middledigit == 0):
        return True
    else:
        return False








