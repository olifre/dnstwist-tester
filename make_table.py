#!/usr/bin/env python3
import csv
import sys

if len(sys.argv) != 2:
  print("Need exactly 1 commandline argument, got {} instead".format(len(sys.argv)-1))
  sys.exit(1)

with open(sys.argv[1], 'rt') as csvfile:
  reader = csv.reader(csvfile, quotechar='"')
  rowc = 0
  for row in reader:
    print("<tr>", end="")
    if (rowc == 0):
      for col in row:
        print("<th>{}</th>".format(col), end="")
    else:
      for col in row:
        print("<td>{}</td>".format(col), end="")
    print("</tr>")
    rowc += 1
