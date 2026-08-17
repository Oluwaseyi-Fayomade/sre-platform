import json
import socket
from datetime import datetime

LOG_FILE = "/Users/mac/sre-toolkit/linux/sample.log"

# Collect metadata
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
hostname = socket.gethostname()

# Parse the log file
total_lines = 0
error_count = 0
warning_count = 0
info_count = 0
last_errors = []

with open(LOG_FILE, "r") as f:
    for line in f:
        line = line.strip()
        total_lines += 1
        if "ERROR" in line:
            error_count += 1
            last_errors.append(line)
        elif "WARNING" in line:
            warning_count += 1
        elif "INFO" in line:
            info_count += 1

# Determine status
if error_count > 0:
    status = "warning"
else:
    status = "healthy"

# Build data structure
log_data = {
    "timestamp": timestamp,
    "hostname": hostname,
    "log_file": LOG_FILE,
    "total_lines": total_lines,
    "error_count": error_count,
    "warning_count": warning_count,
    "info_count": info_count,
    "last_errors": last_errors[-3:],
    "status": status
}

# Output as JSON
print(json.dumps(log_data, indent=2))
