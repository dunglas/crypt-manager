# Introduction #

The goal of _Crypt Manager_ is to provide an easy and generic solution to manage encrypted folders on Linux and especially on GTK based desktops (GNOME [1](1.md) and Xfce [2](2.md)).

  * [1](1.md) http://www.gnome.org/
  * [2](2.md) http://www.xfce.org/


# Details #

_Crypt Manager_ is designed for the end user, with it graphical interface, no need to type obscures command lines to keep sensitives data out of view.
Everyone using Linux must be able to encrypt a folder, open and close it just by using it's mouse. _Crypt Manager_ it's the confidentiality for everyone and every companies.

The modularization of the code (see _cryptsetup.py_ Python module) allow to easily wrote applications using this encrypted folder management system.
By example, it will be easy to wrote a KDE [3](3.md) interface using the module.

  * [3](3.md) http://www.kde.org/