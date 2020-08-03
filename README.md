# Fan Control Tray Icon
A simple fan control tray icon I created to switch between auto mode and full-speed on my Thinkpad Extreme.
<p align="center">
  <img src="https://github.com/NickL77/FanControlTrayIcon/blob/master/img/fanControlTrayIcon.png">
</p>

## Autostart on Startup (tested on Ubuntu 18.04)
Note: This is not an ideal configuration. Writing a file into the sudoer file is not a safe approach, but I went with this as it was the fastest way to get the script to start at start-up.

1. In the package, run `chmod 755 fanControl.sh` (this is very important so non-sudoers can not exploit this configuration to run commands as sudo with a password)
2. Open up visual sudo with `sudo visudo` and add the following line `ALL    ALL = (root) NOPASSWD: <path to package>/fanControl.sh`
3. Add an autostart config file:
    1. `cd ~/.config/autostart`
    2. Create a new file, for example `fanControlTrayIcon.desktop`
    3. Add the following contents:
      ```
      [Desktop Entry]
      Type=Application
      Name=Fan Control Tray Icon
      Exec=<path to package>/fanTrayIcon.py
      X-GNOME-Autostart-enabled=true
      ```
## Resources
* Controlling fans on Thinkpads [[1](http://www.thinkwiki.org/wiki/How_to_control_fan_speed)]
* Creating a tray icon [[2](https://fosspost.org/tutorials/custom-system-tray-icon-indicator-linux)] [[3](http://candidtim.github.io/appindicator/2014/09/13/ubuntu-appindicator-step-by-step.html)]
* Running a script on start up [[4](https://stackoverflow.com/questions/8247706/start-script-when-gnome-starts-up)]
