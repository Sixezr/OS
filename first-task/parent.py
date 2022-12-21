#!/usr/bin/python3
import os
import sys
import random

def forkChild():
    child = os.fork()
    if child > 0:
        print(f'Parent[{os.getpid()}]: I ran children process with PID {child}.')
    else:
        count = random.randint(5, 10)
        os.execl('./child.py', './child.py', str(count))

    return child

count = int(sys.argv[1])
mutableCount = count

while mutableCount > 0:
    child = forkChild()
    if child > 0:
        mutableCount = mutableCount - 1

mutableCount = count

while mutableCount > 0:
    child_pid, status = os.wait()
    if status != 0:
        child = forkChild()
    else:
        print(f'Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit Status {status}.')
        mutableCount = mutableCount - 1

os._exit(os.EX_OK)