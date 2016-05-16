#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os

targetDir = "pictures/"
count = 0
for fileName in os.listdir(targetDir):
    temp = fileName.split(".")[0]
    if not temp:
        continue
    unix = int(temp)/1000
    f = targetDir + fileName
    s = os.stat(f)

    os.utime(f, (unix,unix))

    print "convert done " + f
    count += 1
print str(count) + " files done"
