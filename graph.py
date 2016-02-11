from graph_tool.all import *

from parse import (Name, Code)

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


def add_relation(g, nobjs, e_times, v_colors, v_groups):
    # List of collaborators.
    collabs = []
    for n in nobjs:
        # We only use the big research departments atm.
        if not Code(177) in n.uni:
            continue
        if not n.user:
            continue
        if not n.department:
            continue
        if n.department[0].code not in color_table:
            continue
        collabs.append(n)
        # We ignore individual research.
        for i in range(1, len(collabs)):
            a, b = collabs[0], collabs[i]
            v1, v2 = None, None

            # Reuse vertices.
            if a.user in vertices:
                v1 = vertices[a.user]
            else:
                v1 = new_vertex(g, a, v_colors, v_groups)
            if b.user in vertices:
                v2 = vertices[b.user]
            else:
                v2 = new_vertex(g, b, v_colors, v_groups)

            # Reuse edges.
            if hash(a, b) in edges:
                inc_collab(hash(a, b), len(collabs), e_times)
            elif hash(b, a) in edges:
                inc_collab(hash(b, a), len(collabs), e_times)
            else:
                new_collab(g, v1, v2, hash(a, b), len(collabs), e_times)


def new_vertex(g, z, v_colors, v_groups):
    v = g.add_vertex()
    vertices[z.user] = v
    v_colors[v] = color_table[z.department[0].code]
    v_groups[v] = group_numbers[z.department[0].code]
    return v


def hash(a, b):
    return a.user + " " + b.user


def inc_collab(h, n, e_times):
    """Increase collaboration between the researchers"""
    e_times[edges[h]] += 1.0/n


def new_collab(g, v1, v2, h, n, e_times):
    """Create a new collaboration edge between v1 and v2"""
    e = g.add_edge(v1, v2)
    edges[h] = e
    e_times[e] = 1.0/n
