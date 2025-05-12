
# Helper functions for qrcode program

# Constants
VALID_NUMBERS = "01"

# Function that converts date to dictionary
def convert_date(date_str) :
    """ (str) -> dict
    Takes a string input with date in format dd/mm/yyyy
    and returns a dictionary with "Day", "Month" and "Year"
    as keys and strings as values.  If input format is wrong,
    raise ValueError
    
    >>> convert_date("11/12/2004")
    {'Day': '11', 'Month': '12', 'Year': '2004'}
    
    >>> convert_date("25/09/2024")
    {'Day': '25', 'Month': '09', 'Year': '2024'}
    
    >>> convert_date("9/1/2024")
    Traceback (most recent call last):
    ValueError: Input format incorrect!
    """

    if len(date_str) == 10 :
        # Separating dates using slash
        date_list = date_str.split('/')

        # Checking for validity of input
        if len(date_list) == 3 and (len(date_list[0]) == 2 and \
            len(date_list[1]) == 2 and len(date_list[2]) == 4) :
            # Making dictionary and keys
            date_dict = {}
            date_dict["Day"] = date_list[0]
            date_dict["Month"] = date_list[1]
            date_dict["Year"] = date_list[2]

        else :
            raise ValueError('Input format incorrect!')

    else :
        raise ValueError('Input format incorrect!')
        
    return date_dict


# Function that puts file lines into nested list
def get_data(file_path) :
    """ (str) -> list
    Takes a file path as an input and returns a
    nested list of integers representing the data
    in the file. If the file contains characters other
    than 0 and 1, raises a Value Error

    >>> get_data("small_data.txt")
    [[0, 1], [1, 0]]

    >>> get_data("not_1_or_0.txt")
    Traceback (most recent call last):
    ValueError: File should contain only 0s and 1s!

    >>> get_data("yes_1_and_0.txt")
    [[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1]]
    """
    
    # Reading the lines inside file
    fdata = open(file_path, 'r')
    data_list = [ ]

    for line in fdata :
        # The nested list
        line_list = [ ]
        line = line.strip('\n')

        for char in line :
            # Checking if numbers are valid
            if char not in VALID_NUMBERS :
                raise ValueError('File should contain only 0s and 1s!')
            else :
                char = int(char)
                line_list.append(char)

        data_list.append(line_list)
        
    return data_list
        
            
                
            

                
                

        