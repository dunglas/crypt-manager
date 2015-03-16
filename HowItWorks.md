# Introduction #

_Crypt Manager_ maintain a list of encrypted folders, and stock encrypted images on a specific format.


# Details #

## Process ##

### Folder encryption ###
  * Creation of the encrypted folder in ~/.cryptmanager/crypt/SHA256\_DIGEST
  * Move of existing data in a temporary directory
  * Setup with encfs
  * Copy of files in the temporary dir
  * Unmount
  * Add the folder to the list (object Folders)


### Open an encrypted folder ###
  * Mounting


### Close an encrypted folder ###
  * Unmount


### Uncrypt a folder ###
  * Open the folder
  * Copy data in a temporary directory
  * Close the folder
  * Delete the encrypted disk image
  * Remove the folder from the list (object Folders)


## Files ##
### ~/.config/crypmanager/crypt/ ###

_~/.config/crypmanager/crypt/_ contain all encrypted data. The name of the encrypted folder is the sha256 hash of the mount point full path name. It allow to test if a folder is encrypted because a sha256 hash is unique (low collision risk).

### ~/.config/crypmanager/cache/folders ###

_~/.config/crypmanager/cache/_ contain a file called _folders_ which is a binary serialization of the object "Folders" (the list of encrypted folders) of the cryptmanager.py module.

### /tmp/cryptmanager ###
_/tmp/crypmanager/_ is a temporary space for copy/paste/move operations during the encryption and unencryption process.
It also use the sha256 hash of the path to unique the temporary path and it is cleaned at the end of each process.