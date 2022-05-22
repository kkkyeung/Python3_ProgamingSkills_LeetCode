import math,time,threading,operator

# function to check perferct square
def checkPerfectSquare(n):
    sqrt = int(math.sqrt(n))
    if pow(sqrt, 2) == n:
        return True
    else:
        return False
 
# function to check Fibonacci number Step1
def isFibonacciNumber(n):
    res1 = 5 * n * n + 4
    res2 = 5 * n * n - 4
    if checkPerfectSquare(res1) or checkPerfectSquare(res2):
        return True
    else:
        return False

# function to check Fibonacci number Step2
def checkinput(n):
    global stop_threads
    if n != 'quit':
        n = int(n)
        if isFibonacciNumber(n) and n < 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228876:
            print ("FIB")
        if n not in inputDictionary:
            inputDictionary[n] = 1
        else:
            inputDictionary[n] += 1
    else:
        stop_threads = True
        print(dict(sorted(inputDictionary.items(), key=operator.itemgetter(1),reverse=True)))
        print("Thanks for playing, press any key to exit.")
        return stop_threads


# def stopinput(whatinput):
#     if whatinput == 'halt':
#         current_time = time.time()
#         elapsed_time = current_time - start_time
#         pausetime = input("time halt")
#         if pausetime == 'resume':
#             checkinput(pausetime)
#             if stop_threads == True:
#                 return stop_threads
#             else:
#                 if (time.time() - elapsed_time) >= (frequencyTime - elapsed_time):
#                     if stop_threads == True:
#                         return stop_threads
#                     else:
#                         print(dict(sorted(inputDictionary.items(), key=operator.itemgetter(1),reverse=True)))
#                         return stop_threads



def thread_job():
    global stop_threads
    # timer
    start_time = time.time()
    frequencyTime = input("Please input the amount of time in seconds between emitting numbers and their frequency: \n")
    if frequencyTime == 'quit':
        stop_threads = True
        print(dict(sorted(inputDictionary.items(), key=operator.itemgetter(1),reverse=True)))
        print("Thanks for playing, press any key to exit.")
        
    else:
        frequencyTime = int(frequencyTime)
        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time >= frequencyTime:
                if stop_threads == True:
                    return stop_threads
                else:
                    print(dict(sorted(inputDictionary.items(), key=operator.itemgetter(1),reverse=True)))
                    start_time = time.time()
 

def T2_job():
    start_time = time.time()

    global stop_threads
    # first input
    FirstNum = input("Please enter the first number: \n")
    checkinput(FirstNum)
    if stop_threads == True:
        
        return stop_threads

    # loop the next input
    while True:
        NextNum = input("Please enter the next number: \n")
        checkinput(NextNum)
        if stop_threads == True:
            return stop_threads



if __name__ == '__main__':
    # frequency Dictionary
    inputDictionary = {}
    stop_threads = False
    added_thread = threading.Thread(target=thread_job, name='T1')
    thread2 = threading.Thread(target=T2_job, name='T2')
    added_thread.start()
    if stop_threads == True:
            added_thread.join()
    else:
        thread2.start()
        if stop_threads == True:
            thread2.join()
            added_thread.join()