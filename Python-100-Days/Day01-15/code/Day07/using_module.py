#! /usr/bin/python

#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

# Filename: using_module.py
# Description: using module and __name__

if __name__ == '__main__':
    print 'This is main'
else:
    print 'This is sub module'

## If using it directly by 'python using_module.py' or 
## './using_module.py', then it is excuted by main
## otherwise if it is used by import using_module, then
## it is excute by sub module.
