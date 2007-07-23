#!/bin/bash
mkdir /usr/share/gcrypt-manager/
cp gcrypt-manager/share/gcrypt-manager.glade /usr/share/gcrypt-manager/
cp gcrypt-manager/share/icon.png /usr/share/gcrypt-manager/
cp gcrypt-manager/share/gcrypt-manager.desktop /usr/share/applications/
cp python-cryptmanager/cryptmanager.py /usr/lib/python2.5/
chmod a+rx crypt-manager/crypt-manager gcrypt-manager/gcrypt-manager
cp crypt-manager/crypt-manager gcrypt-manager/gcrypt-manager /usr/bin
cp nautilus-crypt/crypt-manager.py /usr/lib/nautilus/extensions-1.0/python/
