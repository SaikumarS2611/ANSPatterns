

def for_equilateral_triangle():
        """Shape of 'Equilateral Triangle' using Python for loop"""

        for row in range(12):
                if row%2!=0:
                        print(' '*(12-row), '* '*row)
def while_equilateral_triangle():
        """Shape of 'Equilateral Triangle' using Python while loop"""
        row = 0
        while row<12:
                if row%2!=0:
                        print(' '*(12-row), '* '*row)
                row += 1
# ----------------------------------------------------------------------

def for_isosceles_triangle():
        """Shape of 'Isosceles Triangle' using Python for loop"""

        for row in range(7):
                print(' '*(7-row), '* '*row)

def while_isosceles_triangle():
        """Shape of 'Isosceles Triangle' using Python while loop """
        row = 0
        while row<7:
                print(' '*(7-row), '* '*row)
                row += 1
# ----------------------------------------------------------------------
def for_kite():
        """Pattern of 'Kite' using Python for loop """

        for row in range(9):
                if row%2!=0:
                        print(' '*(10-row), '* '*row)
        for col in range(10):
                print(' '*(col+1),'* '*(9-col))
                
def while_kite():
        """Pattern of 'Kite' using Python while loop """

        row = 0
        while row<9:
                if row%2!=0:
                        print(' '*(10-row), '* '*row)
                row += 1
        col = 0
        while col<10:
                print(' '*(col+1),'* '*(9-col))
                col += 1
                
# ----------------------------------------------------------------------
def for_leftange_triangle():           

        """Shape of 'leftangle Triangle' using Python for loop"""

        for row in range(1,6):
                print(' '*(5-row),'*'*row)

def while_leftange_triangle():           

        """Shape of 'leftangle Triangle' using Python while loop"""
        row = 1
        while row<6:
                print(' '*(5-row),'*'*row)
                row += 1

# ----------------------------------------------------------------------
def for_parallelogram():
        """Shape of 'Parallelogram' using Python for loop """

        for row in range(6):
                print(' '*(5-row), end = ' ')
                for col in range(9):
                        if row==0 or col==0 or row==5 or col==8:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_parallelogram():
        """Shape of 'Parallelogram' using Python while loop """
        row = 0
        while row<6:
                print(' '*(5-row), end = ' ')
                col = 0
                while col<9:
                        if row==0 or col==0 or row==5 or col==8:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        
                        col +=1
                print()
                row += 1
                            
# ----------------------------------------------------------------------
def for_rectangle():
        """Shape of 'Rectangle' using Python for loop """

        for row in range(6):
                for col in range(8):
                        if row==0 or col==0 or row==5 or col==7:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()
                
def while_rectangle():
        """Shape of 'Rectangle' using Python while loop """
        row = 0
        while row<6:
                col = 0
                while col<8:
                
                        if row==0 or col==0 or row==5 or col==7:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
                
                
# ----------------------------------------------------------------------
def for_reverse_triange():
        """Shape of 'Reverse Triangle' using Python for loop """

        for row in range(6,0,-1):
                print(' '*(6-row), '* '*row)
                

def while_reverse_triange():
        """Shape of 'Reverse Triangle' using Python while loop """
        row = 6
        while row>0:
                
                print(' '*(6-row), '* '*row)
                row -= 1
                

# ----------------------------------------------------------------------
def for_rhombus():
        """Shape of 'Rhombus' using Python for loop """
        
        for row in range(9):
                for col in range(9):
                        if row+col==4 or col-row==4 or row-col==4 or row+col==12:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_rhombus():
        """Shape of 'Rhombus' using Python while loop """
        row = 0
        while row<9:
                col = 0
                while col<9:
                        if row+col==4 or col-row==4 or row-col==4 or row+col==12:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------

def for_rightangle_triangle():

        """Shape of 'Rightangle Triangle' using Python for loop"""

        for row in range(1,6):
                print('* '*row)


def while_rightangle_triangle():

        """Shape of 'Rightangle Triangle' using Python while loop"""
        row = 1
        while row<6:
                print('* '*row)
                row += 1

# ----------------------------------------------------------------------
def for_square():
        """Shape of 'Square' using Python for loop """

        for row in range(5):
                for col in range(5):
                        if row==0 or col==0 or row==4 or col==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_square():
        """Shape of 'Square' using Python while loop """

        row = 0
        while row<5:
                col = 0
                while col<5:
                        if row==0 or col==0 or row==4 or col==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------

def for_tltriangle():
        """Shape of 'Top_Leftangle Triangle' """

        for row in range(6,0,-1):
                print(' '*(6-row),'*'*row)


def while_tltriangle():
        """Shape of 'Top_Leftangle Triangle' using Python while loop"""
        row = 6
        while row>0:
                print(' '*(6-row),'*'*row)
                row -= 1

# ----------------------------------------------------------------------

def for_trtriangle():
        """Shape of 'Top_Rightangle Triangle' using Python for loop """

        for row in range(6,0,-1):
                print('* '*row)



def while_trtriangle():
        """Shape of 'Top_Rightangle Triangle' using Python while loop """
        row = 6
        while row>0:
                print('* '*row)
                row -= 1

# ----------------------------------------------------------------------
def for_trapezium():
        """Shape of 'Trapezium' using Python for loop """

        for row in range(6):
                print(' '*(5-row), end = ' ')
                for col in range(14):
                        if row==0 and col<9 or col==0 or row==5 or col-row==8:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_trapezium():
        """Shape of 'Trapezium' using Python while loop """

        row = 0
        while row<6:

                print(' '*(5-row), end = ' ')
                col = 0
                while col<14:
                        if row==0 and col<9 or col==0 or row==5 or col-row==8:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_triangle():
        """Shape of 'Triangle' using Python for loop"""

        for row in range(6):
                for col in range(6):
                        if row<=col:
                                print(' ', end = ' ')
                        else:
                                print('*', end = ' ')
                print()

def while_triangle():
        """Shape of 'Triangle' using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<6:
                        if row<=col:
                                print(' ', end = ' ')
                        else:
                                print('*', end = ' ')

                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
