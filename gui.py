import gtk
import dbHandler as fileDB
import dbManager as db
import Utils

class helloworld:
    def delete_event(self, widget, event, data=None):
        print("Delete event")
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def addNewItem(self, widget, data=None):
        db.addItem(str(self.addText.get_text()))
        fileDB.Store(db.getDB())

    def refreshTable(self):
        for key, item in db.getItems():
            self.taskStore.append([
                item["status"],
                item["description"],
                str(item["tags"])
            ])

    def createItemList(self):
        self.taskStore = gtk.ListStore(str, str, str)
        self.refreshTable()
        renderer = gtk.CellRendererText()
        toggle = gtk.CellRendererToggle()
        tree = gtk.TreeView(self.taskStore)

        statusColumn = gtk.TreeViewColumn("Status", toggle , text=0)
        descColumn = gtk.TreeViewColumn("Description", renderer, text=1)
        tagColumn = gtk.TreeViewColumn("Tags", renderer, text=2)

        allColumns = [ statusColumn, descColumn, tagColumn ]

        for column in allColumns:
            tree.append_column(column)
        tree.show()

        return tree


    def createAddBar(self):
        # text field
        self.addText = gtk.Entry(max=0)
        self.addText.insert_text("Write new task here", position=0)
        self.addText.show()

        addNewButton = gtk.Button("Add Item")
        addNewButton.show()
        addNewButton.connect("clicked", self.addNewItem, None)

        #build structs
        addNewBar = gtk.HBox(False, 0)
        addNewBar.add(self.addText)
        addNewBar.add(addNewButton)
        addNewBar.show()
        return addNewBar

    def __init__(self):

        addNewBar = self.createAddBar()
        tree = self.createItemList()


        verticalbox = gtk.VBox(False, 0)
        verticalbox.show()
        verticalbox.add(addNewBar)
        verticalbox.add(tree)

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Mango Mapper")
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)
        self.window.show()
        self.window.add(verticalbox)


    def main(self):
        gtk.main()


if __name__ == "__main__":
    Utils.initLogger(False)
    db.setDB(fileDB.Load())
    hello = helloworld()
    hello.main()
    fileDB.Store(db.getDB())
