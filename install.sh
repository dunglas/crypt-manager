#!/bin/bash
mkdir /usr/share/gcrypt-manager/
cp gcrypt-manager.glade /usr/share/gcrypt-manager/
cp cryptmanager.py /usr/lib/python2.5/
chmod a+rx crypt-manager gcrypt-manager
cp crypt-manager gcrypt-manager gcrypt-manager.glade /usr/bin
cp crypt-manager.py /usr/lib/nautilus/extensions-1.0/python/
