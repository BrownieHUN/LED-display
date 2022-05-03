# -----------------
# -   LIBRARIES   -
# -----------------

import sys #(sys.argv[x])

# -----------------
# -   VARIABLES   -
# -----------------

rows = 19
columns = 95
pieces = 6
matrix = [["■" for i in range(columns)] for j in range(rows)] #matrix[sor][oszlop]
options = [0,"","","",0]
colored = "\u001b[33m■\033[0m"
segedpixel = [0,10]
letterdb = open("letters.txt", "r")
letterdata = [i.strip("\n") for i in letterdb] #letterdata[sor][oszlop]   # HOGY A FASZBA LEHET EZT 18 SOROKRA OSZTANI?

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

#mostani
#segédpixel a következőnek a helyes megjelenítése miatt kell
def V2():
    for i in range(len(letterdata)):
        for j in range(len(letterdata[i])):
            if letterdata[i][j] == "1":
                matrix[i][j] = colored
            segedpixel[1] += 1
        segedpixel[0] += 1
    segedpixel[0] = 0
    segedpixel[1] = len(letterdata[3]) + 1
    print(segedpixel)

#előző
def V():
    print(segedpixel[0])
    segedpixel[0] += segedpixel[0]+1
    print(segedpixel[0])
    matrix[2][2] = colored
    matrix[3][2] = colored
    matrix[2][3] = colored
    matrix[3][3] = colored
    for i in range(4, 8):
        matrix[i][3] = colored
        matrix[i][4] = colored
    for i in range(8, 11):
        matrix[i][4] = colored
        matrix[i][5] = colored
    for i in range(11, 15):
        matrix[i][5] = colored
        matrix[i][6] = colored
    for i in range(15, 17):
        matrix[i][6] = colored
        matrix[i][7] = colored
        matrix[i][8] = colored
    for i in range(11, 15):
        matrix[i][8] = colored
        matrix[i][9] = colored
    for i in range(8, 11):
        matrix[i][9] = colored
        matrix[i][10] = colored
    for i in range(4, 8):
        matrix[i][10] = colored
        matrix[i][11] = colored
    matrix[2][11] = colored
    matrix[3][11] = colored
    matrix[2][12] = colored
    matrix[3][12] = colored

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
#for i in range(rows):
#    for j in range(0, columns, 12):
#        matrix[i][j] = colored

V2()

#print(matrix[1])
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end = " ")
    print("")

#print("asd")
#print(matrix[5])

#seged = input("text: ")

#lista = [i.split(" ") for i in seged]

# ■
