logfile = "syslog.log"
with open(logfile, 'r') as f:
    lines = f.readlines()
print("Filtered error entries:\n")
for idx, line in enumerate(lines,start=1):
    if 'ERROR' in line:
        print(f"Line {idx}:{line.strip()}")
