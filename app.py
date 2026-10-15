print("Welcome to DevOps Training")
print("Learning Git, Terraform, Docker and Kubernetes")
print("Git tracks changes in DevOps projects")

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("DevOps application started")
logging.warning("This is a test warning")
logging.info("DevOps application completed")
