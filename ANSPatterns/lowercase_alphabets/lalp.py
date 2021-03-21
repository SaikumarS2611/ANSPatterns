
def for_a():
        """ Lower case Alphabet letter 'a' pattern using Python for loop """


        for row in range(7):
                for col in range(5):
                        if row%3==0 and col>0 and col<4 or col==0 and row in (1,4,5) or col==4 and row>0 :
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_a():
                
        """ Small case Alphabet letter 'a' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<5:
                        if row%3==0 and col>0 and col<4 or col==0 and row in (1,4,5) or col==4 and row>0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_b():
        """ Lower case Alphabet letter 'b' pattern using Python for loop"""

        for row in range(7):
                for col in range(4):
                        if col==0 or row!=0 and row%3==0 and col<3 or col==3 and row in (4,5):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_b():
                
        """ Lower case Alphabet letter 'b' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<4:
                        if col==0 or row!=0 and row%3==0 and col<3 or col==3 and row in (4,5):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_c():
        """ Lower case Alphabet letter 'c' pattern using Python for loop"""

        for row in range(4):
                for col in range(4):
                        if col==0 and row%3!=0 or col>0 and row%3==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_c():
                
        """ Lower case Alphabet letter 'c' patter using Python while loop"""

        row = 0
        while row<4:
                col = 0
                while col<4:
                        if col==0 and row%3!=0 or col>0 and row%3==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_d():
        """ Lower case Alphabet letter 'd' pattern using Python for loop"""

        for row in range(7):
                for col in range(4):
                        if col==3 or col==0 and row in (4,5) or row>0 and col>0 and row%3==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_d():
                
        """ Lower case Alphabet letter 'd' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<4:
                        if col==3 or col==0 and row in (4,5) or row>0 and col>0 and row%3==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_e():
        """ Lower case Alphabet letter 'e' pattern using Python for loop"""

        for row in range(7):
                for col in range(6):
                        if col==0 and row>0 and row<6 or col>0 and col<5 and row%3==0 or col==5 and row in (1,2):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_e():
        """ Lower case Alphabet letter 'e' pattern using Python while loop"""
        row = 0
        while row<7:
                col = 0
                while col<6:
                        if col==0 and row>0 and row<6 or col>0 and col<5 and row%3==0 or col==5 and row in (1,2):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_f():
        """ Lower case Alphabet letter 'f' pattern using Python for loop"""

        for row in range(6):
                for col in range(4):
                        if col==1 and row>0 or row==3 and col<3 or col==2 and row==0 or col==3 and row==1:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_f():
                
        """ Lower case Alphabet letter 'f' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<4:
                        if col==1 and row>0 or row==3 and col<3 or col==2 and row==0 or col==3 and row==1:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_g():
        """ Lower case Alphabet letter 'g' pattern using Python for loop"""

        for row in range(7):
                for col in range(5):
                        if row%3==0 and col>0 and col<4 or col==0 and row in (1,2,5) or col==4 and row<6:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_g():
        """ Lower case Alphabet letter 'g' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<5:
                        if row%3==0 and col>0 and col<4 or col==0 and row in (1,2,5) or col==4 and row<6:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_h():
        """ Lower case Alphabet letter 'h' pattern using Python for loop"""

        for row in range(5):
                for col in range(4):
                        if col==0 or row==2 and col<3 or col==3 and row>2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_h():
        """ Lower case Alphabet letter 'h' pattern using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<4:
                        if col==0 or row==2 and col<3 or col==3 and row>2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_i():
        """ Lower case Alphabet letter 'i' pattern using Python for loop"""

        for row in range(6):
                for col in range(4):
                        if col==2 and row!=1 or row==5 and col>0 or col==1 and row==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_i():
        """ Lower case Alphabet letter 'i' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<4:
                        if col==2 and row!=1 or row==5 and col>0 or col==1 and row==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_j():
        """ Lower case Alphabet letter 'j' pattern using Python for loop"""

        for row in range(6):
                for col in range(4):
                        if col==2 and row!=1 or row==5 and col in (1,2) or col==0 and row==4 or col==1 and row==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_j():
        """ Lower case Alphabet letter 'j' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<4:
                        if col==2 and row!=1 or row==5 and col in (1,2) or col==0 and row==4 or col==1 and row==2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_k():
        """ Lower case Alphabet letter 'k' pattern using Python  for loop"""

        for row in range(7):
                for col in range(4):
                        if col==0 or row+col==4 or row-col==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_k():
        """ Lower case Alphabet letter 'k' pattern using Python while loop"""
        row = 0
        while row<7:
                col = 0
                while col<4:
                        if col==0 or row+col==4 or row-col==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_l():
        """ Lower case Alphabet letter 'l' pattern using Python  for loop"""

        for row in range(6):
                for col in range(3):
                        if col==0 and row==5 or col==1 and row!=5 or col==2 and row==5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print() 

