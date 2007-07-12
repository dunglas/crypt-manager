import threading
import gtk
from time import sleep
# Example of working progressbar using threads...
#Initializing the gtk's thread engine
gtk.gdk.threads_init()

class Test1(threading.Thread):
    def run(self):
        i = 0
        while i < 100000:
            print "test1 " + str(i)
            i += 1
        pulser.stop()
        

class Pulser(threading.Thread):
	"""This class sets the fraction of the progressbar"""
	
	def run(self):
		"""Run method, this is the code that runs while thread is alive."""
		
		#While the stopthread event isn't setted, the thread keeps going on
		while not self.stopthread.isSet() :
			# Acquiring the gtk global mutex
			gtk.gdk.threads_enter()
			#Setting a random value for the fraction
			progressbar.pulse()
			# Releasing the gtk global mutex
			gtk.gdk.threads_leave()
			
			#Delaying 100ms until the next iteration
			sleep(0.1)
			
	def stop(self):
		"""Stop method, sets the event to terminate the thread's main loop"""
		threading.Event().set()

def main_quit(obj):
	"""main_quit function, it stops the thread and the gtk's main loop"""
	#Stopping the thread and the gtk's main loop
	pulser.stop()
	gtk.main_quit()

#Gui bootstrap: window and progressbar
window = gtk.Window()
progressbar = gtk.ProgressBar()
window.add(progressbar)
window.show_all()
#Connecting the 'destroy' event to the main_quit function
window.connect('destroy', main_quit)

#Creating and starting the thread
pulser = Pulser()
pulser.start()
t = Test1()
t.start()

gtk.main()
