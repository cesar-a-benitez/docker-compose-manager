import sys
import time
import threading

from manager_lib.logger import logger

second = 1 / 0.6
timer = [0, 0, 0]
count = 0

class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def counter():
        global second
        global timer
        global count
        
        if count >= second:
            if timer[0] < 59:
                timer[0] += 1
            else:
                timer[0]  = 0
                if timer[1] < 59:
                    timer[1] += 1
                else:
                    timer[1] = 0
                    timer[2] += 1
            count = 0
        else:
            count += 1
            
    @staticmethod
    def spinning_cursor():
        global second
        global timer
        global count

        while 1: 

            if count >= second:
                if timer[0] < 59:
                    timer[0] += 1
                else:
                    timer[0]  = 0
                    if timer[1] < 59:
                        timer[1] += 1
                    else:
                        timer[1] = 0
                        timer[2] += 1
                count = 0
            else:
                count += 1

            timestamp = ' '
            if timer[2] == 1:
                timestamp += " " + str(timer[[2]]) + " hour"
            elif timer[2] > 1:
                timestamp += " " + str(timer[[2]]) + " hours"

            if timer[1] == 1:
                timestamp += " " + str(timer[1]) + " minute"
            elif timer[1] > 0:
                timestamp += " " + str(timer[1]) + " minutes"

            timestamp += " " + str(timer[0]) + " seconds"

            timestamp += " elapsed "

            for cursor in '|/-\\': yield cursor + timestamp

    def __init__(self, enabled=True, delay=None):
        global timer
        self.spinner_generator = self.spinning_cursor()
        self.enabled = enabled
        if delay and float(delay): self.delay = delay
        timer = [0, 0, 0]

    def spinner_task(self):
        global timestampLen
        while self.busy:
            if self.enabled:
                sys.stdout.write(next(self.spinner_generator))
                sys.stdout.flush()
                time.sleep(self.delay)
                sys.stdout.write('\033[2K\033[1G')
                sys.stdout.flush()
            else:
                self.counter()
                time.sleep(self.delay)

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)

        if timer[1] == 0:
            timestamp = "Task finished in " + str(timer[0]) + " seconds"
        elif timer[1] == 1:
            timestamp = "Task finished in " + str(timer[1]) + " minute and " + str(timer[0]) + " seconds"
        else:
            timestamp = "Task finished in " + str(timer[1]) + " minutes and " + str(timer[0]) + " seconds"
        
        logger.info(timestamp)

        if exception is not None:
            return False
