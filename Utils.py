import logging.config

def initLogger(verbose):
    if verbose:
        logging.config.fileConfig('./verbose.conf')
    else:
        logging.config.fileConfig('./log.conf')
