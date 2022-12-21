#!/usr/bin/python3
import os
import sys
import time
import random

delay = int(sys.argv[1])
print(f'Сhild[{os.getpid()}]: I am started. My PID {os.getpid()}. Parent PID {os.getppid()}.')
time.sleep(delay)
print(f'Child[{os.getpid()}]: I am ended. PID {os.getpid()}. Parent PID {os.getppid()}.')
os._exit(random.randint(0, 1))