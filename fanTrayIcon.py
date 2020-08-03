#!/usr/bin/env python

import gi
import os

gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

def main():

    CURRPATH = os.path.dirname(os.path.realpath(__file__))
    icon_path = CURRPATH + "/img/fanIcon.png"

    indicator = appindicator.Indicator.new("customtray",
            icon_path, 
            appindicator.IndicatorCategory.APPLICATION_STATUS)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(menu())
    gtk.main()

def menu():
    menu = gtk.Menu()

    auto = gtk.MenuItem("Fan Auto Speed")
    auto.connect("activate", fan_auto)
    menu.append(auto)

    full = gtk.MenuItem("Fan Full Speed")
    full.connect("activate", fan_fullspeed)
    menu.append(full)

    exit = gtk.MenuItem("Exit")
    exit.connect("activate", quit)
    menu.append(exit)

    menu.show_all()
    return menu

def quit(_):
    gtk.main_quit()

def fan_auto(_):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cmd = "sudo " + dir_path + "/fanControl.sh auto"
    os.system(cmd)

def fan_fullspeed(_):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cmd = "sudo " + dir_path + "/fanControl.sh full"
    os.system(cmd)

if __name__ == "__main__":
    main()
