BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DKGREEN = (0, 100, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
DKGRAY = (64, 64, 64)
LTGRAY = (196, 196, 196)
VERYLTGRAY = (211, 211, 211)
BROWN = (92, 64, 51)
TEAL = (2, 132, 130)
GOLD = (212, 175, 55)
ORANGE = (255, 128, 0)
DARKORANGE = (255, 140, 0)
ROYALBLUE = (65, 105, 225)
FORESTGREEN = (34, 139, 34)
OFFWHITE = (245, 245, 245)
UCLABLUE = (50,132, 191 )
UCLAGOLD = (255,232,0)
UCLAPINK = (255,0,165)
UCLADKBLUE = (0,85,166)
UCLAORANGE = (254,187,54)
UCLAGREEN = (0,255,135)
UCLAMDBLUE = (0,165,229)


SCOREBOARDTITLE = "Fallon Engineering Lab"
FELTEAMSFILE = "teams.txt"
SAVEFILE="gamesave.txt"
LOGOIMAGE = "mustang.png"
SBWIDTH = 1280
SBHEIGHT = 780
PADDING = 5
SCOREBOARDSIZE = (SBWIDTH, SBHEIGHT)
AREAWIDTH = int(SBWIDTH * 3 / 4) - 6 * PADDING
DEFAULTFONT = 'Arial'



TOPAREAHEIGHT = int(SBHEIGHT / 3)
ORGNAME = "Fallon Engineering Lab"
ORGNAMEFONT = DEFAULTFONT
ORGNAMEFONTSZ = int(AREAWIDTH / 40)
ORGNAMEFONTCLR = BLACK
GAMENAME = "BALLOON POP"
GAMENAMEFONT = DEFAULTFONT
GAMENAMEFONTSZ = int(AREAWIDTH / 20)
GAMENAMEFONTCLR = UCLAORANGE

GAMEAREAHEIGHT = int(SBHEIGHT / 3)
GAMEAREAWIDTH = AREAWIDTH
GAMETEAMWIDTH = int(GAMEAREAWIDTH/2) - 10 * PADDING
GAMETEAMHEIGHT = int(GAMEAREAHEIGHT * 2 / 6 - 4 * PADDING)
ROUNDHEIGHT = GAMEAREAHEIGHT - GAMETEAMHEIGHT * 2 - 4 * PADDING
GAMETEAMFONT = DEFAULTFONT
GAMETEAMFONTSZ = int(GAMETEAMWIDTH / 32)
GAMETEAMFONTCLR = WHITE
GAMETEAMCOLOR = UCLABLUE
VERSUSFONTSZ = int(GAMEAREAWIDTH/24)
ROUNDFONT = DEFAULTFONT
ROUNDFONTSZ = ROUNDHEIGHT - 10 * PADDING
ROUNDFONTCOLOR = DKGRAY

TEAMAREAHEIGHT = int(SBHEIGHT / 3)
TEAMAREAWIDTH = AREAWIDTH
TEAMBUTTONHEIGHT = int(TEAMAREAHEIGHT / 3 - PADDING)
TEAMFONT=DEFAULTFONT
#TEAMFONTSZ = int(TEAMBUTTONHEIGHT / 4.3)
TEAMFONTSZ =  20
TEAMFONTCLR = BLACK
TEAMBUTTONCLR=UCLAGOLD
STATUSFONT='Helvetica'
STATUSFONTSZ = int(TEAMBUTTONHEIGHT / 5)
STATUSFONTCLRCOMPLETED = RED
STATUSFONTCLRPLAYING = DKGREEN
SCOREFONT=DEFAULTFONT
SCOREFONTSZ = int(TEAMBUTTONHEIGHT / 5)
SCOREFONTCLR = DKGRAY

CLOCKWIDTH = int(AREAWIDTH / 2)
CLOCKHEIGHT = int(SBHEIGHT / 3) - 8 * PADDING
CLOCKBUTTONWIDTH = int(CLOCKWIDTH / 5) - PADDING
CLOCKBUTTONHEIGHT = int(CLOCKHEIGHT / 4 - PADDING / 4)
CLOCKCOLOR = UCLABLUE
CLOCKFONT = DEFAULTFONT
CLOCKFONTSZ = int(CLOCKWIDTH / 3)
CLOCKFONTCLR = WHITE
CLKBTNCLR = UCLAGOLD
STOPCOLOR = UCLABLUE
CLKBTNFONT = DEFAULTFONT
CLKBTNFNTSZ = int(CLOCKBUTTONWIDTH / 4)
CLKBTNFNTCLR = BLACK

LDRBRDHEIGHT = SBHEIGHT - 2 * PADDING
LDRBRDWIDTH = SBWIDTH - AREAWIDTH - 2 * PADDING
LDRNAME = "WINNER"
LDRFONT = DEFAULTFONT
LDRNAMECLR = DKGRAY
LDRFONTCLR = WHITE
LDRCOLOR = UCLADKBLUE

GAMETIMESECS = 120
OTSECS = 30
teamButton = {}
felteam = {}
gameAreaButton = {}

MAXROUNDS = 1
PENALTYPTS = 5
BONUSPTS = 10