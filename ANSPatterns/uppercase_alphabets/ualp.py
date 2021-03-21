
def for_A():
        """ Upper case Alphabet letter 'A' pattern using Python for loop"""
        for row in range(6):
                for col in range(5):
                        if row==0 and col%4!=0 or col%4==0 and row>0 or row==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_A():
        """ Upper case Alphabet letter 'A' pattern using Python while loop"""
        row = 0
        while row<6:
                col = 0
                while col<5:
                        if row==0 and col%4!=0 or col%4==0 and row>0 or row==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
                
# ----------------------------------------------------------------------
def for_B():
        """ Upper case Alphabet letter 'B' pattern using Python for loop"""

        for row in range(7):
                for col in range(5):
                        if col==0 or row%3==0 and col<4 or col==4 and row%3!=0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_B():
        """ Upper case Alphabet letter 'B' pattern using Python while loop"""
        row = 0
        while row<7:
                col = 0
                while col<5:
                        if col==0 or row%3==0 and col<4 or col==4 and row%3!=0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row +=1
# ----------------------------------------------------------------------
def for_C():
        """ Upper case Alphabet letter 'C' pattern using Python for loop"""

        for row in range(6):
                for col in range(5):
                        if row in (0,5) and col>0 and col<4 or col==0 and row>0 and row<5 or col==4 and row in (1,4):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_C():
        """ Upper case Alphabet letter 'C' pattern using Python while loop"""
        row = 0
        while row<6:
                col = 0
                while col<5:
                        if row in (0,5) and col>0 and col<4 or col==0 and row>0 and row<5 or col==4 and row in (1,4):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row +=1
# ----------------------------------------------------------------------
# using for loop

def for_D():
        """ Upper case Alphabet letter 'D' pattern using Python for loop"""

        for row in range(6):
                for col in range(5):
                        if col==0 or row in (0,5) and col<4 or col==4 and row>0 and row<5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

# using while loop
def while_D():
        """ Upper case Alphabet letter 'D' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<5:
                        if col==0 or row in (0,5) and col<4 or col==4 and row>0 and row<5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col +=1
                print()
                row +=1

# ----------------------------------------------------------------------
def for_E():
        """ Upper case Alphabet letter 'E' pattern using Python for loop"""

        for row in range(7):
                for col in range(4):
                        if col==0 or row%3==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_E():
        """ Upper case Alphabet letter 'E' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<4:
                        if col==0 or row%3==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row +=1
# ----------------------------------------------------------------------
def for_F():
        """ Upper case Alphabet letter 'F' pattern using Python for loop"""

        for row in range(7):
                for col in range(4):
                        if col==0 or row%3==0 and row!=6:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_F():
        """ Upper case Alphabet letter 'F' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<4:
                        if col==0 or row%3==0 and row!=6:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col +=1
                print()
                row +=1
# ----------------------------------------------------------------------
def for_G():
        """ Upper case Alphabet letter 'G' pattern using Python for loop"""

        for row in range(7):
                for col in range(5):
                        if col==0 and row>0 and row<6 or row%3==0 and col>0 and col<4 and row!=3 or row==3 and col>1 or col==4 and (row>2 and row<6 or row==1):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()
def while_G():
        """ Upper case Alphabet letter 'G' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<5:
                        if col==0 and row>0 and row<6 or row%3==0 and col>0 and col<4 and row!=3 or row==3 and col>1 or col==4 and (row>2 and row<6 or row==1):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row +=1
