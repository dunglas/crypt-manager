#!/bin/bash
mkdir /usr/share/gcrypt-manager/
cp share/gcrypt-manager.glade /usr/share/gcrypt-manager/
cp share/icon.png /usr/share/gcrypt-manager/
cp share/gcrypt-manager.desktop /usr/share/applications/
cp src/cryptmanager.py /usr/lib/python2.5/
chmod a+rx src/crypt-manager src/gcrypt-manager
cp src/crypt-manager src/gcrypt-manager /usr/bin
cp nautilus-extension/crypt-manager.py /usr/lib/nautilus/extensions-1.0/python/
