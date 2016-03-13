import pygtk
import gtk

class helloworld:
    def helloworld(self, wiget, data=None):
        print("Hello world from mango brain!")

    def delete_event(self, widget, event, data=None):
        print("Delete event")
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)
        self.window.show()







        self.verticalbox = gtk.VBox(False, 0)
        self.window.add(self.verticalbox)
        self.verticalbox.show()


        self.title = gtk.Label("Mango mapper")
        self.verticalbox.pack_start(self.title, True, True, 0)
        self.title.show()


        self.mainTable = gtk.Table(rows=1 , columns=1)
        self.verticalbox.pack_start(self.mainTable, True, True, 0)
        self.mainTable.show()



        # self.button1 = gtk.Button("Hello world! 1")
        # self.button2 = gtk.Button("Hello world! 2")
        # self.button1.connect("clicked", self.helloworld, None)
        # self.button2.connect("clicked", self.helloworld, None)
        # self.box1 = gtk.HBox(False, 0)
        # self.box1.pack_start(self.button1, True,True, 0)
        # self.box1.pack_start(self.button2, True,True, 0)
        # self.button1.connect_object("clicked",  gtk.Widget.destroy, self.window)
        #
        # self.window.add(self.box1)
        # self.button1.show()
        # self.button2.show()
        # self.box1.show()


        # show things

    def main(self):
        gtk.main()


if __name__ == "__main__":
    hello = helloworld()
    hello.main()
