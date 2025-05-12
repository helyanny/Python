# 1. Please complete the following:
#   Your First name and Last Name: Helyanny Perozo
#   Your Student ID: 261238389


# Evaluating characters in a string for non-letters
def is_not_valid(n):
    """ (str) -> boolean
    Goes through string, if a character is not a 
    letter or a space returns True, otherwise 
    returns False
    >>> is_not_valid('asdfsfg!sfg*')
    True
    >>> is_not_valid('f shdjjke FFG  ')
    False
    >>> is_not_valid('18&3helloYOU')
    True
    """
    for char in n:
        # For all the non-letters or spaces
        if not ('A' <= char <= 'Z' or 'a' <= char <= 'z' or char == ' ') :
            return True
    return False


# Checking if length of input is not a square number
def is_not_square(n) :
    """ (str) -> boolean
    Takes length of string, if it is not a
    square number returns True, otherwise
    returns False
    >>> is_not_square('abcdefghi')
    False
    >>> is_not_square('hi')
    True
    >>> is_not_square('1234567')
    True
    """
    # List of possible square numbers (up to 15 square)
    non_square = 1
    list_squares = [ ]
    while 0 < non_square <= 100 :
        square = non_square * non_square
        list_squares.append(square)
        non_square += 1
    s = len(n)
    if s not in list_squares :
        return True
    return False


# Making 2D square list
def string2list(n) :
    """ (str) -> list
    Takes a string of square length and returns
    a 2D square list
    >>> string2list('Hello Bye')
    [['H', 'e', 'l'], ['l', 'o', ' '], ['B', 'y', 'e']]
    >>> string2list('Blue')
    [['B', 'l'], ['u', 'e']
    >>> string2list('diphenylhydroxyethylamine')
    [['d', 'i', 'p', 'h', 'e'], ['n', 'y', 'l', 'h', 'y'], ['d', 'r', 'o', 'x', 'y'],
    ['e', 't', 'h', 'y', 'l'], ['a', 'm', 'i', 'n', 'e']]
    """
    empty_list = [ ]
    is_not_valid(n)
    # Checking for non-letters or non-spaces
    if is_not_valid(n) == True :
        return empty_list
    else :
        # Checking for non-square strings
        is_not_square(n)
        if is_not_square(n) == True :
            return empty_list
        else :
            # Checking for valid length
            if not 1 < len(n) < 1000 :
                return empty_list
            else :
                # How many elements per row/column
                jumps = int(len(n)**(1/2))
                string_list = [ ]
                for char in range(0, len(n), jumps) :
                    square_list = list(n[char : char + jumps])
                    # Adding list elements into many 2D list
                    string_list.append(square_list)
    return string_list


# Adding  space before a capital letter
def add_space(input_text) :
    """ (str) -> str
    Takes a string, adds a space before a capital letter
    if it is between 2 non-capitals, returns new string
    with the spaces included
    >>> add_space('HelloEveryone')
    Hello Everyone
    >>> add_space('BoomShakaLaka')
    Boom Shaka Laka
    >>> add_space('OhCaNadA')
    Oh Ca NadA
    """
    # Turning string into list for mutability
    my_list = list(input_text)
    for i in range(1, len(my_list)) :
        if 'A' <= my_list[i] <= 'Z' :
            # Checking if capital letter is in between non-capitals
            if 'a' <= my_list[i-1] <= 'z' and 'a' <= my_list[i+1] <= 'z' :
                my_list.insert(i, ' ')
    # Turning list back into string
    output_text = ''.join(my_list)
    return output_text


# Turning a 2D list into a string
def list2string(twod_list) :
    """ (list) -> str
    Takes a 2D and transforms it into a string going
    from top to bottom, left to right
    >>> list2string([['H', 'e', 'l'], ['l', 'o', 'o'], ['B', 'y', 'e']])
    'Helloo Bye'
    >>> list2string([['B', 'l'], ['U', 'e']])
    'Bl Ue'
    >>> list2string([['d', 'i', 'p', 'h', 'e'], ['n', 'y', 'l', 'h', 'y'], ['d', 'r', 'o', 'x', 'y'],
           ['e', 't', 'h', 'y', 'l'], ['a', 'm', 'i', 'n', 'e']])
    'diphenylhydroxyethylamine'
    """
    new_list = [ ]
    # Turning the sublists into strings
    for sublist in twod_list :
        element = ''.join(sublist)
        new_list.append(element)
    # turning simplified list into a string
    new_string = ''.join(new_list)
    # adding spaces before the capital letters (surrounded by
    # non-capitals)
    add_space(new_string)
    return add_space(new_string)
            

# Flipping 2D list Horizontally
def horizontal_flip(square_list) :
    flipped_list = [ ]
    for sublist in square_list :
        sublist[ : ] = sublist[ : : -1]
        flipped_sublist = [ ]
        for i in sublist :
            flipped_sublist.append(i)
        flipped_list.append(flipped_sublist)
        

def transpose(square_list) :
    s = len(square_list)
    for col in range(s) : 
        transposed_sublist = [ ]
        for row in range(s) :
            transposed_sublist.append(square_list[row][col])
        square_list.append(transposed_sublist)
        
    del square_list[ : s]
    
    
def flip_list(input_list) :
    horizontal_flip(input_list)
    transpose(input_list)
    

def decipher_code(n) :
    string2list(n)
    if type(string2list(n)) == list :
        list1 = string2list(n)
        flip_list(list1)
        list2string(list1)
    return list2string(list1)

def cipher_sentence(sentence: str):
    a = 0
    while a**2 < len(sentence):
        a += 1
    b = [[]]
    for f in sentence:
        c = a * (len(b[-1]) + 1) - len(b) + 1
        while a**2 >= c > len(sentence):
            b[-1].append('')
            c += a
        if len(b[-1]) < a:
            b[-1].append(f)
        else:
            b.append([f])
    c = a * (len(b[-1]) + 1) - len(b) + 1
    while a**2 >= c > len(sentence):
        b[-1].append('')
        c += a
    if len(sentence) != 0:
        transpose(b)
        horizontal_flip(b)
    d = ''
    for e in b:
        for f in e:
            d += f
    return d


def cipher_message(message: str):
    """
    >>> cipher_message('ThisIs ToShow. You how thisWorks.')
    'S sThTIhoosiw.ohou riw Yks hosWt.'
    >>> decipher_code('S sThTIhoosiw.ohou riw Yks hosWt.')
    'This Is To Show. You how this Works.'
    """
    a = ''
    b = ''
    for c in message:
        if c == '.':
            if not is_not_valid(a):
                b += cipher_sentence(a) + '.'
            a = ''
        else:
            a += c
    if a != '' and not is_not_valid(a):
        b += cipher_sentence(a)
    return b