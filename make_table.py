#!/usr/bin/env python3
import csv
import sys
import argparse

unstable_fields = [ 'ssdeep', 'banner_http', 'banner_smtp' ]

argparser = argparse.ArgumentParser(description='CSV to HTML table formatting tool for dnstwist output.')

argparser.add_argument('-f', '--filter_unstable',
    help="Filters out unstable fields",
    action="store_true", dest="filter_unstable", default=False,
)
argparser.add_argument('csvfile',
    help="CSV file to read",
    action="store",
)

args = argparser.parse_args()

with open(args.csvfile, 'rt') as csvfile:
  reader = csv.reader(csvfile, quotechar='"')
  total_rows = sum(1 for row in reader)
  csvfile.seek(0)
  reader = csv.reader(csvfile, quotechar='"')
  for rowc, row in enumerate(reader):
    if (rowc == 0):
      print("<thead>")
      coldesc = row
    elif (rowc == 1):
      print("<tbody>")
    print("<tr>", end="")
    td_type = 'td' if (rowc > 0) else 'th'
    for colidx, col in enumerate(row):
      if args.filter_unstable and (coldesc[colidx] in unstable_fields):
        continue
      print("<{}>{}</{}>".format(td_type, col, td_type), end="")
    print("</tr>")
    if (rowc == 0):
      print("</thead>")
    elif (rowc == total_rows-1):
      print("</tbody>")
