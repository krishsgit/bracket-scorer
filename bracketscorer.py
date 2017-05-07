#!/usr/local/bin/python3
import sys
import time

import pygame
from pygame.locals import *
from bracketscorerconfig import *




class Team(object):
    def __init__(self, name=""):
        self.name = name
        self.score = 0
        self.status = ""
        self.quadmotor = False
        self.color = BLUE
        self.playingnow = False
        self.roundsplayed = 0
        self.penalty = 0
        self.won = False

    def add(self):
        self.button = teamButton[self.name]
        self.button.add(textorientation="top")
        statusfontclr = STATUSFONTCLRPLAYING
        if (self.playingnow):
            self.status = "Now playing round #" + str(self.roundsplayed + 1)
        elif (self.roundsplayed == 1):
            self.status = "Completed " + str(self.roundsplayed) + " round"
            statusfontclr = STATUSFONTCLRCOMPLETED
        elif (self.roundsplayed > 1):
            self.status = "Completed " + str(self.roundsplayed) + " rounds"
            statusfontclr = STATUSFONTCLRCOMPLETED
        statusfontsz = scorefontsz = int(self.button.width/11)
        if(statusfontsz > 18):
            statusfontsz = scorefontsz = 18
        self.button.display.font = pygame.font.SysFont(STATUSFONT, statusfontsz,italic=True)
        text = self.button.display.font.render(self.status, True, statusfontclr)
        textpos = text.get_rect()
        textpos.centerx = self.button.rect.centerx
        textpos.centery = self.button.rect.centery + int(SBHEIGHT/500)*PADDING
        self.button.display.screen.blit(text, textpos)
        if (self.roundsplayed > 0):
            self.button.display.font = pygame.font.SysFont(SCOREFONT, scorefontsz)
            if (self.won):
                text = self.button.display.font.render("Won this round", True, SCOREFONTCLR)
                textpos = text.get_rect()
                textpos.centerx = self.button.rect.centerx
                textpos.centery = self.button.rect.centery + int(SBHEIGHT/150)*PADDING
                self.button.display.screen.blit(text, textpos)

    update = add

class Button(object):
    def __init__(self, display, left, top, width, height, name, color=OFFWHITE, font=DEFAULTFONT, fontsize=30, fontcolor=BLACK):
        self.display = display
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.name = name
        self.subname = ""
        self.color = color
        self.font = font
        self.fontsize = fontsize
        self.fontcolor = fontcolor
        self.textx = self.left + (self.width - self.fontsize/2 * len(self.name))/2 - 4*PADDING
        self.texty = self.top + (self.height - self.fontsize)/2
        pass

    def add(self, textorientation=None):
        self.rect = pygame.draw.rect(self.display.screen, self.color, (self.left, self.top, self.width, self.height))
        self.display.font = pygame.font.SysFont(self.font, self.fontsize)
        text = self.display.font.render(self.name, True, self.fontcolor)
        textpos = text.get_rect()
        textpos.centerx = self.rect.centerx
        if (textorientation=="top"):
            textpos.top = self.top + PADDING
        else:
            textpos.centery = self.rect.centery
        self.display.screen.blit(text, textpos)
        if self.subname != "":
            self.display.font = pygame.font.SysFont(self.font, int(self.fontsize/2))
            subtext = self.display.font.render(self.subname, True, RED)
            textpos = subtext.get_rect()
            textpos.centerx = self.rect.centerx
            if (textorientation=="top"):
                textpos.top = self.top + int(self.fontsize/2) + PADDING
            else:
                textpos.centery = self.rect.centery + int(self.fontsize/2) + PADDING
            self.display.screen.blit(subtext, textpos)
        pygame.display.update()

    update = add

