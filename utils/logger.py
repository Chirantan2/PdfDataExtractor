import logging

def log_message(message: str, level: int):
    """Log message

    Args:
        message (str): message to be logged
        level (int): 0 if INFO, 1 if ERROR
    """

    logging.basicConfig(filename='logs.log',
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        level=logging.INFO)
    
    if level == 1:
        logging.error(message)
    elif level == 0:
        logging.info(message)
