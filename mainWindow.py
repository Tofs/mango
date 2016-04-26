import sys
try:
 	import pygtk
  	pygtk.require("2.0")
except:
  	pass
try:
	import gtk
  	import gtk.glade
except:
	sys.exit(1)


def hello(button):
    print("hello")

class MainWindow:
    def __init__(self):
        #Set the Glade file
        self.gladefile = "c:\Git\mango\mainWindow.glade"
        builder = gtk.Builder()
        builder.add_from_file(self.gladefile)
        handlers = {
            "onDeleteWindow": gtk.main_quit,
            "onButtonPressed": hello
        }
        builder.connect_signals(handlers)

        #Get the Main Window, and connect the "destroy" event
        self.window = builder.get_object("MainWindow")
        self.window.show_all()




if __name__ == "__main__":
	hwg = MainWindow()
	gtk.main()
