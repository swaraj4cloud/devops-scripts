with open ('sample.log', 'r')as f:
  lines = f.readlines()
print ("ERROR lines found :\n")
for idx, line in enumerate(lines, start=1):
  if 'ERROR'in line:
    print(f"Line{idx}: {line.strip()}")
