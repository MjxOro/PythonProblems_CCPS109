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

def domino_cycle(tiles):
    # Check empty list case
    if not tiles:
        return True

    # Check if each tile's end matches the next tile's start
    for i in range(len(tiles)):
        # Get current tile's end value
        current_end = tiles[i][1]
        # Get next tile's start value (wrap around for last tile)
        next_start = tiles[(i + 1) % len(tiles)][0]
        # If they don't match, not a cycle
        if current_end != next_start:
            return False

    return True

def colour_trio(colours):
    # Check single color case
    if len(colours) == 1:
        return colours

    # Keep reducing rows until we have one color left
    current_row = colours
    while len(current_row) > 1:
        next_row = ''
        for i in range(len(current_row) - 1):
            # Mix colors at position i and i+1
            c1 = current_row[i]
            c2 = current_row[i + 1]
            # If same color, result is that color
            if c1 == c2:
                next_row += c1
            else:
                # Different colors give the third color
                # Use if/else to figure out which third color
                if (c1 == 'r' and c2 == 'y') or (c1 == 'y' and c2 == 'r'):
                    next_row += 'b'
                elif (c1 == 'r' and c2 == 'b') or (c1 == 'b' and c2 == 'r'):
                    next_row += 'y'
                else:  # (c1 == 'y' and c2 == 'b') or (c1 == 'b' and c2 == 'y')
                    next_row += 'r'
        current_row = next_row

    return current_row

def count_dominators(items):
    # check empty list
    if not items:
        return 0

    # start from right to avoid nested loops
    count = 1  # last element always dominator
    maxFromRight = items[len(items) - 1]

    # loop backwards from second-to-last
    for i in range(len(items) - 2, -1, -1):
        if items[i] > maxFromRight:
            count += 1
            maxFromRight = items[i]

    return count

def extract_increasing(digits):
    # check empty string
    if not digits:
        return []

    result = []
    previous = -1
    current = 0

    # build numbers by adding digits until larger than previous
    for d in digits:
        current = 10 * current + int(d)
        if current > previous:
            result.append(current)
            previous = current
            current = 0

    return result

def words_with_letters(words, letters):
    # check empty letters
    if not letters:
        return words

    result = []

    for word in words:
        # check if letters is a subsequence of word
        letterIndex = 0
        for char in word:
            if char == letters[letterIndex]:
                letterIndex += 1
                if letterIndex == len(letters):
                    # found all letters as subsequence
                    result.append(word)
                    break

    return result

def taxi_zum_zum(moves):
    # start at origin facing north
    x = 0
    y = 0
    # directions: 0=north, 1=east, 2=south, 3=west
    direction = 0
    # direction vectors: north, east, south, west
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for move in moves:
        if move == 'L':
            direction = (direction - 1) % 4
        elif move == 'R':
            direction = (direction + 1) % 4
        elif move == 'F':
            x += dx[direction]
            y += dy[direction]

    return (x, y)








