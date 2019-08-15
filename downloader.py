#!/usr/bin/python
import datetime
import urllib.request
import os

baseUrl = "http://loveline.noxsolutions.com/mp3/LL-"
baseDate = datetime.date(2013, 9, 9)
urlList = []
dateList = []

print("Generating download information...")
for i in range(365):
    newDate = baseDate + datetime.timedelta(days = i)
    # Loveline didn't air on these days.
    if(newDate.weekday() != 4 and newDate.weekday() != 5):
        urlList.append(baseUrl + str(newDate) + ".mp3")
        dateList.append("Loveline - " + str(newDate) + ".mp3")

print("Beginning downloads...")
os.mkdir('Loveline')
for j in range(len(urlList)):
    try:
        # File will download in the current directory
        mp3file = urllib.request.urlretrieve(urlList[j], "Loveline/" + dateList[j])
        print("(" + str(j+1) + "/" + str(len(urlList)) + "): Successfully downloaded " + dateList[j])
    except:
        # Probably a fix to this; if it fails there may be a nuance in the URL that leads us to find it on a similar web server path
        print("(" + str(j+1) + "/" + str(len(urlList)) + "): Downloaded Forbidden: " + dateList[j])
print("Downloads complete.")
