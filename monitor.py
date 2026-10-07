import psutil
import time

print("===== Linux Server Monitor =====")

while True:
    # CPU
    cpu = psutil.cpu_percent(interval=1)

    # Memory
    memory = psutil.virtual_memory()

    # Disk
    disk = psutil.disk_usage("/")

    # Network
    network = psutil.net_io_counters()

    # System uptime
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_hours = uptime_seconds / 3600

    print("\n------------------------------")
    print("CPU Usage     :", cpu, "%")
    print("Memory Usage  :", memory.percent, "%")
    print("Disk Usage    :", disk.percent, "%")
    print("Data Sent     :", network.bytes_sent / (1024 ** 2), "MB")
    print("Data Received :", network.bytes_recv / (1024 ** 2), "MB")
    print("System Uptime :", round(uptime_hours, 2), "hours")
    print("------------------------------")

    time.sleep(2)