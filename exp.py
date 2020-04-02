from random import random
import threading
import time

result = None

def background_calculation():
    # here goes some long calculation
    time.sleep(60)

    # when the calculation is done, the result is stored in a global variable
    global result
    result = 40

def main():
    thread = threading.Thread(target=background_calculation)
    thread.start()

    # TODO: wait here for the result to be available before continuing!

    print('The result is', result)
    
if __name__ == '__main__':
    main()