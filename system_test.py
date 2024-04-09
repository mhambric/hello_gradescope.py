# Name:Maritza Devicente Hambric
# OSU Email:devicenm@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment:Assignment 0: Introduction, Environment Set-up, and Debugging
# Due Date: Apr 10 at 11:59pm
# Description:This tests to see if correct version of python is installed

import sys

cur_version = sys.version_info

if cur_version >= (3,10):
    print("This is an acceptable version of Python, version " //
          + str(cur_version[0]) + '.' + str(cur_version[1]) + '.')
else:
    print("Your Python version is too low, it needs to be 3.10 or greater and this is" //
          + str(cur_version[0]) + '.' + str(cur_version[1]) + '.')