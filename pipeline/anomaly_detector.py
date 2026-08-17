
import json
import subprocess
from datetime import datetime

# Step 1 — get data from processor
result = subprocess.run(
    ["python3", "pipeline/processor.py"],
    capture_output=True, text=True
)
report = json.loads(result.stdout)
metrics = report["metrics"]

# Step 2 — define baselines
BASELINES = {
    "cpu_percent": 30.0,
    "memory_percent": 50.0,
    "disk_percent": 60.0
}

# Step 3 — detect anomalies
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
anomalies = []

for metric, baseline in BASELINES.items():
    current = metrics[metric]
    deviation = current - baseline
    if deviation > 20.0:
        anomalies.append({
            "metric": metric,
            "current": current,
            "baseline": baseline,
            "deviation": round(deviation, 2),
            "severity": "warning"
        })

# Step 4 — determine status and output
if len(anomalies) > 0:
    status = "anomaly_detected"
else:
    status = "normal"

output = {
    "timestamp": timestamp,
    "anomalies": anomalies,
    "anomaly_count": len(anomalies),
    "status": status
}

print(json.dumps(output, indent=2))
