import sys

if len (sys.argv) < 2:
    print("usage: python3 log_parser.py <logfile>")
    sys.exit(1)
logfile= sys.argv[1]

with open (logfile, 'r')as f:
  lines = f.readlines()

print ("ERROR lines found :\n")
for idx, line in enumerate(lines, start=1):
  if 'ERROR'in line:
    print(f"Line{idx}: {line.strip()}")
