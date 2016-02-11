import pprint
import re

from graph_tool.all import *
from table import (Table, Type)

vertices = {}
edges = {}
group_numbers = {
    5956:0,
    5903:1,
    6023:2,
    5977:3,
    5994:4,
    5850:5,
    6172:6,
    6091:7,
    5923:8,
    6161:9,
}

# 5956:cerise 'Skolan för datavetenskap och kommunikation (CSC)', Type.department),
# 5903:gul? 'Skolan för bioteknologi (BIO)', Type.department),
# 6023:brun 'Skolan för industriell teknik och management (ITM)', Type.department),
# 5977:vit 'Skolan för elektro- och systemteknik (EES)', Type.department),
# 5994:blå? 'Skolan för informations- och kommunikationsteknik (ICT)', Type.department),
# 5850:purple 'Skolan för arkitektur och samhällsbyggnad (ABE)', Type.department),
# 6172:svart/röd 'Skolan för teknikvetenskaplig kommunikation och lärande (ECE)', Type.department),
# 6091:fysik 'Skolan för teknikvetenskap (SCI)', Type.department),
# 5923:gul 'Skolan för kemivetenskap (CHE)', Type.department),
# 6161:blå/vit 'Skolan för teknik och hälsa (STH)', Type.department),

color_table = {
    5956: [.8862745098039215, .0, .4980392156862745, 1.],
    # 5903:"gul?",
    6023:[.40, .20, 0., 1.],
    5977:[1., 1., 1., 1.],
    5994:[.86, .60, 1., 1.],
    5850:[.5, 0, .5, 1.],
    # 6172:"svart/r;d",
    6091:[1., .39, .16, 1.],
    5923:[1., .93, 0., 1.],
    6161:[.67, .84, .90, 1.],
}

PAT = re.compile(r"\[.*?\]")

def name(n, uids):
    n = Name("", "", "", 0, "", [], [], [])
    for uid in uids:
        if len(uid) == 19:
            # ResearcherID
            # 0000-0001-7788-6127
            n.rid = uid
        elif uid.isdigit() and int(uid) in Table:
            e = Table[int(uid)].type
            if e == Type.uni:
                n.uni.append(Code(int(uid)))
            elif e == Type.department:
                n.department.append(Code(int(uid)))
            elif e == Type.field:
                n.field.append(Code(int(uid)))
        elif uid.isdigit():
            if int(uid) not in Table:
                # ORCID
                n.orcid = int(uid)
                continue
        else:
            # Username
            n.user = uid
    return n


def names(names):
    nobjs = []
    for n in names:
        # Find everything within square brackets: [...].
        uids = [uid[1:-1] for uid in PAT.findall(n)]
        if not uids:
            continue
        nobjs.append(name(n, uids))
    return nobjs


class Code(object):
    def __init__(self, code):
        self.code = code

    def __eq__(self, c2):
        return self.code == c2.code

    def __str__(self):
        if self.code in Table:
            return Table[self.code].v
        else:
            return self.code + " "

class Name(object):
    def __init__(self, first, family, user, orcid, rid, uni, department, field):
        self.first = first
        self.family = family
        self.user = user
        self.orcid = orcid
        self.rid = rid
        self.uni = uni
        self.department = department
        self.field = field
        self.color = ""

    def __str__(self):
        return pprint.pformat([self.first, self.family, self.user, self.rid, self.orcid, self.uni, self.department, self.field])
