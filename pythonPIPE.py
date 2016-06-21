#!/usr/bin/env python

from subprocess import Popen,PIPE

proc = Popen(['ps','-aux'],stdout=PIPE)
output=proc.communicate()[0]
print output


