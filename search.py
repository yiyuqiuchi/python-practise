#!/usr/bin/env python
#coding:utf-8
#

import sys
import optparse
import MySQLdb

query = sys.argv[1]

opt = optparse.OptionParser()
opt.add_option("-q", "--query", action="store", type="string", dest="term")
opt.add_option("-t", "--table", action="store", type="string", dest="table")
opt.add_option("-c", "--column", action="store", type="string", dest="column")
opt.add_option("-f", "--format", action="store_true", dest="format")
opt, args = opt.parse_args()
term = opt.term
table = opt.table
format = opt.format
column = opt.column

mydb = MySQLdb.connect(host = 'localhost',
                       user = 'root',
                       passwd = '',
                       db = 'world')

cursor = mydb.cursor()

statement = """select * from %s where %s like '%s' """ %(table, column, term)

command = cursor.execute(statement)
results = cursor.fetchall()

record_list = []
for record in results:
    record_list.append(record[1])

for i in xrange(0, len(record_list)):
    print "%s. %s" %(i+1, record_list[i])


