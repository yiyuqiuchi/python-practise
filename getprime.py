#!/usr/bin/env python

prime = []
print "Please wait a moment, do some others"
for i in range(2, 1000000):
  for j in range(2, i):
    if i % j == 0:
      break
  else:
    prime.append(i)

print "The list is the whole primes between 1 and 100000 :"
print prime
