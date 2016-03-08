from logging import *

def setDB(dataBase):
    global container
    global db
    if dataBase == None:
        error("trying to load a none as DB you sure?")
        return
    container = dataBase
    db = dataBase["dataBase"]
    debug("db loaded with data: {0}".format(db))

def getDB():
    global container
    return container


def addItem(Item):
    global container
    global db
    ic  = container["itemCounter"]
    content = { "description" : Item, "tags" : []}
    info("Adding item to db Id: {0} With Content:{1}".format(ic, content))
    db[str(ic)] = content
    db[str(ic)]["status"] = "New"
    container["itemCounter"] = container["itemCounter"] + 1

def setStatus(Item, Status):
    global db
    debug("set status of {0} to {1}".format(Item, Status))
    if not Item in db:
        error("item ({0}) not in db ".format(Item))
    else:
        db[Item]["status"] = Status

def removeItem(Item):
    global db
    if not Item in db:
        error("Trying to remove non existing item ({0}) from db".format(Item))
    info("removing item: {0}".format(Item))
    del db[Item]

def getItems(filter = None):
    global db
    items = db.items()
    return items

def addTag(nodeId, tag):
    global db
    if nodeId in db:
        db[nodeId]["tags"].append(tag)
        debug("add tag: {1} to: {0}".format(nodeId, tag))
    else:
        error("item with id: {0} does not exist!".format(nodeId))

def getItem(nodeId):
    global db
    debug("get node: {0}".format(nodeId))
    if nodeId in db:
        return db[nodeId]
    else:
        error("item with id: {0} does not exist!".format(nodeId))
