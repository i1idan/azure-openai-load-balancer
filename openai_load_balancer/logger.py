import logging

# Create a logger
logger = logging.getLogger("load_balancer")

# Set the logging level (optional)
logger.setLevel(logging.DEBUG)
logger.propagate = False
# Create a file handler for logging to a file
file_handler = logging.FileHandler("log_file.log")

# Create a stream handler for logging to the console
stream_handler = logging.StreamHandler()

# Create a formatter for formatting the log messages
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Set the formatter for the handlers
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)