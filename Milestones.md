## During the Summer Of Code ##
  * Study encryptions methods on Linux **[OK](OK.md)**
  * Select the more appropriate way **[OK](OK.md)**: cryptsetup/Luks was first selected instead of TrueCrypt because it it is more integrated with Linux, more reliable, more faster, become the standard disk encryption on Linux and TrueCrypt as licence issues (publicity).
  * Make tests. **[OK](OK.md)**
  * Tests with EncFS
  * EncFS is now selected because he run as normal user and do not add a size limit to the folder.
  * Implements the best way to encrypt folders in Python. **[OK](OK.md)**
  * Create a Python module which offer the capability of management, encryption, open, close and uncryption of directories. **[OK](OK.md)** See CryptManagerModule
  * Create a command-line tool using this module. **[OK](OK.md)** See CommandLineTool
  * Create a GTK interface using this module. **[OK](OK.md)** See GcryptManager
  * Release a beta version.
  * Research about integration of GcryptManager with Gnome and Nautilus. See GnomeIntegration **[OK](OK.md)**
  * Create a Nautilus extension **[OK](OK.md)**
  * Release a beta
  * Get feedback, adapt, debug.
  * Package for Ubuntu.

## After ##
  * Start a KDE/QT interface.