import boto3
import subprocess
import json
import uuid

# Step 1 — run anomaly_detector.py and parse output
result = subprocess.run(
    ["python3", "pipeline/anomaly_detector.py"],
    capture_output=True, text=True
)
report = json.loads(result.stdout)

# Step 2 — generate unique ID
unique_id = str(uuid.uuid4())

# Step 3 — write to DynamoDB
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("sre-platform-anomalies")

table.put_item(
    Item={
        "id": unique_id,
        "timestamp": report["timestamp"],
        "status": report["status"],
        "anomaly_count": report["anomaly_count"],
        "anomalies": json.dumps(report["anomalies"])
    }
)

# Step 4 — confirm
print(f"Anomaly record logged to DynamoDB: {unique_id}")