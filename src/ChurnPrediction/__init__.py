import os
import sys
import logging

#defines the format of the log messages, specifying the timestamp, log level, module, and the log message itself.
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
#specifies the directory where logs will be stored.
log_dir = "logs"
#creates the full path for the log file inside the log_dir
log_filepath = os.path.join(log_dir,"running_logs.log")
#ensures that the log_dir exists or creates it if it doesn't.
os.makedirs(log_dir, exist_ok=True)

# sets up the basic configuration for the logging system.
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

#creates a logger object named "ChurnPredictionLogger". This allows different parts of the code to use the same logger.
logger = logging.getLogger("ChurnPrediction")

#This setup will log messages of level INFO and above both to the specified log file (running_logs.log inside the logs directory) 
# and to the console. The messages will follow the defined format. The logger ChurnPredictionLogger can be used throughout 
# the codebase to log relevant information or errors.