# ---------------
# -  LIBRARIES  -
# ---------------

import sys #(sys.argv[x])
import os #(os.system('clear'))
import time

# ---------------
# -  VARIABLES  -
# ---------------

ROWS = 20
COLUMNS = 95
BASE = ("\u001b[37m□\033[0m" if os.name != "nt" else "□")
matrix = [[BASE for i in range(COLUMNS)] for j in range(ROWS)] #matrix[sor][oszlop]
COLORED = ("\u001b[33m■\033[0m" if os.name != "nt" else "■")
#colored = "■"
segedpixel = 1
letterdb = open("letters-1row.txt", "r", encoding="utf8").readlines()
letterdata = [[letterdb[i+(j*ROWS)] for i in range(ROWS)] for j in range(len(letterdb)//ROWS)]
letterdb2 = open("letters-2row.txt", "r", encoding="utf8").readlines()
letterdata2 = [[letterdb2[i+(j*10)] for i in range(10)] for j in range(len(letterdb2)//10)]
specialdb = open("special-1row.txt", "r", encoding="utf8").readlines()
specialdata = [[specialdb[i+(j*ROWS)] for i in range(ROWS)] for j in range(len(specialdb)//ROWS)]

matrixtext = []
diff = [0, 0, 0, 0, 0] #[0] - ur/lr kezdet, [1] - ur vég, [2] - lr vég, [3] r vég, [4] lr kezdet

for i in range(len(letterdb)//ROWS):
    letterdata[i][0] = letterdata[i][0].rstrip('\n')

for i in range(len(letterdb2)//10):
    letterdata2[i][0] = letterdata2[i][0].rstrip('\n')

for i in range(len(specialdb)//ROWS):
    specialdata[i][0] = specialdata[i][0].rstrip('\n')

letterdict = {}

for i in range(len(letterdb)//ROWS):
    for j in range(ROWS):
        letterdict[letterdata[i][0]] = letterdata[i]

letterdict2 = {}

for i in range(len(letterdb2)//10):
    for j in range(10):
        letterdict2[letterdata2[i][0][0]] = letterdata2[i]

specialdict = {}

for i in range(len(specialdb)//ROWS):
    for j in range(ROWS):
        specialdict[specialdata[i][0]] = specialdata[i]

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

#Bálint féle új, elavult 
def V4(x: int):
    for i in range(1, len(letterdata[x])): # 1-gyel kezdődik, mert gyökér vagyok és a betű is beleszámít a sorokba
        global segedpixel
        for j in range(len(letterdata[x][i])):
            if letterdata[x][i][j] == "1":
                matrix[i][segedpixel+j] = colored
    segedpixel += len(letterdata[x][2])-1

# jelenlegi, egybecsinálva a 2 dictet
def V5(x: str, ul: int, ld): # x = adott betű, ul = melyik sorban kezdődjön a kiírás, ld = egysoros-e (2 = special)
    if ld == 0:
        nld = letterdict2
    elif ld == 1:
        nld = letterdict
    else:
        nld = specialdict

    for i in range(1, len(nld[x])):
        global segedpixel
        for j in range(len(nld[x][i])):
            if nld[x][i][j] == "1":
                matrix[ul+i][segedpixel+j] = COLORED
    segedpixel += len(nld[x][i])-1

# ---------------------
# -  OTHER FUNCTIONS  -
# ---------------------

def clearDisplay():
    for i in range(ROWS):
        for j in range(COLUMNS):
            if(matrix[i][j] != BASE):
                matrix[i][j] = BASE

def drawDisplay():
    for i in range(ROWS):
        for j in range(COLUMNS):
            print(matrix[i][j], end = " ")
        print("")

def textToMatrix(ul: int, ld: int): #ul = u.a., mint a V5-nél lévő ul; ld = 1 soros-e a kiírás (2 = special)
    for i in matrixtext:
        V5(i[0], ul, ld)

def centerText(rn): # rn = rownr., 1. vagy 2.; ha 3, akkor egy soros
    global segedpixel
    # a mátrixba írós függvény azon része, ami megmondja, hogy milyen hosszú a szöveg
    for i in matrixtext:
        if rn != 3:
            segedpixel += len(letterdict2[i[0]][1])-1
        else:
            segedpixel += len(letterdict[i[0]][1])-1
    diff[rn] = segedpixel
    # ez itt a szöveg végéből a kezdetét kivonja, így megkapva a hosszúságát, majd azt a columns változóból
    # kivonva és kettővel elosztva, majd hozzáadva a szöveg kezdetét megkapható, 
    # hogy mennyi indent kell ahhoz, hogy relatíve középen legyen
    segedpixel = (COLUMNS - (diff[rn] - diff[0]) + diff[0])//2
    diff[rn] = segedpixel
    diff[0] = segedpixel

def tesztDraw():
    drawDisplay()
    time.sleep(1)
    os.system('cls' if os.name == "nt" else 'clear')
    clearDisplay()

def kijelzoTeszt():
    os.system('clear')
    for i in range(ROWS):
        for j in range(COLUMNS):
            matrix[i][j] = COLORED
    tesztDraw()
    for i in range(ROWS):
        for j in range(COLUMNS):
            if i % 2 == 0:
                if j % 2 == 0:
                    matrix[i][j] = COLORED
            else:
                if j % 2 == 1:
                    matrix[i][j] = COLORED
    tesztDraw()
    for i in range(ROWS):
        for j in range(COLUMNS):
            if i % 2 == 0:
                matrix[i][j] = COLORED
    tesztDraw()
    for i in range(ROWS):
        for j in range(COLUMNS):
            if i % 2 == 1:
                matrix[i][j] = COLORED
    tesztDraw()
    for i in range(ROWS):
        for j in range(COLUMNS):
            if j % 2 == 0:
                matrix[i][j] = COLORED
    tesztDraw()
    for i in range(ROWS):
        for j in range(COLUMNS):
            if j % 2 == 1:
                matrix[i][j] = COLORED
    tesztDraw()
    for i in range(ROWS):
        for j in range(COLUMNS):
            matrix[i][j] = COLORED
        drawDisplay()
        time.sleep(0.5)
        os.system('cls' if os.name == "nt" else 'clear')
    for i in range(ROWS):
        for j in range(COLUMNS):
            matrix[i][j] = BASE
        drawDisplay()
        time.sleep(0.5)
        os.system('cls' if os.name == "nt" else 'clear')


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
            "-lns,  --specialln=STR     replaces the line number with a custom set of pixels from 'special-1row.txt'\n"
            "-r,    --row=STR           one-row mode: displays text in one row in the middle\n"
            "-ri,   --rowinvert         inverts the displayed text in the main row"
            "-ur,   --upperrow=STR      upper-row mode: displays text in the upper row of the display\n"
            "-uri,  --upperinvert       inverts the displayed text in the upper row\n"
            "-lr,   --lowerrow=STR      lower-row mode: displays text in the lower row of the display\n"
            "-lri,  --lowerinvert       inverts the displayed text in the lower row"
            "-t,    --test              display test: tests the display by turning on or off different pixels\n"
            "-s,    --save=FILE         save the display in a file in the folder from which you run this script\n"
            "-l,    --load=FILE         load another display from a file in the folder from which you run this script\n"
            "-c,    --center            centers the text (doesn't include line number)\n"
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
        textToMatrix(0, 1)
        segedpixel += 3

    elif(sys.argv[i] == "-lns" or sys.argv[i] == "--specialln"):
        matrixtext = [i.split() for i in sys.argv[i+1]]
        textToMatrix(0,2)
        segedpixel += 3

    elif(sys.argv[i] == "-r" or sys.argv[i] == "--row"):
        matrixtext = [i.split() for i in sys.argv[i+1]]
        diff[0] = segedpixel
        for j in sys.argv:
            if j == "-c":
                centerText(3)
        textToMatrix(0, 1)

    elif(sys.argv[i] == "-ri"):
        for j in range(20):
            for k in range(diff[3]-2, segedpixel+1):
                if matrix[j][k] == COLORED:
                    matrix[j][k] = BASE
                else:
                    matrix[j][k] = COLORED

    elif(sys.argv[i] == "-ur" or sys.argv[i] == "--upperrow"):
        matrixtext = sys.argv[i+1]
        diff[0] = segedpixel
        diff[4] = diff[0]
        diff[1] = diff[0]
        for j in sys.argv:
            if j == "-c":
                centerText(1)
        textToMatrix(0, 0)

    elif(sys.argv[i] == "-uri"):
        for j in range(10):
            for k in range(diff[1]-2, segedpixel+1):
                if matrix[j][k] == COLORED:
                    matrix[j][k] = BASE
                else:
                    matrix[j][k] = COLORED

    elif(sys.argv[i] == "-lr" or sys.argv[i] == "--lowerrow"):
        matrixtext = sys.argv[i+1]
        segedpixel = diff[4]
        diff[0] = diff[4]
        diff[2] = diff[4]
        for j in sys.argv:
            if j == "-c":
                centerText(2)
        textToMatrix(9, 0)

    elif(sys.argv[i] == "-lri"):
        for j in range(10, 20):
            for k in range(diff[2]-2, segedpixel+1):
                if matrix[j][k] == COLORED:
                    matrix[j][k] = BASE
                else:
                    matrix[j][k] = COLORED

    elif(sys.argv[i] == "-s"):
        output = open(f"{sys.argv[i+1]}", "w", encoding="utf8")
        for i in range(ROWS):
            for j in range(COLUMNS):
                print(matrix[i][j])
                output.write("1" if "■" in matrix[i][j] else "0")
            output.write("\n")

    elif(sys.argv[i] == "-l"):
        loadtext = open(f"{sys.argv[i+1]}", "r", encoding="utf8").readlines()
        for j in range(len(loadtext)):
            for k in range(len(loadtext[5])):
                if loadtext[j][k] == "1":
                    matrix[j][k] = COLORED

drawDisplay()

#seged = input("text: ")
#lista = [i.split() for i in seged]

# kérlek ezt nézd meg és magyarázd el, hogy itt mi a keserves faszt csináltam véletlenül, amitől elkezdett működni
# annyit tudok fixen, hogy ránéztem a mai infos alkotásodra és mondom hátha kihagyhatom a range(len...) részt belőle
# de mondom ez magában kevés lesz, akkor kéne a segéd hozzá, ami így utólag ránézve semmit nem csinál
# így utólag nem tudom, hogy ez mégis miért működik, az én olvasatom szerint ez minden, csak nem egy működő 2 sor
#for i in matrixtext:
#    V5(i[0])

# itt az előző, viszonyítás gyanánt
#for i in range(len(lista)):
#    V5(lista[i])    # ez az, ami soha nem működött, de ezt szerettem volna
#    V5(seged)       # ez működött, de csak részben érte el a célját (egy karakter limit)

# soronként invert
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


# ■
