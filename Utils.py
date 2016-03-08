import logging.config

def initLogger(verbose):
    if verbose:
        logging.config.fileConfig('./Config/log.conf')
    else:
        logging.config.fileConfig('./Config/verbose.conf')
