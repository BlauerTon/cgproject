import logging

# Configure logging to log all computations into a file
logging.basicConfig(filename='computations.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function to log computations
def log_computation(message):
    logging.info(message)

# Example constraint function (you can add more as per your requirements)
def ensure_unique_emails(email_list):
    if len(set(email_list)) != len(email_list):
        raise ValueError("Generated emails are not unique!")