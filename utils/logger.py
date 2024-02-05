import logging

def log_message(message: str, level: int):

    logging.basicConfig(filename='logs.log',
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        level=logging.INFO)
    
    if level == 1:
        logging.error(message)
    elif level == 0:
        logging.info(message)
