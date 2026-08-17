import boto3
import json
import subprocess
from datetime import datetime

BUCKET = "sre-platform-reports-oluwaseyi-2026"

# Step 1 — get report from processor
result = subprocess.run(
    ["python3", "pipeline/processor.py"],
    capture_output=True, text=True
)
report = json.loads(result.stdout)

# Step 2 — generate timestamped filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
key = f"reports/{timestamp}.json"

# Step 3 — upload to S3
s3 = boto3.client("s3")
s3.put_object(
    Bucket=BUCKET,
    Key=key,
    Body=json.dumps(report, indent=2),
    ContentType="application/json"
)

# Step 4 — confirm
print(f"Report saved to S3: {key}")