#!/usr/bin/env python3
import csv
import sys
import os
import argparse

unstable_fields = [ 'ssdeep', 'banner_http', 'banner_smtp' ]

argparser = argparse.ArgumentParser(description='CSV to HTML table formatting tool for dnstwist output.')

argparser.add_argument('-f', '--filter_unstable',
    help="Filters out unstable fields",
    action="store_true", dest="filter_unstable", default=False,
)
argparser.add_argument('-s', '--screenshot_dir',
    help="Directory with screenshots (optional)",
    action="store", dest="screenshot_dir",
)
argparser.add_argument('csvfile',
    help="CSV file to read",
    action="store",
)

args = argparser.parse_args()

check_screenshots = False
if args.screenshot_dir:
  if os.path.isdir(args.screenshot_dir):
    check_screenshots = True
  else:
    print("error: screenshot directory {} not accessible, ignoring that!".format(args.screenshot_dir), file=sys.stderr)

with open(args.csvfile, 'rt') as csvfile:
  reader = csv.reader(csvfile, quotechar='"')
  total_rows = sum(1 for row in reader)
  csvfile.seek(0)
  reader = csv.reader(csvfile, quotechar='"')
  for rowc, row in enumerate(reader):
    if check_screenshots:
      if (rowc == 0):
        row.append("screenshot")
      else:
        domain = row[coldesc.index('domain')]
        screenshots = list(filter(lambda x:x.endswith("_{}.png".format(domain)), os.listdir(args.screenshot_dir)))
        if len(screenshots)>0:
          shotlinks = []
          for shot in screenshots:
            shotlinks.append('<a href="' + args.screenshot_dir + '/' + shot + '">' + "Screenshot" + '</a>')
          row.append(' '.join(shotlinks))
        else:
          row.append("")
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
