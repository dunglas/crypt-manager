#!/usr/bin/python
# vim: set fileencoding=utf-8 :
# Copyright (C) 2007 Kévin Dunglas <dunglas@gmail.com>
# Copyright (C) 2003-2006 by Simon Edwards <simon@simonzone.com>
#
# Authors:
#  Kévin Dunglas
#
# This program is a part of a the Google Summer Of Code 2007
# For futher information see :
# http://code.google.com/soc/ubuntu/appinfo.html?csaid=EF4FCF874D88234
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA 02111-1307 USA
#
# Setup script based on Guidance - http://www.simonzone.com/software/guidance/

from distutils.core import Extension
import kdedistutils

def doit():
    kdedistutils.setup(name="conceal-kde",
        version="0.0.5",
        author="Kévin Dunglas",
        author_email="dunglas@gmail.com",
        url="http://code.google.com/p/crypt-manager/",
        min_kde_version = "3.0.0",
        min_qt_version = "3.0.0",
        license = "GPL",
        application_data = ["conceal-kde.py"],
        executable_links = [("conceal-kde", "conceal-kde.py")],
        kcontrol_modules = [("conceal-kde.desktop", "conceal-kde")],

        py_modules=["ui.WindowOpen", "ui.WindowCrypt", "ui.WindowDecrypt",\
            "ui.WindowManager", "ui.WindowProperties", "ui.WindowError"])
doit()
