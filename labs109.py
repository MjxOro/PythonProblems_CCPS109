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

def safe_squares_rooks(n, rooks):
    # set() is a python function that stores unique values only
    rows = set()
    cols = set()

    for rook in rooks:
        rows.add(rook[0])
        cols.add(rook[1])

    # count safe rows and columns
    safeRows = n - len(rows)
    safeCols = n - len(cols)

    # safe area is rectangle
    return safeRows * safeCols

def winning_card(cards, trump=None):

    # rank order from highest to lowest
    
    ranks = ['ace', 'king', 'queen', 'jack', 'ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two']

    trumps = []
    for card in cards:
        if card[1] == trump:
            trumps.append(card)

    # if trump cards exist, return highest trump
    if trumps:
        winner = trumps[0]
        for card in trumps:
            if ranks.index(card[0]) < ranks.index(winner[0]):
                winner = card
        return winner

    # no trump, find highest card of first suit
    
    firstSuit = cards[0][1]
    suitCards = []
    for card in cards:
        if card[1] == firstSuit:
            suitCards.append(card)

    winner = suitCards[0]
    for card in suitCards:
        if ranks.index(card[0]) < ranks.index(winner[0]):
            winner = card
    return winner

def seven_zero(n):

    # if n not divisible by 2 or 5, only need sevens
    if n % 2 != 0 and n % 5 != 0:
        num = 0
        for i in range(1, n + 1):
            num = num * 10 + 7
            if num % n == 0:
                return num

    # general case: try all combos of sevens and zeros

    for d in range(1, 100000):
        for k in range(1, d + 1):
            num = 0
            # add k sevens
            for i in range(k):
                num = num * 10 + 7
            # add d-k zeros
            for i in range(d - k):
                num = num * 10
            if num % n == 0:
                return num

def can_balance(items):

    # try each position as fulcrum
    for fulcrum in range(len(items)):
        left = 0
        right = 0

        # calculate left torque
        for i in range(fulcrum):
            distance = fulcrum - i
            left += items[i] * distance

        # calculate right torque
        for i in range(fulcrum + 1, len(items)):
            distance = i - fulcrum
            right += items[i] * distance

        if left == right:
            return fulcrum

    return -1

def josephus(n, k):

    circle = []
    for i in range(1, n + 1):
        circle.append(i)

    result = []
    pos = 0

    while circle:
        # modulo handles large k values automatically
        pos = (pos + k - 1) % len(circle)
        result.append(circle.pop(pos))
        if pos >= len(circle) and circle:
            pos = 0

    return result

def group_and_skip(n, out, ins):

    # works when out and ins share no common factors (gcd == 1)
    result = []

    while n > 0:
        leftover = n % out
        result.append(leftover)
        groups = n // out
        n = groups * ins

    return result








