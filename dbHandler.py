import json
import os
from logging import *



def Init(force = False, dbPath = "~/.db"):
    dbPath = os.path.expanduser(dbPath)
    debug("Init a DB")
    if os.path.isfile(dbPath):
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


def Load(dbPath = "~/.db"):
    dbPath = os.path.expanduser(dbPath)
    debug("Load DB")
    if os.path.isfile(dbPath):
        with open(dbPath) as file:
            return json.load(file)
    else:
        error("No DB exist in folder")
        return None

def Store(db, dbPath = "~/.db"):
    dbPath = os.path.expanduser(dbPath)
    debug("Storing DB to file")
    with open(dbPath, 'w') as outputFile:
        json.dump(db, outputFile)
        info("DB stored to file")
