import subprocess
import json
from datetime import datetime


# Collect metadata
report_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

metrics_result = subprocess.run(
    ["python3", "agents/metric_collector.py"],
    capture_output=True, text=True
)

logs_result = subprocess.run(
    ["python3", "agents/log_collector.py"],
    capture_output=True, text=True
)

metrics_data = json.loads(metrics_result.stdout)
logs_data = json.loads(logs_result.stdout)

if metrics_data["status"] == "warning" or logs_data["status"] == "warning":
    overall_status = "warning"
else:
    overall_status = "healthy"

report = {
    "report_timestamp": report_timestamp,
    "metrics": metrics_data,
    "logs": logs_data,
    "overall_status": overall_status
}

print(json.dumps(report, indent=2))
