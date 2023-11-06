import logging

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def setup_logger(name, log_file, level=logging.INFO):
    """To create as many loggers as you want"""

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# info logger
# info_file_logger = setup_logger('info logger', 'info.log')
# info_logger.info('This is just info message')

# error logger
# error_file_logger = setup_logger('error logger', 'error.log')
# error_logger.error('This is an error message')
