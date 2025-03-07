"""
Logging Module

This module sets up a robust logging system for the application. It uses Python's built-in logging module along with custom configurations to create a flexible and efficient logging solution.

Key Features:
- Configurable logging based on environment variables
- File rotation support
- Console output
- Custom formatter for better compatibility with some logging systems
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Set up logger file path
LOG_FILE = 'test.log'

logger_file = "logs/" + LOG_FILE
file_dir = Path(logger_file).parent

# Ensure the log directory exists
file_dir.mkdir(parents=True, exist_ok=True)

# Get max bytes for the log file rotation
max_bytes = int(3698000)

# Get log level
LOG_LEVEL = 'INFO'

if LOG_LEVEL == "DEBUG":
    LOG_LEVEL = logging.DEBUG
elif LOG_LEVEL == "INFO":
    LOG_LEVEL = logging.INFO
elif LOG_LEVEL == "WARNING":
    LOG_LEVEL = logging.WARNING
elif LOG_LEVEL == "ERROR":
    LOG_LEVEL = logging.ERROR
elif LOG_LEVEL == "CRITICAL":
    LOG_LEVEL = logging.CRITICAL
else:
    LOG_LEVEL = (
        logging.WARNING
    )  # Default log level to WARNING if nothing is directly specified

# Creating an object and set overall level from the root
log = logging.getLogger()
log.setLevel(LOG_LEVEL)


# Check if the logger has handlers to avoid adding duplicates
if not log.handlers:

    # Set Formatting
    fileFormatter = logging.Formatter(
        "[%(asctime)s.%(msecs)03d] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        "%Y-%m-%dT%H:%M:%S",
    )

    # Create handler for log file
    file_handler = RotatingFileHandler(logger_file, maxBytes=max_bytes, backupCount=10)
    file_handler.setFormatter(fileFormatter)

    # Create handler for console output
    stream_handler = logging.StreamHandler()
    # stream_handler.setFormatter(streamFormatter)

    # Add handlers to log object
    log.addHandler(file_handler)
    log.addHandler(stream_handler)


def message(msg):
    """
    Return a formatted message for logging.

    Args:
        msg (str): The message to be logged.

    Returns:
        str: Formatted message with separators.
    """
    return f"\n----------- {msg} -----------"
