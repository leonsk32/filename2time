#!/usr/bin/env python
# -*- coding: utf-8 -*-
#必要なのはexifじゃなかった...
#
import sys
import os
import stat
import datetime
import pyexiv2

targetDir = "pictures/"
count = 0
for fileName in os.listdir(targetDir):
    temp = fileName.split(".")[0]
    if not temp:
        continue
    unix = int(temp)/1000
    print temp
    print unix
    date_value = datetime.datetime.fromtimestamp(unix)
    print date_value
    f = targetDir + fileName
    s = os.stat(f)
    #times = (s[stat.S_ENFMTST_MTIME], s[stat.S_ENFMTST_MTIME])
    #mtime = datetime.datetime.fromtimestamp(s[stat.S_ENFMTST_MTIME])

    metadata = pyexiv2.ImageMetadata(f)
    metadata.read()
    dateTimeTag = metadata['Exif.Image.DateTime']
    dateTimeOriginalTag = metadata['Exif.Photo.DateTimeOriginal']
    dateTimeDigitizedTag = metadata['Exif.Photo.DateTimeDigitized']
    thumbnailDateTimeTag = metadata['Exif.Thumbnail.DateTime']

    dateTimeTag.value = date_value
    dateTimeOriginalTag.value = date_value
    dateTimeDigitizedTag.value = date_value
    thumbnailDateTimeTag.value = date_value

    print "convert done " + f + " ->" + dateTimeTag.raw_value
    metadata.write()
    count += 1
print str(count) + " files done"