def while_l():
                
        """ Lower case Alphabet letter 'l' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<3:
                        if col==0 and row==5 or col==1 and row!=5 or col==2 and row==5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_m():
        """ Lower case Alphabet letter 'n' pattern using Python for loop"""

        for row in range(4):
                for col in range(5):
                        if row==0 and (col==0 or col%2!=0) or row>0 and col%2==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_m():
        """ Lower case Alphabet letter 'm' pattern using Python while loop"""

        row = 0
        while row<4:
                col = 0
                while col<5:
                        if row==0 and (col==0 or col%2!=0) or row>0 and col%2==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_n():
        """ Lower case Alphabet letter 'n' pattern using Python  for loop"""

        for row in range(4):
                for col in range(3):
                        if row==0 and col in (0,1) or row>0 and col%2==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_n():
        """ Lower case Alphabet letter 'n' pattern using Python while loop"""

        row = 0
        while row<4:
                col = 0
                while col<3:
                        if row==0 and col in (0,1) or row>0 and col%2==0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_o():
        """ Lower case Alphabet letter 'o' pattern using Python for loop"""

        for row in range(4):
                for col in range(4):
                        if row%3==0 and col in (1,2) or col%3==0 and row in (1,2):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')	
                print()


def while_o():
        """ Lower case Alphabet letter 'o' pattern using Python while loop"""

        row = 0
        while row<4:
                col = 0
                while col<4:
                        if row%3==0 and col in (1,2) or col%3==0 and row in (1,2):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_p():
        """ Lower case Alphabet letter 'p' pattern using Python for loop"""

        for row in range(5):
                for col in range(4):
                        if col==0 or row%2==0 and row!=4 and col<3 or col==3 and row==1:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_p():
        """ Lower case Alphabet letter 'p' pattern using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<4:
                        if col==0 or row%2==0 and row!=4 and col<3 or col==3 and row==1:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_q():
        """ Lower case Alphabet letter 'q' pattern using Python for loop"""

        for row in range(6):
                for col in range(4):
                        if col>0 and col<2 and row%3==0 or col==0 and row in (1,2) or col==2 or col==3 and row==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print() 

def while_q():
        """ Lower case Alphabet letter 'q' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<4:
                        if col>0 and col<2 and row%3==0 or col==0 and row in (1,2) or col==2 or col==3 and row==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_r():
        """ Lower case Alphabet letter 'r' pattern using Python for loop"""

        for row in range(5):
                for col in range(4):
                        if row==0 and col!=1 or col==1 and row>0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_r():
        """ Lower case Alphabet letter 'r' pattern using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<4:
                        if row==0 and col!=1 or col==1 and row>0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_s():
        """ Lower case Alphabet letter 's' pattern using Python for loop"""

        for row in range(7):
                for col in range(5):
                        if row%3==0 and col>0 and col<4 or col==0 and row%3!=0 and row!=4 or col==4 and row%3!=0 and row!=2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()


def while_s():
        """ Lower case Alphabet letter 's' pattern using Python while loop"""

        row = 0
        while row<7:
                col = 0
                while col<5:
                        if row%3==0 and col>0 and col<4 or col==0 and row%3!=0 and row!=4 or col==4 and row%3!=0 and row!=2:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_t():
        """ Lower case Alphabet letter 't' pattern using Python for loop"""

        for row in range(6):
                for col in range(3):	
                        if col==1 and row!=5 or row==2 or col==2 and row==5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_t():
        """ Lower case Alphabet letter 't' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<3:
                        if col==1 and row!=5 or row==2 or col==2 and row==5:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_u():
        """ Lower case Alphabet letter 'u' pattern using Python for loop"""

        for row in range(4):
                for col in range(4):
                        if col%3==0 and row<3 or row==3 and col>0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_u():
        """ Lower case Alphabet letter 'u' pattern using Python while loop"""

        row = 0
        while row<4:
                col = 0
                while col<4:
                        if col%3==0 and row<3 or row==3 and col>0:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_v():
        """ Lower case Alphabet letter 'v' pattern using Python for loop"""

        for row in range(4):
                for col in range(8):
                        if row-col==0 or row+col==6:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                print()


def while_v():
        """ Lower case Alphabet letter 'v' pattern using Python  while loop"""

        row = 0
        while row<4:
                col = 0
                while col<8:
                        if row-col==0 or row+col==6:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_w():
        """ Lower case Alphabet letter 'w' pattern using Python for loop"""

        for row in range(5):
                for col in range(7):
                        if col in (0,6) and row<4 or row==4 and col%3!=0 or col==3 and row in (2,3):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print()

def while_w():
                
        """ Lower case Alphabet letter 'w' pattern using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<7:
                        if col in (0,6) and row<4 or row==4 and col%3!=0 or col==3 and row in (2,3):
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_x():
        """ Lower case Alphabet letter 'x' pattern using Python for loop"""

        for row in range(5):
                for col in range(5):
                        if row-col==0 or row+col==4:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                print()

def while_x():
        """ Lower case Alphabet letter 'x' pattern using Python while loop"""

        row = 0
        while row<5:
                col = 0
                while col<5:
                        if row-col==0 or row+col==4:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_y():
        """ Lower case Alphabet letter 'y' pattern using Python for loop"""

        for row in range(6):
                for col in range(7):
                        if row+col==5 or row-col==0 and row<3:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                print()

def while_y():
        """ Lower case Alphabet letter 'y' pattern using Python while loop"""

        row = 0
        while row<6:
                col = 0
                while col<7:
                        if row+col==5 or row-col==0 and row<3:
                                print('*', end = '')
                        else:
                                print(' ', end = '')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
def for_z():
        """ Lower case Alphabet letter 'z' pattern using Python for loop"""

        for row in range(4):
                for col in range(4):
                        if row==0 or row==3 or row+col==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                print() 

def while_z():
        """ Lower case Alphabet letter 'z' pattern using Python while loop"""

        row = 0
        while row<4:
                col = 0
                while col<4:
                        if row==0 or row==3 or row+col==3:
                                print('*', end = ' ')
                        else:
                                print(' ', end = ' ')
                        col += 1
                print()
                row += 1

# ----------------------------------------------------------------------
