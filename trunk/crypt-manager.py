import nautilus
import os
import urllib
import cryptmanager
import cPickle

# Crypt Manager extension for nautilus
CACHE = os.environ['HOME'] + "/.cryptmanager/cache"
 
class CryptManagerExtension(nautilus.MenuProvider):
    def __init__(self):
        pass

    def load_data(self):
        if not os.path.exists(os.path.join(CACHE, "folders")):
            return cryptmanager.Folders()
        f = open(os.path.join(CACHE, "folders"), "r")
        folders = cPickle.load(f)
        f.close()
        return folders
     
    def clicked(self, menu, file):
        if self.status == 1:
            os.system('gcrypt-manager --crypt "%s"'%self.filename)
        if self.status == 2:
            os.system('gcrypt-manager --close "%s"'%self.filename)
        if self.status == 3:
            os.system('gcrypt-manager --open "%s"'%self.filename)
     
    def get_file_items(self, window, files):
        if len(files) != 1:
            return

        file = files[0]
        self.filename = urllib.unquote(file.get_uri()[7:]) 
        if not os.path.isdir(self.filename):
            return
        self.folders = self.load_data()
        self.folders.clean()
        
        try:
            folder = self.folders.get(self.filename)
        except cryptmanager.NoEncrypted:
            self.status = 1
            entry = "Encrypt"
            desc = "Encrypt this folder using Crypt Manager"
        else:
            if folder.opened:
                self.status = 2
                entry = "Close"
                desc = "Close this encrypted folder"""
            else:
                self.status = 3
                entry = "Open"
                desc = "Open this encrypted folder"
        
        print self.status
        
        menu = nautilus.MenuItem(
            "NautilusPython::CryptManagerExtension",
            entry,
            desc
        )
        menu.connect("activate", self.clicked, file)
        return menu,
         
    def get_background_items(self, window, file):
        return
