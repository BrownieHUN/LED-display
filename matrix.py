# ---------------
# -  LIBRARIES  -
# ---------------

import sys #(sys.argv[x])
import os #(os.system('clear'))
import time

# ---------------
# -  VARIABLES  -
# ---------------

rows = 20
columns = 95
base = "\u001b[37m□\033[0m"
matrix = [[base for i in range(columns)] for j in range(rows)] #matrix[sor][oszlop]
colored = "\u001b[33m■\033[0m"
#colored = "■"
segedpixel = 1
letterdb = open("letters-1row.txt", "r").readlines()
letterdata = [[letterdb[i+(j*rows)] for i in range(rows)] for j in range(len(letterdb)//rows)]
letterdb2 = open("letters-2row.txt", "r").readlines()
letterdata2 = [[letterdb2[i+(j*10)] for i in range(10)] for j in range(len(letterdb2)//10)]
matrixtext = []
diff = [0, 0, 0] #[0] - ur kezdet, [1] - ur vég, [2] - lr vég

for i in range(len(letterdb)//rows):
    letterdata[i][0] = letterdata[i][0].rstrip('\n')

for i in range(len(letterdb2)//10):
    letterdata2[i][0] = letterdata2[i][0].rstrip('\n')

letterdict = {}

for i in range(len(letterdb)//rows):
    for j in range(rows):
        letterdict[letterdata[i][0]] = letterdata[i]

letterdict2 = {}

for i in range(len(letterdb2)//10):
    for j in range(10):
        letterdict2[letterdata2[i][0][0]] = letterdata2[i]

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
    for i in range(1, len(letterdata[x])): # 1-gyel kezdődik, mert gyökér vagyok és a betű is beleszámít a sorokba
        global segedpixel
        for j in range(len(letterdata[x][i])):
            if letterdata[x][i][j] == "1":
                matrix[i][segedpixel+j] = colored
    segedpixel += len(letterdata[x][2])-1

def V5(x: str):
    for i in range(1, rows):
        global segedpixel
        for j in range(len(letterdict[x][i])):
            if letterdict[x][i][j] == "1":
                matrix[i][segedpixel+j] = colored
    segedpixel += len(letterdict[x][i])-1

def V52(x: str):
    for i in range(1, 10):
        global segedpixel
        for j in range(len(letterdict2[x][i])):
            if letterdict2[x][i][j] == "1":
                matrix[seged+i][segedpixel+j] = colored
    segedpixel += len(letterdict2[x][i])-1

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

def textToMatrix():
    for i in matrixtext:
        V5(i[0])

def textToMatrix2():
    for i in matrixtext:
        seged = 0
        V52(i[seged])

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
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = colored
        drawDisplay()
        time.sleep(0.5)
        os.system('clear')
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = base
        drawDisplay()
        time.sleep(0.5)
        os.system('clear')


# ---------------
# -  ARGUMENTS  -
# ---------------

for i in range(len(sys.argv)):
    if(sys.argv[i] == "-h" or sys.argv[i] == "--help"):
        print(
            "Usage: matrix.py [OPTION]...\n\n"
            "Wannabe LED display. Displays text in a pre-defined font.\n\n"
            "Options:\n"
            "-ln,   --linenumber=STR    line number: displays line number at the start of the display\n"
            "-r,    --row=STR           one-row mode: displays text in one row in the middle\n"
            "-ur,   --upperrow=STR      upper-row mode: displays text in the upper row of the display\n"
            "-lr,   --lowerrow=STR      lower-row mode: displays text in the lower row of the display\n"
            "-t,    --test              display test: tests the display by turning on or off different pixels\n"
            "-s,    --save=FILE         save the display in a file [default: $HOME/.cache/LEDdisplay]\n"
            "-l,    --load=FILE         load another display from a file [default: $HOME/.cache/LEDdisplay]\n"
            "-h,    --help              displays this menu\n\n"
            "Special characters and their ids respectively:\n"
            "  = _\n"
            ". = .\n"
            "! = !\n"
            "? = ?\n"
            "> = }\n"
            "▶ = {\n"
            "/ = /\n"
            "( = [\n"
            ") = ]\n"
            "+ = +\n"
            "- = -"
        )

    elif(sys.argv[i] == "-t" or sys.argv[i] == "--test"):
        kijelzoTeszt()

    elif(sys.argv[i] == "-ln" or sys.argv[i] == "--linenumber"):
        matrixtext = [i.split() for i in sys.argv[i+1]]
        textToMatrix()
        segedpixel += 3

    elif(sys.argv[i] == "-r" or sys.argv[i] == "--row"):
        matrixtext = [i.split() for i in sys.argv[i+1]]
        textToMatrix()

    elif(sys.argv[i] == "-ur"):
        matrixtext = [i.split() for i in sys.argv[i+1]]
        seged = 0
        diff[0] = segedpixel-1
        # a mátrixba írós függvény azon része, ami megmondja, hogy milyen hosszú a szöveg
        for i in matrixtext:
            segedpixel += len(letterdict2[i[0]][j])-1
        # ez itt a szöveg végéből a kezdetét kivonja, így megkapva a hosszűságát, majd azt a columns változóból
        # kivonva és kettővel elosztva megkapható, hogy mennyi indent kell ahhoz, hogy relatíve középen legyen
        seged2 = (columns-(segedpixel - diff[0]))//2
        segedpixel = seged2 + diff[0]//2
        textToMatrix2()
        diff[1] = segedpixel

    elif(sys.argv[i] == "-lr"):
        matrixtext = [i.split() for i in sys.argv[i+1]]
        seged = 9
        segedpixel = diff[0]
        # a mátrixba írós függvény azon része, ami megmondja, hogy milyen hosszú a szöveg
        for i in matrixtext:
            segedpixel += len(letterdict2[i[0]][j])-1
        # ez itt a szöveg végéből a kezdetét kivonja, így megkapva a hosszűságát, majd azt a columns változóból
        # kivonva és kettővel elosztva megkapható, hogy mennyi indent kell ahhoz, hogy relatíve középen legyen
        seged2 = (columns-(segedpixel - diff[0]))//2
        segedpixel = seged2 + diff[0]//2
        textToMatrix2()
        diff[2] = segedpixel

#seged = input("text: ")
#lista = [i.split() for i in seged]

# kérlek ezt nézd meg és magyarázd el, hogy itt mi a keserves faszt csináltam véletlenül, amitől elkezdett működni
# annyit tudok fixen, hogy ránéztem a mai infos alkotásodra és mondom hátha kihagyhatom a range(len...) részt belőle
# de mondom ez magában kevés lesz, akkor kéne a segéd hozzá, ami így utólag ránézve semmit nem csinál, de mégis kell
# így utólag nem tudom, hogy ez mégis miért működik, az én olvasatom szerint ez minden, csak nem egy működő 4 sor
#for i in matrixtext:
#    V5(i[0])

# itt az előző, viszonyítás gyanánt
#for i in range(len(lista)):
#    V5(lista[i])    # ez az, ami soha nem működött, de ezt szerettem volna
#    V5(seged)       # ez működött, de csak részben érte el a célját (egy karakter limit)

#for i in range(0, rows):
 #   if i <= 9:
  #      for j in range(diff[0]-1, diff[1]):
   #         if matrix[i][j] == colored:
    #            matrix[i][j] = base
     #       else:
      #          matrix[i][j] = colored
    #else:
     #   for j in range(diff[0]-1, diff[2]):
      #      if matrix[i][j] == colored:
       #         matrix[i][j] = base
        #    else:
         #       matrix[i][j] = colored


drawDisplay()
#print("asd")
#print(matrix[5])

#seged = input("text: ")

#lista = [i.split(" ") for i in seged]

# ■
