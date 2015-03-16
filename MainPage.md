# Introduction #

_Crypt Manager_ is the Google Summer of Code project of **Kévin Dunglas** [1](1.md) for **Ubuntu**, [2](2.md) mentored by **Jani Monoses** [3](3.md).
The goal of this project is to **increase security of sensitives data** especially on computers which can be thieved (like laptops).
_Crypt manager_ is a compilation of tools which allow to **easily encrypt, open, close and uncrypt folders** in a Desktop environment.
It is wrote in Python [4](4.md), it EncFS [5](5.md) as backend.
_Gcrypt Manager_, the graphical interface for _Crypt Manager_ also use Pygtk [6](6.md) and Glade [7](7.md).

_Note: Crypt Manager was using use cryptsetup [8](8.md) and LUKS [9](9.md) as backend at developpement start. See deprecated downloads._

  * [1](1.md) http://placelibre.ath.cx/keyes/
  * [2](2.md) http://www.ubuntu.com/
  * [3](3.md) http://janimo.blogspot.com/
  * [4](4.md) http://www.python.org/
  * [5](5.md) http://arg0.net/wiki/encfs
  * [6](6.md) http://www.pygtk.org/
  * [7](7.md) http://glade.gnome.org/
  * [8](8.md) http://www.saout.de/misc/dm-crypt/
  * [9](9.md) http://luks.endorphin.org/

# Details #

The Crypt Manager project is composed of three parts:
  * A Python module called _cryptsetup.py_ which perform basics crypt, uncrypt, open and close operations on crypted folders. See CryptManagerModule
  * A command line tool using the module called _crypt-manager_. See CommandLineTool
  * A GTK interface using the module called _gcrypt-manager_. See GcryptManager
  * A Nautilus extension. See GnomeIntegration