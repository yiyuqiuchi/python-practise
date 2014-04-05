#!/usr/bin/env python

import os

a = 10

print "Please input your number: "
b = int(raw_input())
if a == b:
  print "You win!"
  exit()
elif a > b:
  print "Your number is small."
  exit()
else:
  print "Your number is big."
  exit()
