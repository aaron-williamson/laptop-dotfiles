#!/usr/bin/python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
import subprocess

lockProg = "/home/aaron/.config/i3/scripts/pixellock.sh"
logoutCmd = ["/usr/bin/i3-msg", "exit"]
shutdownCmd = ["sudo", "systemctl", "poweroff"]
rebootCmd = ["sudo", "systemctl", "reboot"]

class ExitMenu(Gtk.Window):

    # Constructor
    def __init__(self):
        # Customizable exit dialog
        exitDialog = "Exiting i3wm..."

        Gtk.Window.__init__(self, title="Exit")

        self.set_border_width(10)
        self.set_type_hint(Gdk.WindowTypeHint.DIALOG)
        self.set_decorated(False)

        # Enable button images
        settings = Gtk.Settings.get_default()
        settings.set_property("gtk_button_images", True)

        # The dialog for the exit menu
        exitDialog = Gtk.Label(exitDialog)

        # Create the different boxes
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        dummybox = Gtk.Box()

        # Set homogeneity
        vbox.set_homogeneous(True)
        hbox1.set_homogeneous(True)
        hbox2.set_homogeneous(True)
        hbox3.set_homogeneous(True)

        # Add the master box to our panel
        self.add(vbox)

        # Add the dialog and both sub-boxes
        vbox.pack_start(exitDialog, True, True, 0)
        vbox.pack_start(hbox1, True, True, 0)
        vbox.pack_start(hbox2, True, True, 0)
        vbox.pack_start(hbox3, True, True, 0)

        # Get all the images needed
        shutdownIcon = Gtk.Image()
        shutdownIcon.set_from_icon_name("system-shutdown", 2)

        rebootIcon = Gtk.Image()
        rebootIcon.set_from_icon_name("system-reboot", 2)

        logoutIcon = Gtk.Image()
        logoutIcon.set_from_icon_name("system-log-out", 2)
        logoutIcon.set_padding(2,0)

        lockIcon = Gtk.Image()
        lockIcon.set_from_icon_name("system-lock-screen", 2)
        lockIcon.set_padding(2,0)

        cancelIcon = Gtk.Image()
        cancelIcon.set_from_icon_name("edit-delete", 1)

        shutdownButton = Gtk.Button(label="Shut Down")
        shutdownButton.set_image(shutdownIcon)
        shutdownButton.connect("clicked", self.shutdown)
        hbox1.pack_start(shutdownButton, True, True, 0)

        rebootButton = Gtk.Button(label="Reboot")
        rebootButton.set_image(rebootIcon)
        rebootButton.connect("clicked", self.reboot)
        hbox1.pack_start(rebootButton, True, True, 0)

        lockButton = Gtk.Button(label="Lock")
        lockButton.set_image(lockIcon)
        lockButton.connect("clicked", self.lock)
        hbox2.pack_start(lockButton, True, True, 0)

        logoutButton = Gtk.Button(label="Log Out")
        logoutButton.set_image(logoutIcon)
        logoutButton.connect("clicked", self.logout)
        hbox2.pack_start(logoutButton, True, True, 0)

        cancelButton = Gtk.Button(label="Cancel")
        cancelButton.set_image(cancelIcon)
        cancelButton.connect("clicked", Gtk.main_quit)
        hbox3.pack_start(dummybox, True, True, 0)
        hbox3.pack_start(cancelButton, True, True, 0)

    # Function definitions
    def logout(self, widget):
        subprocess.call(logoutCmd)
        Gtk.main_quit()

    def shutdown(self, widget):
        subprocess.call(logoutCmd)
        subprocess.call(shutdownCmd)

    def reboot(self, widget):
        subprocess.call(logoutCmd)
        subprocess.call(rebootCmd)

    def lock(self, widget):
        subprocess.call(lockProg)
        Gtk.main_quit()

# Main function
win = ExitMenu()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
