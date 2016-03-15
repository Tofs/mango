from gtk import Window, VBox, HBox, Entry, Button
import gtk
import dbHandler as fileDB
import dbManager as db
import Utils

class helloworld:
    def helloworld(self, wiget, data=None):
        print("Hello world from mango brain!")

    def delete_event(self, widget, event, data=None):
        print("Delete event")
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def addNewItem(self, widget, data=None):
        db.addItem(str(self.addText.get_text()))
        fileDB.Store(db.getDB())

    def __init__(self):
        self.window = Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Mango Mapper")
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)
        self.window.show()

        verticalbox = VBox(False, 0)
        self.window.add(verticalbox)
        verticalbox.show()




        # create the buttom row, housing add task funcs
        addNewBar = HBox(False, 0)
        verticalbox.add(addNewBar)
        addNewBar.show()

        # text field
        self.addText = Entry(max=0)
        addNewBar.add(self.addText)
        self.addText.insert_text("Write new task here", position=0)
        self.addText.show()

        addNewButton = Button("Add Item")
        addNewButton.show()
        addNewButton.connect("clicked", self.addNewItem, None)
        addNewBar.add(addNewButton)


    def main(self):
        gtk.main()


if __name__ == "__main__":
    Utils.initLogger(True)
    db.setDB(fileDB.Load())
    hello = helloworld()
    hello.main()
    fileDB.Store(db.getDB())