# ----------------------------------------------------------------------
def for_H():
        """ Upper case Alphabet letter 'H' pattern using Python for loop"""

        for row in range(7):
                for col in range(5):
                        if col%4==0 or row==3:
                                print('*', end =' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_H():
        """ Upper case Alphabet letter 'H' pattern using Python while loop"""
        row = 0
        while row<7:
                col = 0
                while col<5:
                        if col%4==0 or row==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_I():
        """ Upper case Alphabet letter 'I' pattern using Python for loop"""

        for row in range(6):
                for col in range(5):
                        if row in (0,5) or col==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_I():
                
        """ Upper case Alphabet letter 'I' pattern using Python while loop"""
        row = 0
        while row<6:
                col = 0
                while col<5:
                        if row in (0,5) or col==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_J():
        """ Upper case Alphabet letter 'J' pattern using Python Python for loop"""

        for row in range(6):
                for col in range(5):
                        if row==0 or col==2 and row<5 or row+col==6 and col<3 or col==0 and row==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()



def while_J():
        """ Upper case Alphabet letter 'J' pattern using Python Python while loop"""
        row = 0
        while row<6:
                col = 0
                while col<5:
                        if row==0 or col==2 and row<5 or row+col==6 and col<3 or col==0 and row==4:
                            print('*', end = ' ')
                        else:
                            print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_K():
        """ Upper case Alphabet letter 'K' pattern using Python Python for loop"""

        for row in range(6):
                for col in range(4):
                        if col==0 or row+col==3 or row-col==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_K():
        """ Upper case Alphabet letter 'K' pattern using Python Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<4:
                        if col==0 or row+col==3 or row-col==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_L():
        """ Upper case Alphabet letter 'L' pattern using Python Python for loop"""

        for row in range(6):
                for col in range(4):
                        if col==0 or row==5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_L():
        """ Upper case Alphabet letter 'L' pattern using Python Python while loop"""

        for row in range(6):
                for col in range(4):
                        if col==0 or row==5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()
# ----------------------------------------------------------------------
def for_M():
        """ Upper case Alphabet letter 'M' pattern using Python Python for loop"""

        for row in range(6):
                for col in range(5):
                        if col in (0,4) or (row-col==0 or row+col==4) and row<3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_M():
        """ Upper case Alphabet letter 'M' pattern using Python Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<5:
                        if col in (0,4) or (row-col==0 or row+col==4) and row<3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_N():
        """ Upper case Alphabet letter 'N' pattern using Python Python for loop"""

        for row in range(5):
                for col in range(5):
                        if col in (0,4) or row-col==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')

                print()


def while_N():
        """ Upper case Alphabet letter 'N' pattern using Python Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<5:
                        if col in (0,4) or row-col==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_O():
        """ Upper case Alphabet letter 'O' pattern using Python for loop"""

        for row in range(6):
                for col in range(5):
                        if row in (0,5) and col>0 and col<4 or col in (0,4) and row>0 and row<5:
                                print('*', end = ' ')
                        else:
                        	print(' ', end = ' ')
                print()


def while_O():
                
        """ Upper case Alphabet letter 'O' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<5:
                        if row in (0,5) and col>0 and col<4 or col in (0,4) and row>0 and row<5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_P():
        """ Upper case Alphabet letter 'P' pattern using Python for loop"""

        for row in range(6):
                for col in range(4):
                        if col==0 or row%3==0 and col<3 or col==3 and row%3!=0 and row<3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')

                print()

def while_P():
                
        """ Upper case Alphabet letter 'P' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<4:
                        if col==0 or row%3==0 and col<3 or col==3 and row%3!=0 and row<3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row +=1

# ----------------------------------------------------------------------
def for_Q():
        """ Upper case Alphabet letter 'Q' pattern using Python for loop"""

        for row in range(5):
                for col in range(5):
                        if col in (0,4) and row>0 and row<4 or row in (0,4) and col>0 and col<4 or col-row==0 and row>2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_Q():
        """ Upper case Alphabet letter 'Q' pattern using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<5:
                        if col in (0,4) and row>0 and row<4 or row in (0,4) and col>0 and col<4 or col-row==0 and row>2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_R():
        """ Upper case Alphabet letter 'R' pattern using Python for loop"""

        for row in range(6):
                for col in range(5):
                        if col==0 or row%3==0 and col<3 or col==3 and row%3!=0 and row<3 or row-col==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_R():
        """ Upper case Alphabet letter 'R' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<5:
                        if col==0 or row%3==0 and col<3 or col==3 and row%3!=0 and row<3 or row-col==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_S():
        """ Upper case Alphabet letter 'S' pattern using Python for loop"""

        for row in range(7):
                for col in range(5):
                        if row%3==0 and col>0 and col<4 or col==0 and row%3!=0 and row<3 or col==4 and row%3!=0 and row>3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_S():
        """ Upper case Alphabet letter 'S' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<5:
                        if row%3==0 and col>0 and col<4 or col==0 and row%3!=0 and row<3 or col==4 and row%3!=0 and row>3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_T():
        """ Upper case Alphabet letter 'T' pattern using Python for loop"""

        for row in range(5):
                for col in range(3):
                        if row==0 or col==1:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_T():
        """ Upper case Alphabet letter 'T' pattern using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<3:
                        if row==0 or col==1:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_U():
        """ Upper case Alphabet letter 'U' pattern using Python for loop"""

        for row in range(6):
                for col in range(5):
                        if col%4==0 and row<5 or row==5 and col>0 and col<4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()
                

def while_U():
        """ Upper case Alphabet letter 'U' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<5:
                        if col%4==0 and row<5 or row==5 and col>0 and col<4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1


# ----------------------------------------------------------------------
def for_V():
        """ Upper case Alphabet letter 'V' pattern using Python for loop"""

        for row in range(7):
                for col in range(13):
                        if row==col or row+col==12:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                print()


def while_V():
        """ Upper case Alphabet letter 'V' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<13:
                        if row==col or row+col==12:
                                print('*', end = ' ')
                        else:
                                print(' ', end ='')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_W():
        """ Upper case Alphabet letter 'W' pattern using Python for loop"""

        for i in range(5):
                for j in range(27):
                        if (i==j or (i>1 and (i+j==8) or (i+j==13)) or (i==3 and i+j==11)):
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                print()


def while_W():
        """ Upper case Alphabet letter 'W' pattern using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<27:
                        if row==col or row>1 and row+col==8 or row+col==13 or row==3 and row+col==11:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                        col +=1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_X():
        """ Upper case Alphabet letter 'X' pattern using Python for loop"""

        for row in range(5):
                for col in range(6):
                        if row-col==0 or row+col==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_X():
        """ Upper case Alphabet letter 'X' pattern using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<6:
                        if row-col==0 or row+col==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_Y():
        """ Upper case Alphabet letter 'Y' pattern using Python for loop"""

        for row in range(7):
                for col in range(7):
                        if col==3 and row>2 or (row-col==0 or row+col==6) and row<3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_Y():
        """ Upper case Alphabet letter 'Y' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<7:
                        if col==3 and row>2 or (row-col==0 or row+col==6) and row<3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1
# ----------------------------------------------------------------------
def for_Z():
        """ Upper case Alphabet letter 'Z' pattern using Python for loop"""

        for row in range(6):
                for col in range(6):
                        if row in (0,5) or row+col==5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_Z():
        """ Upper case Alphabet letter 'Z' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<6:
                        if row in (0,5) or row+col==5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
