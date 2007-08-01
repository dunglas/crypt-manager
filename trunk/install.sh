#!/bin/bash
mkdir /usr/share/foldercrypt/
cp foldercrypt-gtk/share/foldercrypt.glade /usr/share/foldercrypt/
cp foldercrypt-gtk/share/icon.png /usr/share/foldercrypt/
cp foldercrypt-gtk/share/foldercrypt.desktop /usr/share/applications/
cp foldercrypt/foldercrypt.py /usr/lib/python2.5/
chmod a+rx foldercrypt/foldercrypt foldercrypt-gtk/foldercrypt-gtk
cp foldercrypt/foldercrypt foldercrypt-gtk/foldercrypt-gtk /usr/bin
cp nautilus-foldercrypt/crypt.py /usr/lib/nautilus/extensions-1.0/python/
python foldercrypt-kde/setup.py install
