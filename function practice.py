def ask_display_number ( ) :
    number = int (input ('Enter an integer value:'))
    print ('The value you entered is: ', number)
    
ask_display_number ( )

def greetings ( ) :
    print('hello')
    print('bonjour')
    
def greet_twice ( ) :
    greetings ( )
    greetings ( )
    
greet_twice ( )

def print_line ( ) :
    print('+'*6)
    
print_line ( )

def print_vertical_line ( ) :
    print("|", 2*" ", "|")
    
print_vertical_line ( )

def print_box ( ) :
    print_line ( )
    print_vertical_line ( )
    print_vertical_line ( )
    print_line ( )
    
print_box ( )
    
