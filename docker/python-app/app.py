import os
from datetime import datetime, timezone

print("================================")
print("Docker Python Application")
print("================================")
print("Application started successfully!")
print("Environment:", os.getenv("APP_ENV", "development"))
print("Current time:", datetime.now(timezone.utc))
print("Running inside Docker container")
