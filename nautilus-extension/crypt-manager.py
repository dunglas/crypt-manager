import nautilus
import urllib
import cryptmanager
import subprocess

# Crypt Manager extension for nautilus
EMBLEM = "readonly"

class CryptManagerExtension(nautilus.InfoProvider, nautilus.MenuProvider):
    def __init__(self):
        pass

    def _load_data(self):
        data = cryptmanager.Data()
        self.folders = data.folders
        self.folders.clean()
     
    def _clicked(self, menu, file):
        if self.status == 1:
            p = subprocess.Popen(["gcrypt-manager", "--crypt", self.filename])
            if p.poll() == 0:
                file.add_emblem(EMBLEM)
        if self.status == 2:
            p = subprocess.Popen(["gcrypt-manager", "--close", self.filename])
        if self.status == 3:
            p = subprocess.Popen(["gcrypt-manager", "--open", self.filename])

    def _get_status(self):
        try:
            folder = self.folders.get(self.filename)
        except cryptmanager.NoEncrypted:
            self.status = 1
        else:
            if folder.opened:
                self.status = 2
            else:
                self.status = 3

    def _get_messages(self):
        """1: unencrypted, 2: opened, 3: closed"""
        if self.status == 1:
            self.entry = "Encrypt"
            self.desc = "Encrypt this folder using Crypt Manager"
        elif self.status == 2:
            self.entry = "Close"
            self.desc = "Close this encrypted folder"""
        else:
            self.entry = "Open"
            self.desc = "Open this encrypted folder"

    def update_file_info(self, file):
        self._load_data()
        self.filename = urllib.unquote(file.get_uri()[7:])
        self._get_status()
        print file.get_parent_uri()
        if self.status == 2 or self.status == 3:
            file.add_emblem(EMBLEM)

    def get_file_items(self, window, files):
        self._load_data()
        if len(files) != 1:
            return

        file = files[0]
        self.filename = urllib.unquote(file.get_uri()[7:]) 
        if not file.is_directory():
            return
        
        self._get_status()
        self._get_messages()

        
        menu = nautilus.MenuItem(
            "NautilusPython::CryptManagerExtension",
            self.entry,
            self.desc
        )
        menu.connect("activate", self._clicked, file)
        return menu,
         
    def get_background_items(self, window, file):
        return
