import sys
from datetime import datetime

logFile = "manager.log"

class sysLog:
    log = True

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

infoMsg     = "[" + bcolors.OKGREEN    + "INFO"    + bcolors.ENDC + "]"
errorMsg    = "[" + bcolors.FAIL       + "ERROR"    + bcolors.ENDC + "]"
warnMsg     = "[" + bcolors.WARNING    + "WARNING"    + bcolors.ENDC + "]"
debugMsg    = "[" + bcolors.OKBLUE     + "DEBUG"   + bcolors.ENDC + "]"

class Logger:
    def info(self, msg):
        sys.stdout.write('\033[2K\033[1G')
        print (f'{infoMsg} {msg}')
        sys.stdout.flush()
        if sysLog.log:
            self.logMsg(f'[INFO] {msg}')

    def error(self, msg):
        sys.stdout.write('\033[2K\033[1G')
        print (f'{errorMsg} {msg}')
        sys.stdout.flush()
        if sysLog.log:
            self.logMsg(f'[ERROR] {msg}')

    def warn(self, msg):
        sys.stdout.write('\033[2K\033[1G')
        print (f'{warnMsg} {msg}')
        sys.stdout.flush()
        if sysLog.log:
            self.logMsg(f'[WARNING] {msg}')

    def debug(self, msg):
        sys.stdout.write('\033[2K\033[1G')
        print (f'{debugMsg} {msg}')
        sys.stdout.flush()

    def logMsg(self, msg):
        now = datetime.now()
        with open(logFile, 'a') as file:
            file.write(f'{now.strftime("%d/%m/%Y %H:%M:%S")} | {msg}\n')
            file.close

logger = Logger()