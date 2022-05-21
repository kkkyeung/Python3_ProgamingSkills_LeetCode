import math, time
from datetime import datetime


# function to check perferct square
def checkPerfectSquare(n):
    sqrt = int(math.sqrt(n))
    if pow(sqrt, 2) == n:
        return True
    else:
        return False
 
# function to check Fibonacci number
def isFibonacciNumber(n):
    res1 = 5 * n * n + 4
    res2 = 5 * n * n - 4
    if checkPerfectSquare(res1) or checkPerfectSquare(res2):
        return True
    else:
        return False

def checkinput(n):
    if n != 'quit':
        n = int(n)
        if isFibonacciNumber(n) and n < 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228876:
            print ("FIB")
        if n not in inputDictionary:
            inputDictionary[n] = 1
        else:
            inputDictionary[n] += 1
            print(inputDictionary)
    else:
        print("Thanks for playing, press any key to exit.")



class MyTimer():
    """
    timer.start() - should start the timer
    timer.pause() - should pause the timer
    timer.resume() - should resume the timer
    """

    def __init__(self):
        self.timestarted = None
        self.timepaused = None
        self.paused = False

    def start(self):
        """ Starts an internal timer by recording the current time """
        self.timestarted = datetime.now()

    def pause(self):
        """ Pauses the timer """
        if self.timestarted is None:
            raise ValueError("Timer not started")
        if self.paused:
            raise ValueError("Timer is already paused")
        print('timer halted')
        self.timepaused = datetime.now()
        self.paused = True

    def resume(self):
        """ Resumes the timer by adding the pause time to the start time """
        if self.timestarted is None:
            raise ValueError("Timer not started")
        if not self.paused:
            raise ValueError("Timer is not paused")
        print('timer resumed')
        pausetime = datetime.now() - self.timepaused
        self.timestarted = self.timestarted + pausetime
        self.paused = False

    def get(self):
        """ Returns a timedelta object showing the amount of time
            elapsed since the start time, less any pauses """
        if self.timestarted is None:
            raise ValueError("Timer not started")
        if self.paused:
            return self.timepaused - self.timestarted
        else:
            return datetime.now() - self.timestarted




if __name__ == "__main__":
    # frequency Dictionary
    inputDictionary = {}
    # timer
    t = MyTimer()
    frequencyTime = int(input("Please input the amount of time in seconds between emitting numbers and their frequency: \n"))
    if frequencyTime > 0:
        t.start()
    # first input
    FirstNum = input("Please enter the first number: \n")
    checkinput(FirstNum)
    if FirstNum == 'halt':
        t.pause()
    elif FirstNum == 'resume':
        t.resume()
    # loop the next input
    while inputDictionary:
        NextNum = input("Please enter the next number: \n")
        checkinput(NextNum)
        if NextNum == 'halt':
            t.pause()
        elif NextNum == 'resume':
            t.resume()
        elif NextNum == 'quit':
            break