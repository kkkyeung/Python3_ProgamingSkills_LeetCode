import math,time,threading,os,signal

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
    else:
        print("Thanks for playing, press any key to exit.")


def thread_job():
    # timer
    start_time = time.time()
    frequencyTime = input("Please input the amount of time in seconds between emitting numbers and their frequency: \n")
    if frequencyTime == 'quit':
        print("Thanks for playing, press any key to exit.")
    else:
        frequencyTime = int(frequencyTime)
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            global stop_threads 
            if elapsed_time >= frequencyTime:
                print(inputDictionary)
                start_time = time.time()
                if stop_threads:
                    break

        
            


def T2_job():
   # first input
    FirstNum = input("Please enter the first number: \n")
    checkinput(FirstNum)
    # loop the next input
    while inputDictionary:
        NextNum = input("Please enter the next number: \n")
        checkinput(NextNum)
        global stop_threads
        if NextNum == 'quit':
            stop_threads = True
            break

def main():
    added_thread = threading.Thread(target=thread_job, name='T1')
    thread2 = threading.Thread(target=T2_job, name='T2')
    added_thread.start()
    thread2.start()
    thread2.join()
    # added_thread.join()



if __name__ == '__main__':
    # frequency Dictionary
    stop_threads = False
    inputDictionary = {}
    main()
