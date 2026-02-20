import logging

class Monitor:
    def __init__(self):
        logging.basicConfig(filename='cash_flow_optimizer.log', level=logging.INFO)
        
    def log_success(self, message):
        logging.info(f"SUCCESS: {message}")
        
    def log_error(self, message):
        logging.error(f"ERROR: {message}")