with open ('sample.log', 'r')as f:
  lines = f.readlines()
print ("ERROR lines found :\n")
for line in lines :
  if 'ERROR'in line:
    print(line.strip())
