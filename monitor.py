import psutil
import time

print("===== Linux Server Monitor =====")

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    print("\nCPU Usage     :", cpu, "%")
    print("Memory Usage  :", memory.percent, "%")
    print("Disk Usage    :", disk.percent, "%")

    time.sleep(2)