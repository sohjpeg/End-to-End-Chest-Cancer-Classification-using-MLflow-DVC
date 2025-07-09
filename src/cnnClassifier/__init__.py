import os
import sys
import logging

logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

long_dir = "logs"
log_filepath = os.path.join(long_dir , "running_logs.log")
os.makedirs(long_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")