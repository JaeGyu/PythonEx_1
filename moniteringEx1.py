import json
import time
import socket
import os
import re
import sys
#import commands  #파이선3에서 디프리되었다! subprocess로 대체
import subprocess
#import urllib2, base64


def main():
    ip = socket.gethostname()
    timestamp = int(time.time())
    print(timestamp)

if __name__ == "__main__":
    proc = subprocess.getoutput(' ps -ef|grep %s|grep -v grep|wc -l ' % os.path.basename(sys.argv[0]))
    
    if int(proc) < 5:
        main()

