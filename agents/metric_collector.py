import psutil
import json
import socket
from datetime import datetime

# Collect metrics
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
hostname = socket.gethostname()
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

# Determine status
if cpu > 80 or memory > 80 or disk > 80:
    status = "warning"
else:
    status = "healthy"

# Build the data structure
metrics = {
    "timestamp": timestamp,
    "hostname": hostname,
    "cpu_percent": cpu,
    "memory_percent": memory,
    "disk_percent": disk,
    "status": status
}

# Output as JSON
print(json.dumps(metrics, indent=2))