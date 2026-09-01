import logging
from pathlib import Path
from src.config import LOG_DIR, LOG_FILE

def setup_logger():

    LOG_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format=(
            "%(asctime)s - "
            "%(levelname)s - "
            "%(message)s"
        )
    )

    return logging.getLogger(__name__)