class Scoreboard(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont(DEFAULTFONT, 25)
        pygame.display.set_caption(SCOREBOARDTITLE)
        self.screen = pygame.display.set_mode(SCOREBOARDSIZE, 0, 32)
        self.screen.fill(OFFWHITE)
        self.toprect = pygame.draw.rect(self.screen, BLACK, (PADDING, PADDING, AREAWIDTH, TOPAREAHEIGHT), 2)
        self.logoimage = pygame.image.load(LOGOIMAGE)
        self.logoleft = 2*PADDING
        self.logotop = 2*PADDING
        self.logowidth = int(AREAWIDTH - CLOCKWIDTH - CLOCKBUTTONWIDTH - 2*PADDING)
        self.logoheight = CLOCKHEIGHT
        self.logoimagerect = self.logoimage.get_rect()
        self.screen.blit(self.logoimage, (int(self.logowidth - self.logoimagerect.width)/2,self.logotop))
        self.org = Button(self, self.logoleft, self.logotop + self.logoimagerect.height + PADDING, self.logowidth, int((self.logoheight - self.logoimagerect.height)/2) - PADDING, ORGNAME, font=ORGNAMEFONT,  fontsize=ORGNAMEFONTSZ, fontcolor=ORGNAMEFONTCLR)
        self.org.add()
        self.game = Button(self, self.logoleft, self.logotop + self.logoimagerect.height + self.org.height + PADDING, self.logowidth, int((self.logoheight - self.logoimagerect.height)/2) - PADDING, GAMENAME, font=GAMENAMEFONT, fontsize=GAMENAMEFONTSZ, fontcolor=GAMENAMEFONTCLR)
        self.game.add()

class TeamArea():
    def __init__(self, display):
        self.display = display
        self.left = PADDING
        self.top = SBHEIGHT - TEAMAREAHEIGHT - PADDING
        self.width = TEAMAREAWIDTH
        self.height = TEAMAREAHEIGHT
        self.rect = pygame.draw.rect(display.screen, WHITE, (self.left, self.top, self.width, self.height))
        self.rect = pygame.draw.rect(display.screen, BLACK, (self.left, self.top, self.width, self.height), 2)
        teamboxleft = 3*PADDING
        teamboxtop = SBHEIGHT - TEAMAREAHEIGHT
        buttonsinrow = int ((len(felteams) + 3 - len(felteams)%3)/3)
        teambuttonwidth = int(TEAMAREAWIDTH / buttonsinrow - 2*PADDING)
        fontsize = fitfontsize(self.display, TEAMFONT, teambuttonwidth - PADDING, TEAMBUTTONHEIGHT)
        for team in felteams:
            teamButton[team] = Button(scoreboard, teamboxleft,teamboxtop, teambuttonwidth,TEAMBUTTONHEIGHT, team, color=TEAMBUTTONCLR, fontsize=fontsize)
            felteam[team].update()
            teamboxleft += teambuttonwidth + PADDING
            if (teamboxleft + teambuttonwidth) > TEAMAREAWIDTH :
                teamboxleft = 3*PADDING
                teamboxtop += TEAMBUTTONHEIGHT + PADDING

class GameArea():
    def __init__(self, display):
        self.display = display
        self.currentround = 0
        self.left = PADDING
        self.top = SBHEIGHT - TEAMAREAHEIGHT - PADDING - GAMEAREAHEIGHT
        self.width = GAMEAREAWIDTH
        self.height = GAMEAREAHEIGHT
        self.rect = pygame.draw.rect(self.display.screen, WHITE, (self.left, self.top, self.width, self.height))
        self.rect = pygame.draw.rect(self.display.screen, BLACK, (self.left, self.top, self.width, self.height), 2)
        self.roundButton = Button(self.display, self.left + 4*PADDING, self.top + PADDING, self.width - 8*PADDING, ROUNDHEIGHT, "", color=WHITE, font=ROUNDFONT, fontcolor=ROUNDFONTCOLOR, fontsize=ROUNDFONTSZ )
        fontsize = fitfontsize(self.display, GAMETEAMFONT, GAMETEAMWIDTH, GAMEAREAHEIGHT - PADDING)
        self.teamplaying = [ ]
        # Create a button for the first team and store it in the first index of a list
        self.teamplaying.append(
            Button(self.display, self.left + PADDING, self.top + ROUNDHEIGHT + 2 * PADDING,
                   GAMETEAMWIDTH, GAMETEAMHEIGHT, "Pick team", color=RED, font=GAMETEAMFONT,
                   fontsize=fontsize, fontcolor=GAMETEAMFONTCLR))
        # Create a button for the seond team and store it in the second index of the list
        self.teamplaying.append(
            Button(self.display, self.left + self.width - GAMETEAMWIDTH - PADDING, self.top + ROUNDHEIGHT + 2 * PADDING,
                   GAMETEAMWIDTH, GAMETEAMHEIGHT, "Pick team", color=BLUE, font=GAMETEAMFONT,
                   fontsize=fontsize, fontcolor=GAMETEAMFONTCLR))
        self.teamplaying.append(
            Button(self.display, self.left + PADDING, self.top + ROUNDHEIGHT + GAMETEAMHEIGHT + 4 * PADDING,
                   GAMETEAMWIDTH, GAMETEAMHEIGHT, "Pick team", color=GREEN, font=GAMETEAMFONT,
                   fontsize=fontsize, fontcolor=GAMETEAMFONTCLR))
        self.teamplaying.append(
            Button(self.display, self.left + self.width - GAMETEAMWIDTH - PADDING, self.top + ROUNDHEIGHT + GAMETEAMHEIGHT + 4 * PADDING,
                   GAMETEAMWIDTH, GAMETEAMHEIGHT, "Pick team", color=BROWN, font=GAMETEAMFONT,
                   fontsize=fontsize, fontcolor=GAMETEAMFONTCLR))
        #self.versusButton = Button(self.display, self.left + int(self.width/2) - PADDING,
        #                     self.top + ROUNDHEIGHT + 2 * PADDING,
        #                    20, GAMETEAMHEIGHT, "vs.", color=WHITE, font=GAMETEAMFONT,
        #                    fontsize=VERSUSFONTSZ, fontcolor=BLACK)

    def update(self, currentround=0):
        self.currentround = currentround
        if (self.currentround == 0):
            self.roundButton.name = ""
        else:
            self.roundButton.name = "Round #" + str(self.currentround)
        self.roundButton.add()
        self.teamplaying[0].add()
        self.teamplaying[1].add()
        self.teamplaying[2].add()
        self.teamplaying[3].add()
        #self.versusButton.add()

class GameClock(object):
    def __init__(self, display):
        self.left = int(AREAWIDTH - 2*PADDING - CLOCKWIDTH - CLOCKBUTTONWIDTH)
        self.top = PADDING
        self.controls = ['Start', 'Finish', 'Penalty']
        self.button = {}
        self.elapsedtime = 0
        self.lapstart = time.time()
        self.stoppedtime = 0
        self.clockReset = False
        self.clockStopped = False
        self.display = display
        self.penalty = 0
        self.timedisplay="0.00"
        self.button['Start'] = Button(self.display, self.left + CLOCKWIDTH + PADDING, self.top + 2*PADDING, CLOCKBUTTONWIDTH , CLOCKBUTTONHEIGHT, "Start", color=CLKBTNCLR, font=CLKBTNFONT, fontsize=CLKBTNFNTSZ, fontcolor=CLKBTNFNTCLR)
        self.button['Start'].add()
        self.button['Reset'] = Button(self.display, self.left + CLOCKWIDTH + PADDING, self.top + 3*PADDING + CLOCKBUTTONHEIGHT, CLOCKBUTTONWIDTH , CLOCKBUTTONHEIGHT, "Reset", color=CLKBTNCLR, font=CLKBTNFONT, fontsize=CLKBTNFNTSZ, fontcolor=CLKBTNFNTCLR)
        self.button['Reset'].add()
        self.button['OT'] = Button(self.display, self.left + CLOCKWIDTH + PADDING, self.top + 4*PADDING + 2*CLOCKBUTTONHEIGHT, CLOCKBUTTONWIDTH , CLOCKBUTTONHEIGHT, "OT", color=CLKBTNCLR, font=CLKBTNFONT, fontsize=CLKBTNFNTSZ, fontcolor=CLKBTNFNTCLR)

        #self.button['Penalty'] = Button(self.display, self.left + CLOCKWIDTH + PADDING, self.top + 5*PADDING + 3*CLOCKBUTTONHEIGHT, CLOCKBUTTONWIDTH , CLOCKBUTTONHEIGHT, "Penalty", color=CLKBTNCLR, font=CLKBTNFONT, fontsize=CLKBTNFNTSZ, fontcolor=CLKBTNFNTCLR)
        #self.button['Penalty'].add()
        self.clock = Button(self.display, self.left, self.top + 3 * PADDING, CLOCKWIDTH, CLOCKHEIGHT,"", CLOCKCOLOR, font=CLOCKFONT, fontsize=CLOCKFONTSZ, fontcolor=CLOCKFONTCLR)
        self.reset()

    def start(self):
        waitOnButton(self.button['Start'])
        self.button['Start'].name = "Stop"
        self.button['Start'].color = STOPCOLOR
        self.button['Start'].add()
        self.timerrun(GAMETIMESECS)

    def timerrun(self, timelength):
        self.roundstart = time.time()
        self.roundend = self.roundstart + timelength
        self.lapstart = time.time()
        timeleft = timelength
        penaltytime = 0
        while (not self.clockReset and timeleft > 0):
            if (not self.clockStopped):
                self.elapsedtime = self.stoppedtime + time.time() - self.lapstart + penaltytime
            else:
                self.clockStopped = False
            timeleft = timelength - self.elapsedtime
            if timeleft <= 0:
                self.clock.name = "TIME!"
            else:
                self.clock.name = str("%4.1f" % timeleft)

            self.clock.update()

            for control in self.controls:
                clockButtonPressed = whichButtonPressedClock(self.button['Start'], self.button['Reset'])
                if (clockButtonPressed == 'Stop'):
                    self.stoppedtime = self.elapsedtime
                    self.stop()
                    self.lapstart = time.time()
                    if self.clockReset:
                        self.reset()
                elif (clockButtonPressed == 'Reset'):
                    self.reset()
                    self.clockReset = True
                elif (clockButtonPressed == 'Bonus'):
                    self.elapsedtime -= BONUSPTS
                    self.reset()
                    self.clockReset = True
                elif (clockButtonPressed == 'Penalty'):
                    self.penalty += 1
                    self.showpenalty()
                    penaltytime += PENALTYPTS

        if (timeleft <= 0):
            print( "Timer ran out - go to OT")
            self.button['OT'].add()
            waitOnButton(self.button['OT'])
            self.timerrun(OTSECS)


    def showpenalty(self):
        if self.penalty > 0:
            self.button['Penalty'].subname = str(self.penalty)
            self.button['Penalty'].update()


    def stop(self):
        print("GAME STOPPED")
        self.button['Start'].name = "Start"
        self.button['Start'].color = CLKBTNCLR
        self.button['Start'].add()
        self.clockStopped = True
        clockButtonPressed = waitOnButtonsClock(self.button['Start'], self.button['Reset'])
        if clockButtonPressed == 'Start':
            self.button['Start'].name = "Stop"
            self.button['Start'].color = STOPCOLOR
            self.button['Start'].add()
            return
        else:
            self.clockReset = True
            return

    def reset(self):
        self.button['Start'].name = "Start"
        self.button['Start'].color = CLKBTNCLR
        self.button['Start'].update()
        #self.button['Penalty'].subname = ""
        #self.button['Penalty'].update()
        self.penalty = 0
        self.clock.name = str("%4.1f" % (GAMETIMESECS))
        self.clock.update()


class LeaderBoard():
    def __init__(self,display):
        self.display = display
        self.left = SBWIDTH - LDRBRDWIDTH - PADDING
        self.top = PADDING
        self.width = LDRBRDWIDTH
        self.height = LDRBRDHEIGHT
        self.rect = pygame.draw.rect(display.screen, BLACK, (self.left, self.top, self.width, self.height),2)
        #Calculate button height
        self.leaderheight = int(LDRBRDHEIGHT/(len(felteams) +1) - PADDING)
        self.leaderfontsz = fitfontsize(self.display, LDRFONT, self.width - 4*PADDING, self.leaderheight, LDRNAME)
        self.leaderboardlabel = Button(self.display, self.left+PADDING, 2*PADDING, self.width - 2*PADDING, self.leaderheight, LDRNAME, font=LDRFONT, fontsize=self.leaderfontsz, fontcolor=LDRNAMECLR)
        self.leaderboardlabel.add("top")
        self.leaderbutton = {}
        self.update()

    def pick(self):
        self.leads = []
        for team in felteams:
            if felteam[team].won:
                self.leads.append(team)

    def update(self):
        self.pick()
        teamboxheight = 3*PADDING + self.leaderboardlabel.height
        for leader in self.leads:
            if felteam[leader].status == "":
                color = VERYLTGRAY
                fontcolor = WHITE
            else:
                color = LDRCOLOR
                fontcolor = LDRFONTCLR
            self.leaderbutton[leader] = Button(self.display, self.left + PADDING, teamboxheight, self.width - 2*PADDING, self.leaderheight, leader, color=color, font=LDRFONT, fontsize=self.leaderfontsz, fontcolor=fontcolor)
            teamboxheight += self.leaderheight + PADDING
            self.leaderbutton[leader].add()
        pass

def getteams():
    felteamfile = open(FELTEAMSFILE, 'r')
    felteams = felteamfile.read().split()
    for team in felteams:
        felteam[team] = Team(name=team)
    return felteams

def pickTeam(currentround):
    team = waitOnButtons(teamButton.values())
    while felteam[team].roundsplayed >= currentround or felteam[team].playingnow:
        team = waitOnButtons(teamButton.values())
    return team

def pickWinner(gameButtons):
    team = waitOnButtons(gameButtons)
    return team


def getMousePosition():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            return pos

def waitOnButton(button):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if (button.rect.collidepoint(pos)):
                    return button.name

def waitOnButtons(buttonlist):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for button in buttonlist:
                    if (button.rect.collidepoint(pos)):
                        return button.name

def waitOnButtonsClock(button1, button2):
    buttonlist = []
    buttonlist.append(button1)
    buttonlist.append(button2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit();
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for button in buttonlist:
                    if (button.rect.collidepoint(pos)):
                        return button.name

def buttonPressed(button):
    pos = getMousePosition()
    if (button.rect.collidepoint(pos)):
        return True

def whichButtonPressedClock(button1, button2):
    buttonlist = []
    buttonlist.append(button1)
    buttonlist.append(button2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for button in buttonlist:
                #print(button)
                if (button.rect.collidepoint(pos)):
                    return button.name

def fitfontsize(display, font, width, height, textstr="OOOOOOOOOO"):
    for fontsize in range(1,300):
        display.font = pygame.font.SysFont(font, fontsize)
        text = display.font.render(textstr, True, WHITE)
        textpos = text.get_rect()
        if (textpos.width > width) or (textpos.height > height/2):
            return fontsize - 1

if __name__ == '__main__':

#Initialize the scoreboard
    felteams = getteams()
    scoreboard = Scoreboard()
    teamarea = TeamArea(scoreboard)
    gamearea = GameArea(scoreboard)
    leaderboard = LeaderBoard(scoreboard)
    teamsplayed = 0

# Input the initial teams
    for currentround in range(1,MAXROUNDS+1):
        teamsplayed = 0
        while teamsplayed < len(felteams):
            teaminplay = ["", "", "", ""]
            teamsthisround = int(input("How many teams are playing this round?"))
            #print(teamsthisround)

            for i in range(0, teamsthisround):
                gamearea.teamplaying[i].name = "Pick team"
                gamearea.update(currentround)

            if teamsthisround < 4:
                for i in range (teamsthisround,4):
                    gamearea.teamplaying[i].name = "No Player"
                    gamearea.update(currentround)

            for i in range(0,teamsthisround):
                teaminplay[i] = pickTeam(currentround)
                felteam[teaminplay[i]].update()
                gamearea.teamplaying[i].name= teaminplay[i]
                gamearea.update()
                felteam[teaminplay[i]].playingnow = True
                felteam[teaminplay[i]].update()

            gameclock = GameClock(scoreboard)
            gameclock.start()
            #print("Time in round {%d} is {%f}" % (currentround, gameclock.elapsedtime))

            winningTeam = pickWinner(gamearea.teamplaying)
            felteam[winningTeam].won = True
            print("The winner on this game is " + winningTeam)

            for i in range(0, teamsthisround):
                felteam[teaminplay[i]].roundsplayed = currentround
                felteam[teaminplay[i]].playingnow = False
                felteam[teaminplay[i]].update()
            leaderboard.update()

    gamearea.teamplaying.name="GAME OVER"
    gamearea.update()
    time.sleep(100)
