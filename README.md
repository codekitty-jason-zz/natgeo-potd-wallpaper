# natgeo-potd-wallpaper
This unofficial Python 3 script sets the current National Geographic Photo of the Day as the Windows Desktop wallpaper.

NOTE: Please respect the copyright of National Geographic, and the amazing photographers who take these photos. 
This script is intended for unofficial, personal, "fair" use. If you use this for any reason whatsoever, please support them by subscribing.
I am in no way affiliated with National Geographic, and their Photo of the Day and JSON feed are used without consent. 
Use at your own risk.

## Installation on Windows
1. To install this, first you need to install the latest version (3.8.1 as of this writing) of Python 3 for Windows, from here:
https://www.python.org/ftp/python/3.8.1/python-3.8.1.exe
2. Next, download the .zip of this repository and extract it to a folder on your computer someplace you have write access (a natgeo-potd folder in your Documents folder is a fine choice).
3. Test the script by running the set-natgeo-potd-wallpaper.bat file.  Did it change your background?
4. Assuming the script worked just fine, the final task is to open the Task scheduler in windows and schedule the the set-natgeo-potd-wallpaper.bat file to run once per day. This page gives a good description of how to do this:
https://www.thewindowsclub.com/how-to-schedule-batch-file-run-automatically-windows-7

## Installation on Linux (Ubuntu/Gnome)
1. Make sure you have Python3 installed!
2. Clone this repo to somewhere you have write access to
3. Test the script by opening a terminal (Ctrl-Alt-T in Ubuntu), changing directory to where you cloned this repo to, and typing:
[code]python3 ./natgeo-potd-wallpaper.py[/code] 
Did it change your background?
4. Assuming the script worked fine, the final task is to schedule it to run everyday using cron or whatever linux scheduling tool you prefer.  Make sure you specify the FULL path of the .py file, instead of using 
./'! 

## Installation on MacOS, ChromeOS, etc
I haven't gotten this far yet. If you'd like to see me add support for your favorite OS, just let me know!