import sys
import re

lines = [line.rstrip('\n') for line in open('b.lst')]
i = 0
#         opt      opt
# a, b [username] [???] (school)
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

for line in lines:
    # if i == 3:
    #     sys.exit(0)
    names = line.split(';')
    for name in names:
        test = re.findall("\[.*?\]", name)
        if not test:
            continue
        print(test)
        m = re.search(".*?( (?P<user>\[.*\]) )?\((?P<school>KTH)( \[177\])?(, (?P<dpmt>.*?))?(, (?P<subjects>.*))\)", name)
        if not m:
            # print('no matches')
            # print('\t'+name)
            continue
        if not m.group('school'):
            # print ('not kth')
            continue
        user, school, dpmt, subjects = m.group('user'), m.group('school'), m.group('dpmt'), m.group('subjects')
        if not user:
            user = ""
        if not school:
            school = ""
        if not dpmt:
            dpmt = ""
        if not subjects:
            subjects = ""
        s = School(school, dpmt, subjects)
        # print(name)
        # print(user, s)
    i += 1
