#/usr/bin/env python
# -*- coding: utf-8 -*-
#打印杨辉三角形
#提示用户输入高度，然后打印杨辉三角形
#例如高度为6的杨辉三角形
#
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
#1 5 10 10 5 1
print "Please enter height of yanghui's triangle:"
h=int(raw_input())

print "Printing the yanghui's triangle: "
a=[' ']
b=[]
for i in range(h):
  b.append([])
  for j in range(h):
    b[i].append(0)

for i in range(h):
  b[i][0]=1
  b[i][i]=1

for i in range(2,h):
  for j in range(1,i):
    b[i][j] = b[i-1][j-1] + b[i-1][j]

#print b
for i in range(h):
  print a[0]*(h-i),
  for j in range(i + 1):
    print b[i][j],
  print
