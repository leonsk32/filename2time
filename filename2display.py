#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import time

targetDir = "pictures/"
count = 0
for fileName in os.listdir(targetDir):
    temp = fileName.split(".")[0]
    if not temp:
        continue
    unix = int(temp)/1000
    f = targetDir + fileName

    count += 1
    print str(count) + " " + f + ":" + time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(int(unix))) + " " + str(count)
print str(count) + " files done"
