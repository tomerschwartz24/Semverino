import logging


def setup_logger(name, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    c_handler = logging.StreamHandler()
    c_handler.setLevel(level)

    c_format = logging.Formatter(
        "{asctime}| {levelname} | {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M"
    )
    c_handler.setFormatter(c_format)

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(c_handler)

    logger.propagate = False

    return logger
