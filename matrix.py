# ---------------
# -  LIBRARIES  -
# ---------------

import sys #(sys.argv[x])
import os #(os.system('clear'))
import time

# ---------------
# -  VARIABLES  -
# ---------------

rows = 21
columns = 95
pieces = 6
base = "\u001b[37m□\033[0m"
matrix = [[base for i in range(columns)] for j in range(rows)] #matrix[sor][oszlop]
options = [0,"","","","","",""]
colored = "\u001b[33m■\033[0m"
#colored = "■"
segedpixel = 1
letterdb = open("letters-1row.txt", "r").readlines()
letterdata = [[letterdb[i+(j*rows)] for i in range(rows)] for j in range(len(letterdb)//rows)]
letterdb2 = open("letters-2row.txt", "r").readlines()

letterdict = {}

for i in range(len(letterdb)//rows):
    for j in range(rows):
        letterdict[letterdata[i][0]] = letterdata[i]

# -------------
# -  LETTERS  -
# -------------

#mostani MEGTARTVA AZ UTÓKORNAK, NE NYÚLJ HOZZÁ
def V2():
    for i in range(len(letterdata)):
        global segedpixel
        for j in range(len(letterdata[i])):
            if letterdata[i][j] == "1":
                matrix[i][segedpixel+j] = colored
    segedpixel = len(letterdata[0])

#Bálint féle új, működik
def V4(x: int):
    for i in range(len(letterdata[x])):
        global segedpixel
        for j in range(len(letterdata[x][i])):
            if letterdata[x][i][j] == "1":
                matrix[i][segedpixel+j] = colored
    segedpixel += len(letterdata[x][2])-1

# ---------------------
# -  OTHER FUNCTIONS  -
# ---------------------

def clearDisplay():
    for i in range(rows):
        for j in range(columns):
            if(matrix[i][j] != base):
                matrix[i][j] = base

def drawDisplay():
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end = " ")
        print("")

def kijelzoTeszt():
    os.system('clear')
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = colored
    drawDisplay()
    time.sleep(1)
    os.system('clear')
    clearDisplay()
    for i in range(rows):
        for j in range(columns):
            if i % 2 == 0:
                if j % 2 == 0:
                    matrix[i][j] = colored
            else:
                if j % 2 == 1:
                    matrix[i][j] = colored
    drawDisplay()
    time.sleep(1)
    os.system('clear')
    clearDisplay()
    for i in range(rows):
        for j in range(columns):
            if i % 2 == 0:
                matrix[i][j] = colored
    drawDisplay()
    time.sleep(1)
    os.system('clear')
    clearDisplay()
    for i in range(rows):
        for j in range(columns):
            if i % 2 == 1:
                matrix[i][j] = colored
    drawDisplay()
    time.sleep(1)
    os.system('clear')
    clearDisplay()
    for i in range(rows):
        for j in range(columns):
            if j % 2 == 0:
                matrix[i][j] = colored
    drawDisplay()
    time.sleep(1)
    os.system('clear')
    clearDisplay()
    for i in range(rows):
        for j in range(columns):
            if j % 2 == 1:
                matrix[i][j] = colored
    drawDisplay()
    time.sleep(1)
    os.system('clear')
    clearDisplay()
    #PROBLÉMÁS RÉSZ, NEM MŰKÖDIK RENDESEN
#    for i in range(rows):
#        for j in range(columns):
#            matrix[i][j] = colored
#            drawDisplay()
#            time.sleep(0.1)
#            os.system('clear')


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


#V4(37)
#V4(40)
#segedpixel += 3
#V4(25)
#V4(5)
#V4(24)
#V4(34)
#V4(25)

#seged = input("text: ")
#lista = [i.split(" ") for i in seged]

#for i in lista:
#    if lista[i] in letterdict:
#        print("van")

kijelzoTeszt()

#print("asd")
#print(matrix[5])

#seged = input("text: ")

#lista = [i.split(" ") for i in seged]

# ■
