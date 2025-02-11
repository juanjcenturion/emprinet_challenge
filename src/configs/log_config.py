import logging
import os

LOG_DIR = "src/logs"

# Create directory for logs
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(os.path.join(LOG_DIR, "app.log")),  # Save logs
            logging.StreamHandler(),  # Show in console logs
        ],
    )

    return logging.getLogger(__name__)


logger = setup_logger()
