import time 
from digitalio import DigitalInOut, Direction
import board
import simpleio
from random import randint

class Timer: #to get a stopwatch
    def __init__(self) -> None:
        self.startTime = None
        self.pauseTime = None
        self.elapsedTime = 0
        self.startFlag = False

    def start(self) -> None: #also resumes timer
        self.startTime = time.time()
        self.pauseTime = 0
        
    
    def pause(self) -> None:
        self.pauseTime = time.time()
        self.elapsedTime += self.pauseTime - self.startTime
        self.startTime = None
        self.startFlag = False

    def restart(self) -> None:
        self.startTime = time.time()
        self.elapsedTime = 0

    def elapsed(self):
        if self.startTime is not None:
            return time.time() - self.startTime + self.elapsedTime
        return self.elapsedTime


timer = Timer()

class Simon:

    #innit must put the game in a sleep state that allows the player to play whenever he wants
    def __init__(self) -> None:
        self.button0 = DigitalInOut(board.GP1)      #Enable input pins for the buttons. Don't forger that the 
        self.button1 = DigitalInOut(board.GP5) 
        self.button2 = DigitalInOut(board.GP9)
        self.button3 = DigitalInOut(board.GP13)

        # self.button0Power = DigitalInOut(board.GP0)     # Enable button power's pins 
        # self.button1Power = DigitalInOut(board.GP4)
        # self.button2Power = DigitalInOut(board.GP8)
        # self.button3Power = DigitalInOut(board.GP12)

        self.button0.direction = Direction.INPUT
        self.button1.direction = Direction.INPUT
        self.button2.direction = Direction.INPUT
        self.button3.direction = Direction.INPUT


        # self.button0Power.direction = Direction.OUTPUT 
        # self.button1Power.direction = Direction.OUTPUT
        # self.button2Power.direction = Direction.OUTPUT
        # self.button3Power.direction = Direction.OUTPUT

        # self.button0Power.value = True # gives 3_3V DC to the buttons 
        # self.button3Power.value = True
        # self.button2Power.value = True
        # self.button1Power.value = True


        # ----------- LEDs -------------


        # LEDs Placement 
        #
        #   led0  |  led3
        #   ------|-------  
        #   led1  |  led2

        self.led0 = DigitalInOut(board.GP2) # Allows us to turn on/off the 4 diodes of the device
        self.led1 = DigitalInOut(board.GP6)
        self.led2 = DigitalInOut(board.GP10)
        self.led3 = DigitalInOut(board.GP14)

        self.led0.direction = Direction.OUTPUT
        self.led1.direction = Direction.OUTPUT
        self.led2.direction = Direction.OUTPUT
        self.led3.direction = Direction.OUTPUT


        # # ----------- Buzzer -------------

        self.buzzerPin = board.GP17
        self.tones = [ 262,  # C4
              294,  # D4
              330,  # E4
              349,  # F4
              392,  # G4
              440,  # A4
              494 ] # B4

        
        #Some variables that must be declared on boot 

        self.level = 1 # Allows us to increase difficulty as you win games
        self.timeLimit = self.level + 1 #time limit wich is one second longer at each iteration of level
        self.winFlag = True # Gives indication whenever to quit to the sleep animation, or to continue

    def start(self) -> None:
        print("start")
        simpleio.tone(self.buzzerPin, self.tones[0], duration=0.1)
        simpleio.tone(self.buzzerPin, self.tones[4], duration=0.5)

        self.counter = 0
        self.gameList = []
        self.inputList = []

        #long beep to say "ready"
        self.led0.value = True
        self.led1.value = True
        self.led2.value = True
        self.led3.value = True
        time.sleep(1)
        self.led0.value = False
        self.led1.value = False
        self.led2.value = False
        self.led3.value = False

        

    def showingColors(self) -> None:

        
        print("showing colors")
        for i in range(self.level): #stock the position of the blinking LEDs
            self.gameList.append(randint(0, 3))


        for i in range(len(self.gameList)):
            if self.gameList[i] == 0: #----- Add buzzes on each LED activation (of a different tone)

                
                self.led0.value = True 
                simpleio.tone(self.buzzerPin, self.tones[0], duration=0.4) #works as a sleep
                self.led0.value = False
                
            if self.gameList[i] == 1:

                
                self.led1.value = True
                simpleio.tone(self.buzzerPin, self.tones[2], duration=0.4)
                self.led1.value = False
                
            if self.gameList[i] == 2:

                
                self.led2.value = True
                simpleio.tone(self.buzzerPin, self.tones[4], duration=0.4)
                self.led2.value = False
                
            if self.gameList[i] == 3:

                
                self.led3.value = True
                simpleio.tone(self.buzzerPin, self.tones[6], duration=0.4)
                self.led3.value = False
                
        

    def inputColors(self) -> None:
        print("input")
        timer.start()

        # while self.counter < len(self.gameList):
        #     print(timer.elapsed())
            
        #for i in range(len(self.gameList)):
        while len(self.inputList) != len(self.gameList):
            

            isButtonPressed = False
            
            while not isButtonPressed:
                
                time.sleep(0.4)
                if timer.elapsed() >= self.timeLimit:
                    print("to slow")
                    self.loseAnimation()
                     # Leaves the loop if time's over
            
                if self.button0.value or self.button1.value or self.button2.value or self.button3.value:

                    if self.button0.value:
                        self.inputList.append(0)
                        while self.button0.value:
                            simpleio.tone(self.buzzerPin, self.tones[0], duration=0.1)
                            self.led0.value = True
                        self.led0.value = False

                    elif self.button1.value:
                        self.inputList.append(1)
                        while self.button1.value:
                            self.led1.value = True
                            simpleio.tone(self.buzzerPin, self.tones[2], duration=0.1)
                        self.led1.value = False

                    elif self.button2.value:
                        self.inputList.append(2)
                        while self.button2.value:
                            self.led2.value = True
                            simpleio.tone(self.buzzerPin, self.tones[4], duration=0.1)
                        self.led2.value = False

                    elif self.button3.value:
                        self.inputList.append(3)
                        while self.button3.value:
                            self.led3.value = True
                            simpleio.tone(self.buzzerPin, self.tones[6], duration=0.1)
                        self.led3.value = False
    
                    print(f"inputlist: {self.inputList}")
                    print(f"gamelist: {self.gameList}")
                    

                    if self.inputList[self.counter] != self.gameList[self.counter]:
                            #nop
                        print("worng button")
                        self.loseAnimation()
                        return
                    elif self.inputList[self.counter] == self.gameList[self.counter]:
                        self.counter +=1
                    
                    isButtonPressed = True
            
            
        self.winAnimation()
        
        
    def winAnimation(self) -> None:
        print("win")
        
        timer.restart()
        timer.pause()
        self.level += 1 #You won, so we will spice things a bit :)
        self.counter = 0 #resets counter

        #buzzes some cools sounds 

        for i in range(len(self.tones) - 1):
            simpleio.tone(self.buzzerPin, self.tones[i], duration=0.1)

        for i in range(2):
            self.led0.value = True
            self.led1.value = True
            self.led2.value = True
            self.led3.value = True
            time.sleep(0.3)
            self.led0.value = False
            self.led1.value = False
            self.led2.value = False
            self.led3.value = False

        self.led0.value = True
        self.led1.value = True
        self.led2.value = True
        self.led3.value = True
        time.sleep(4)
        self.led0.value = False
        self.led1.value = False
        self.led2.value = False
        self.led3.value = False
        
        
    
    def loseAnimation(self) -> None:
        print("loose")
        self.winFlag = False 
        timer.restart()
        timer.pause()

        self.level = 0
        # Cross pattern "X" with the LEDS
        
        for i in range(len(self.tones) -1, -1, -1):
            simpleio.tone(self.buzzerPin, self.tones[i], duration=0.1)

        
        for i in range(2):
            
            self.led0.value = True
            time.sleep(0.4)
            self.led0.value = False
            self.led2.value = True
            time.sleep(0.4)
            self.led2.value = False
            self.led3.value = True
            time.sleep(0.4)
            self.led3.value = False
            self.led1.value = True
            time.sleep(0.4)
            self.led1.value = False
        
        time.sleep(1)
        

    def sleepAnimation(self) -> None:
        #no sound, it's nahessing profoundly
        if not self.winFlag:
            self.winFlag = True


        
        self.led0.value = True
        time.sleep(0.09)
        self.led0.value = False
        self.led3.value = True
        time.sleep(0.09)
        self.led3.value = False
        self.led2.value = True
        time.sleep(0.09)
        self.led2.value = False
        self.led1.value = True
        time.sleep(0.09)
        self.led1.value = False 
        print("nahess")

        
        
        

simon = Simon()

if __name__ == "__main__":
    while True:
        while not simon.button0.value or simon.button1.value or simon.button2.value or simon.button3.value: # if nothing is touched, stays on this menu and doesn't plays
            simon.sleepAnimation()
        
        while simon.winFlag:
            simon.start()
            simon.showingColors()
            simon.inputColors() #manages the loosing and winning animations
