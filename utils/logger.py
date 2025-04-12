import logging

def setup_logger(name: str, level=logging.INFO) -> logging.Logger:
    """
    Sets up and returns a logger with the given name and level.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Avoid adding duplicate handlers
    if not logger.handlers:
        # Create console handler with the same logging level
        ch = logging.StreamHandler()
        ch.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    
    return logger

# Example usage:
if __name__ == "__main__":
    log = setup_logger("TestLogger")
    log.info("Logger is set up correctly.")