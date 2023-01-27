'''
DotSquare
1/26/2023
Python I

Instructions:
Before you run the program, what do you think
it will print? Check your prediction by running
the program. What does end="" mean in this line
of code?

print("* ", end="")

Finally, check out the docstring! 
'''

def dot_square():
    '''
    Prints a 10 by 10 square of dots.
    '''
    for i in range(0, 10):
        for j in range(0, 10):
            print("* ", end="")
        print()


dot_square()
