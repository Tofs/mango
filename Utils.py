import logging.config

def initLogger(verbose):
    return
    if verbose:
        logging.basicConfig(filename='./Config/log.conf')
    else:
        logging.basicConfig(filename='./Config/verbose.conf')
