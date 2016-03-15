import dbHandler as fileDB
import Utils
import sys
from logging import *
import dbManager as db


# TODO: remove
# TODO: add tags
# TODO: remove tags
# TODO: filter on tags
# TODO: Search
# TODO: sort
# TODO: Alarm
# TODO: Duetime
# TODO: Creation time
# TODO: Relative priortity
# TODO: Priority as a function of time from creation
# TODO: Link do document
# TODO: Long/ short description
# TODO: Handle verbose paramater


def addTag(args):
    if len(args) == 2:
        db.addTag(args[0], args[1])

def listAll(args):
    if len(args) == 0:
        db.setDB(fileDB.Load())
        for item in db.getItems():
            print(item)
    else:
        warning("User input things... not allowed here")

def add(args):
    if len(args) == 1:
        db.addItem(args[0])
    else:
        error("only one arg")

def setStatus(args):
    if len(args) == 2:
        db.setStatus(args[0], args[1])

def init(args):
    if len(args) == 0:
        fileDB.Init()
    elif len(args) == 1:
        fileDB.Init(int(args[0]))
    else:
        error("no arg")

def remove(args):
    if len(args) == 1:
        db.removeItem(args[0])

actions = {
    "init" : init,
    "list" : listAll,
    "add" : add,
    "remove" : remove,
    "tag" : addTag,
	"status" : setStatus
}

if __name__ == "__main__":
    args = sys.argv

    if len(args) == 1:
        for action in actions:
            print(action)
        exit()



    args.pop(0)
    action = args.pop(0).lower()
    if action == "-v":
        Utils.initLogger(True)
        action = args.pop(0).lower()
    else:
        Utils.initLogger(False)


    info("Action: {0}".format(action))
    for arg in args:
        debug("Argument: {0}".format(arg))


    if action == "init":
        actions[action](args)
    else:
        db.setDB(fileDB.Load())
        actions[action](args)
        fileDB.Store(db.getDB())
