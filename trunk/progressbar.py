import threading
import gtk
import gtk.glade
from time import sleep
# Example of working progressbar using threads...
#Initializing the gtk's thread engine

class Test1(threading.Thread):
    def run(self):
        i = 0
        while i < 100000:
            print "test1 " + str(i)
            i += 1
        p.stop()

class Pulser(threading.Thread):
    """Pulse the progressbar"""
    
    stopthread = threading.Event()
    
    def run(self):
        while not self.stopthread.isSet() :
            gtk.gdk.threads_enter()
            widgets["progressbar_progressbar"].pulse()
            gtk.gdk.threads_leave()
            sleep(0.1)

    def stop(self):
        """Stop method, sets the event to terminate the thread's main loop"""
        self.stopthread.set()

class WidgetsWrapper:
    """Wrapper for GTK/Galde widgets"""
    def __init__(self):
        """Display a window"""
        #gnome.init(APPNAME, APPVERSION)
        self.widgets = gtk.glade.XML("gcrypt-manager.glade")

    def __getitem__(self, key):
        """Allow to use widgets['widget_name'].action()"""
        return self.widgets.get_widget(key)

    def hide_or_quit(self, name):
        """Hide or quit the window"""
        if widgets["manager"].get_property("visible"):
            widgets[name].hide()
            widgets["manager"].set_sensitive(True)
        else:
            self.quit()

    def quit(self):
        """Quit the program"""
        gtk.main_quit()

class Progressbar:
    def start(self):
        widgets["progressbar"].show()
        self.pulser = Pulser()
        self.pulser.start()

    def stop(self):
        widgets["progressbar"].hide()
        self.pulser.stop()

#Creating and starting the thread
#pulser = Pulser()
#pulser.start()
class Encrypt:
    def __init__(self):
        p = Progressbar()
        p.start()
        t = Test1()
        t.start()

widgets = WidgetsWrapper()
Encrypt()
gtk.main()
