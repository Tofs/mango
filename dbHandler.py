import json
import os
from logging import *



def Init(force = False):
    debug("Init a DB")
    if os.path.isfile(".db"):
        if force:
            warning("Overwriting DB")
            createDB = True
        else:
            info("DB exist")
            createDB = False
    else:
        createDB = True

    if createDB:
        container = {
        "version" : 1,
        "itemCounter" : 0,
        "dataBase" : {}
        }
        info("New DB is created")
        Store(container)
        return Load()


def Load():
    debug("Load DB")
    if os.path.isfile(".db"):
        with open(".db") as file:
            return json.load(file)
    else:
        error("No DB exist in folder")
        return None

def Store(db):
    debug("Storing DB to file")
    with open(".db" , 'w') as outputFile:
        json.dump(db, outputFile)
        info("DB stored to file")
