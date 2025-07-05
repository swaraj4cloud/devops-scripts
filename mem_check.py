import os
with open ('/proc/meminfo', 'r') as f:
    lines = f.readlines()
mem_total = int([line for line in lines if 'MemTotal' in line] [0].split()[1])
mem_free = int([line for line in lines if 'MemAvailable' in line] [0].split()[1])
mem_used = mem_total-mem_free
usage_percent = (mem_used / mem_total)* 100
print(f"Memory Usage:{mem_used // 1024} MB /{mem_total // 1024} MB ({int(usage_percent)}%)")
if usage_percent > 80:
      print ('ALERT:Memory usage is above 80%')
