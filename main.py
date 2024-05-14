import time 
from digitalio import DigitalInOut, Direction
import board
from random import randint
class Timer: #to get a stopwatch
    def __init__(self) -> None:
        self.startTime = None
        self.pauseTime = None
        self.elapsedTime = 0

    def start(self) -> None: #also resumes timer
        self.startTime = time.time()
        self.pauseTime = 0
    
    def pause(self) -> None:
        self.pauseTime = time.time()
        self.elapsedTime = self.pauseTime - self.startTime
        self.startTime = None

    def restart(self) -> None:
        self.start_time = time.time()
        self.elapsed_time = 0

    def elapsed(self):
        if self.start_time is not None:
            return time.time() - self.start_time + self.elapsed_time
        return self.elapsed_time


timer = Timer()

class Simon:

    #innit must put the game in a sleep state that allows the player to play whenever he wants
    def __init__(self) -> None:
        self.button0 = DigitalInOut(board.GP1)
        self.button1 = DigitalInOut(board.GP5)
        self.button2 = DigitalInOut(board.GP9)
        self.button3 = DigitalInOut(board.GP13)

        self.button0Power = DigitalInOut(board.GP0)
        self.button1Power = DigitalInOut(board.GP4)
        self.button2Power = DigitalInOut(board.GP8)
        self.button3Power = DigitalInOut(board.GP12)

        self.button0 = Direction.INPUT
        self.button1 = Direction.INPUT
        self.button2 = Direction.INPUT
        self.button3 = Direction.INPUT

        self.button0Power = Direction.OUTPUT
        self.button1Power = Direction.OUTPUT
        self.button2Power = Direction.OUTPUT
        self.button3Power = Direction.OUTPUT




    def start(self) -> None:
        self.timeLimit = 0 #maybe increase it in function of time ?
        self.counter = 0
        self.level = 1
        self.gameList = []
        for i in range(self.level):
            self.gameList.append(randint(0, 3))

    def showingColors(self) -> None:
        for i in range(len(self.gameList)):
            if self.gameList[i] == 0:
                #lights LED
                #buzzes
                #sleeps
                pass
            if self.gameList[i] == 1:
                #lights LED
                #buzzes
                #sleeps
                pass
            if self.gameList[i] == 2:
                #lights LED
                #buzzes
                #sleeps
                pass
            if self.gameList[i] == 3:
                #lights LED
                #buzzes
                #sleeps
                pass

    def inputColors(self) -> None:
        
        timer.start()
        while self.counter < len(self.gameList):
            if timer.elapsed >= self.timeLimit:
                pass #GameOver

            if 
        





simon = Simon()
