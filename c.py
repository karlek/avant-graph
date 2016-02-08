import sys
import re

###
# Structure of a name field
###
#         opt      opt
# a, b [username] [???] (university, school, subjects+)

#
class Name(object):
    def __init__(self, first, family, user, uni):
        self.first  = first
        self.family = family
        self.user   = user
        self.uni    = uni

class School(object):
    def __init__(self, school, dpmt, subj):
        self.school = school
        self.dpmt   = dpmt
        self.subj   = subj
    def __str__(self):
        return self.school + "\t" + self.dpmt + "\t" + self.subj

# Read in all lines (not buffered, might crash on bigger files!).
lines = [line.rstrip('\n') for line in open('b.lst')]

for line in lines:
    names = line.split(';')
    for name in names:
        test = re.findall("\[.*?\]", name)
        if not test:
            continue
        print(test)
