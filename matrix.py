# -----------------
# -   LIBRARIES   -
# -----------------

import sys #(sys.argv[x])

# -----------------
# -   VARIABLES   -
# -----------------

rows = 20
columns = 95
matrix = [["■" for i in range(columns)] for j in range(rows)] #matrix[sor][oszlop]
options = [0,"","","",0]
colored = "\u001b[33m■\033[0m"

# -------------
# -  NUMBERS  -
# -------------

def one():
    matrix

# -------------
# -  LETTERS  -
# -------------

def A():
    print("cica")

#def V():
matrix[2][2] = colored
matrix[3][2] = colored
matrix[2][3] = colored
matrix[3][3] = colored

# ----------------
# -  BASH THING  -
# ----------------

for i in range(len(sys.argv)):
    if(sys.argv[i] == "-h" or sys.argv[i] == "--help"):
        print(
            "Usage: matrix.py [OPTION]...\n\n"
            "Wannabe LED display. Displays text in a pre-defined font.\n\n"
            "Options:\n"
            "-ln,   --linenumber=INT    line number: displays line number at the start of the display\n"
            "-r,    --row=STR           one-row mode: displays text in one row in the middle\n"
            "-ur,   --upperrow=STR      upper-row mode: displays text in the upper row of the display\n"
            "-lr,   --lowerrow=STR      lower-row mode: displays text in the lower row of the display\n"
           #"-in,   --invert            invert colors: the text becomes dark and the surrounding pixels become yellow\n"
            "-s,    --save=FILE         save the state of the display in a file [default: $SHOME/.cache/LEDdisplay]\n"
            "-l,    --load=FILE         load another display from a file [default: $SHOME/.cache/LEDdisplay]\n"
            "-h,    --help              displays this menu\n"
            )

#matrix[0][0] = "\u001b[33m■\033[0m"

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end = " ")
    print("")

#print("asd")
#print(matrix[5])

#seged = input("text: ")

#lista = [i.split(" ") for i in seged]

# ■
