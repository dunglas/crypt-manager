# Introduction #

_cryptmanger.py_ is a Python module wich allow to manage an encrypted folder list, encrypt, open, close and uncrypt folders.


# Details #

_cryptmanager.py_ is composed of 4 public classes (and some privates classes, see the code for details):
  * Data: access to main folder list.
  * Folder: structure representing a folder.
  * Folders: list of folders and operations on list.
  * Manage: operations on a folder.

## Data ##

_Data()_
  * Return a _Folders_ object (pickeling).

  * _folders_ is the current _Folders_ object.

Data has one public method:
  * _save()_ save the current _Folders object._

## Folder ##

_Folder(path)_
  * _path_ represent the full path to the mount point (the encrypted directory).
  * _crypt_ is the place where encrypted data are stored.
  * _digest_ contain the sha256 hash of the path name.

_Folder_ has no public method.

## Folders ##

_Folders()_
  * _li_ is a list of _Folder_

_Folder has 5 publics methods:_
  * _add(folder)_ add a _Folder_ to the list _li_. Raise an _AlreadyExists_ exception if the _Folder_ is already in the list.
  * _rem(folder)_ remvoe a _Folder_ of the list _li_.
  * _update(folder)_ update a _Folder_ which the list _li_ contain.
  * _get(path)_ return a _Folder_ if it is in the list. Either raise an _Uncrypted_ exception.
  * _clean()_ update the object to the current real status and remove out of dates entries.

## Manage ##

_Manage(folder)_
  * Manage the specified _Folder_

_Manage has 4 publics methods:_
  * _crypt(password)_ encrypt the _Folder_ with _password_. Raise a _LoError_ exception if no loopback device available. Raise a _IMGexists_ exception if an ecrypted image already exists for this _Folder_.
  * _mount(password)_ open the _Folder_ to is _path_ using _password_. Raise a _BadPassword_ exception if the password is wrong.  Raise an _AlreadyOpened_ exception if the encrypted folder is already open.
  * _unmount()_ close the _Folder_. Raise a _NotOpened_ exception if the _Folder_ was not open.
  * _uncrypt(password)_ uncrypt the crypted _Folder_. Raise a _BadPassword_ exception if the password is wrong.