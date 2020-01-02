###
### natgeo-potd-wallpaper.py - by Jason Woyak (jason@woyak.com)
### 
### Parses the National Geographic Photo of the Day site's JSON feed,
### grabs the latest image, copies it locally to the hard drive, and
### sets it as the wallpaper.
### 
### NOTE: The photos are NOT used with permission (though I am pretty
###       sure this is governed under 'fair use'). If you use this 
###       for any reason, you should subscribe to Nat Geo!
###

import ctypes 
import os
import urllib.request as request
import datetime
import json
import platform

# Print a nice header
header = "NatGeo Photo of the Day Downloader - by Jason Woyak"
print(header)
headerlen = int(len(header))
for i in header:
        print("-", end="")

# Get the JSON feed
print("\nParsing photo metadata from JSON\n")        
now=datetime.datetime.now()
curMonth = str(now.year) + "-" + str(now.month)
baseURI = "https://www.nationalgeographic.com/photography/photo-of-the-day/_jcr_content/.gallery."
url = baseURI + curMonth + ".json"
#url = "https://www.nationalgeographic.com/photography/photo-of-the-day/_jcr_content/.gallery.2019-12.json"
with request.urlopen(url) as response:
        source = response.read()
        data = json.loads(source)

# Parse out the latest Photo's metadata
natGeoPOTD = (data['items'][0]['image']['uri'])
natGeoPOTDtitle = (data['items'][0]['image']['title'])
natGeoPOTDcaption = (data['items'][0]['image']['caption'])
POTDfile = "natgeo-potd.jpg" # Set an absolute path here if you need to change the photo download location
print("Photo URI:\n" + natGeoPOTD)
print("\nCaption:\n" + natGeoPOTDcaption)

# OS Dependent wallpaper/downloading:
myOS = platform.system()

if (myOS == "Windows"):
        # Download the photo to the location in the POTDfile variable
        print("Downloading Photo...")
        request.urlretrieve(natGeoPOTD, POTDfile)
      
        # Set the wallpaper - this only works in windows! 
        SPI_SET_WALLPAPER = 20
        pathToBmp = os.path.abspath(POTDfile)
        print("Setting wallpaper to " + pathToBmp + "...")
        ctypes.windll.user32.SystemParametersInfoW(SPI_SET_WALLPAPER, 0,pathToBmp, 3)
elif (myOS == "Linux"):
        linuxCMD = "gsettings set org.gnome.desktop.background " + natGeoPOTD
        os.system(linuxCMD)
#elif (myOS == "Darwin"):
#       Hey Mac Users! I don't have a Mac to test this on! YMMV!


# Write metadata to HTML file - mostly as a way to link to NatGeo!
print("Writing about-photo.html ...")
HTMLpath = 'about-photo.html'
HTML_file = open(HTMLpath,'w')

HTMLstart = "<html><body>\n"
HTML_file.write(HTMLstart)

HTMLphoto = "<img src=\"" + POTDfile + "\" width=600 />\n"
HTML_file.write(HTMLphoto)

HTMLtitle = "<h2>" + natGeoPOTDtitle + "</h2>\n"
HTML_file.write(HTMLtitle)

HTMLcaption = natGeoPOTDcaption + "\n"
HTML_file.write(HTMLcaption)

HTMLlink = "<p><a href=\"https://www.nationalgeographic.com/photography/photo-of-the-day/\">Visit the Photo of the Day site to learn more</a></p>\n"
HTML_file.write(HTMLlink)

HTMLend = "</html></body>\n"
HTML_file.write(HTMLend)

HTML_file.close()