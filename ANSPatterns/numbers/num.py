
def for_eight():
        """ Number pattern '8' using Python for loop"""

        for row in range(7):
                for col in range(5):
                        if row%3==0 and col>0 and col<4 or col%4==0 and row%3!=0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_eight():
        """ Number pattern '8' using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<5:
                        if row%3==0 and col>0 and col<4 or col%4==0 and row%3!=0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_five():
        """ Number pattern '5' using Python for loop"""

        for row in range(7):
                for col in range(5):
                        if col==0 and row<6 and row!=4 or col>0 and col<3 and row%3==0 or col==3 and (row==0 or row>3) and row<6:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_five():
                
        """ Number pattern '5' using Python while loop"""
        row = 0
        while row<7:
                col = 0
                while col<7:
                        if col==0 and row<6 and row!=4 or col>0 and col<3 and row%3==0 or col==3 and (row==0 or row>3) and row<6:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_four():
        """ Number pattern '4' using Python for loop"""

        for row in range(5):
                for col in range(5):
                        if col==3 or row==3 or row+col==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print() 

def while_four():
                
        """ Number pattern '4' using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<5:
                        if col==3 or row==3 or row+col==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_nine():
        """ Number pattern '9' using Python for loop"""

        for row in range(7):
                for col in range(5):
                        if row%3==0 and col>0 and col<4 or col==0 and row>0 and row<3 or col==4 and row>0 and row<6:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_nine():
                
        """ Number pattern '9' using Python while loop"""
        row = 0
        while row<7:
                col = 0
                while col<5:
                        if row%3==0 and col>0 and col<4 or col==0 and row>0 and row<3 or col==4 and row>0 and row<6:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_one():
        """ Number pattern '1' using Python for loop"""

        for row in range(6):
                for col in range(3):
                        if col==1 or row==5 or col==0 and row==1:
                                print('1', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_one():
                

        """ Number pattern '1' using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<3:
                        if col==1 or row==5 or col==0 and row==1:
                                print('1', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_seven():
        """ Number pattern '7' using Python for loop"""

        for row in range(6):
                for col in range(5):
                        if row+col==4 or row==0:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                print()


def while_seven():
                
        """ Number pattern '7' using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<5:
                        if row+col==4 or row==0:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_six():
        """ Number pattern '6' using Python for loop"""

        for row in range(7):
                for col in range(5):
                        if row%3==0 and col>0 and col<4 or col==0 and row>0 and row<6 or col==4 and row<6 and row>3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_six():
        """ Number pattern '6' using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<5:
                        if row%3==0 and col>0 and col<4 or col==0 and row>0 and row<6 or col==4 and row<6 and row>3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_three():
        """ Number pattern '3' using Python for loop"""
        for row in range(7):
                for col in range(4):
                        if row%3==0 and col>0 and col<3 or col==3 and row%3!=0 or col==0 and row in (1,5):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_three():
                
        """ Number pattern '3' using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<4:
                        if row%3==0 and col>0 and col<3 or col==3 and row%3!=0 or col==0 and row in (1,5):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_two():
        """ Number pattern '2' using Python for loop"""

        for row in range(5):
                for col in range(4):
                        if row==0 and col>0 and col<3 or col==0 and row==1 or row+col==4 or row==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_two():
        """ Number pattern '2' using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<4:
                        if row==0 and col>0 and col<3 or col==0 and row==1 or row+col==4 or row==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_zero():
        """ Number pattern '0' using Python for loop"""

        for row in range(5):
                for col in range(5):
                        if row%4==0 and col>0 and col<4 or col%4==0 and row>0 and row<4 or row+col==4 and col!=0 and row!=0:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                print()

def while_zero():
                
        """ Number pattern '0' using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<5:
                        if row%4==0 and col>0 and col<4 or col%4==0 and row>0 and row<4 or row+col==4 and col!=0 and row!=0:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
