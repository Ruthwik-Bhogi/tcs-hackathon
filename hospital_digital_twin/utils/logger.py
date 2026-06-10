# utils/logger.py

import logging
import os

from utils.constants import (
    LOG_LEVEL,
    LOG_FILE
)

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

LOG_PATH = os.path.join(
    "logs",
    LOG_FILE
)


def get_logger(name: str):

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(
        getattr(
            logging,
            LOG_LEVEL.upper(),
            logging.INFO
        )
    )

    formatter = logging.Formatter(
        fmt=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File Handler
    file_handler = logging.FileHandler(LOG_PATH)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


# Default application logger
logger = get_logger("HospitalDigitalTwin")


if __name__ == "__main__":

    logger.info(
        "Hospital Digital Twin logger initialized."
    )

    logger.warning(
        "This is a sample warning."
    )

    logger.error(
        "This is a sample error."
    )
