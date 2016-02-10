import time
import sys
from numpy import sqrt
import pydot
import re
import table
import pprint
from collections import defaultdict
from graph_tool.all import *
import sqlite3

def parse(row, uids):
    user       = ""
    rid        = ""
    orcid      = ""
    uni        = []
    department = []
    field      = []

    # test = []
    for uid in uids:
        if len(uid) == 19:
            # ResearcherID
            # 0000-0001-7788-6127
            rid = uid
        elif uid.isdigit() and int(uid) in table.Table:
            e = table.Table[int(uid)]
            if e.type == table.Type.uni:
                uni.append(e.v)
            elif e.type == table.Type.department:
                department.append(e.v)
            elif e.type == table.Type.field:
                field.append(e.v)
        elif uid.isdigit():
            if int(uid) not in table.Table:
                # ORCID
                orcid = uid
                # test.append(uid)
                continue
        else:
            # Probably bad username.
            user = uid

    if not "KTH" in uni:
        return Name("", "", "", "", "", "", "", "")
    # if test:
        # print(test, row)
    # m = re.match("^(?P<first>.*?), (?P<family>.*?) (\[|\().*", row)
    # if not m:
    return Name("", "", user, orcid, rid, uni, department, field)
    # first, family = m.group('first'), m.group('family')
    # return Name(first, family, user, orcid, rid, uni, department, field)
    # return Name(first, family, user, orcid, rid, uni, department, field)

class Name(object):
    def __init__(self, first, family, user, orcid, rid, uni, department, field):
        self.first      = first
        self.family     = family
        self.user       = user
        self.orcid      = orcid
        self.rid        = rid
        self.uni        = uni
        self.department = department
        self.field      = field

    def __str__(self):
        return pprint.pformat([self.first, self.family, self.user, self.rid, self.orcid, self.uni, self.department, self.field])

pat = re.compile("\[.*?\]")
nameToVertex = {}
def parse_row(names, row, g):
    buddies = []
    for n in names:
    #     for row in line.split(';'):
        # Find everything within square brackets: [...].
        uids = [uid[1:-1] for uid in pat.findall(n)]
        if not uids:
            continue
        name = parse(n, uids)
        if not name.user:
            continue
        # print(name.user)
        # v = g.add_vertex()
        buddies.append(name.user)
        # researchers[name.user].extend(name.field)
        # print(name)
        # Create edges for collabs.
        # Isolated nodes are ignored.
        for i in range(1, len(buddies)):
            v1, v2 = Vertex, Vertex
            if buddies[0] in nameToVertex:
                v1 = nameToVertex[buddies[0]]
            else:
                v1 = g.add_vertex()
                nameToVertex[buddies[0]] = v1

            if buddies[i] in nameToVertex:
                v2 = nameToVertex[buddies[i]]
            else:
                v2 = g.add_vertex()
                nameToVertex[buddies[i]] = v2

            g.add_edge(v1, v2)

# g = Graph(directed=False)
# conn = sqlite3.connect('/home/_/kth/kexet/db/kex.db')
# with conn:
#     conn.row_factory = sqlite3.Row
#     cur = conn.cursor()
#     cur.execute("SELECT * from final where name like '%kth%' and keywords is not null and year > 2012 and ContentType = 'Refereegranskat';")
#     # cur.execute("SELECT * FROM final WHERE name like '%kth%' and keywords not null;")
#     while True:
#         row = cur.fetchone()
#         if not row:
#             break
#         parse_row(row['name'].split(';'), row, g)
#
# print(g.num_vertices())
# print(g.num_edges())
# print("[!] db & parse %ss\n" % round(time.time() - start_time, 2))
# g.save('a.gt')
# largest = label_largest_component(g)
# g.set_vertex_filter(largest)
# print(g.num_vertices())
# print(g.num_edges())

start_time = time.time()
g = load_graph('a.gt')
print("[!] loading %ss\n" % round(time.time() - start_time, 2))
# g = GraphView(g, vfilt=label_largest_component(g))
# g.purge_vertices()
# state = minimize_nested_blockmodel_dl(g, deg_corr=True)
# t = get_hierarchy_tree(state)[0]
# tpos = pos = radial_tree_layout(t, t.vertex(t.num_vertices() - 1), weighted=True)
# cts = get_hierarchy_control_points(g, t, tpos)
# pos = g.own_property(tpos)
# b = state.levels[0].b
# shape = b.copy()
# shape.a %= 14
# graph_draw(g, pos=pos, vertex_fill_color=b, vertex_shape=shape, edge_control_points=cts,
#                edge_color=[0, 0, 0, 0.3], vertex_anchor=0, output="netscience_nested_mdl.pdf")
#


# state = minimize_nested_blockmodel_dl(g, deg_corr=True)
# draw_hierarchy(state, output="a.pdf")
# pos = radial_tree_layout(g, g.vertex(2))
# deg = g.degree_property_map("out")
# print(deg)
# deg.a = 4 * (sqrt(deg.a) * 0.5 + 0.4)
# print(deg.a)
# graph_draw(
#     # General options
#     g,
#     # pos=pos,
#     # vorder=deg,
#     # nodesfirst=True,
#     # bg_color=[1., 1., 1., 1],
#     output_size=(4096, 4096),
#     output="a.pdf",
#
#     # Vertx properties
#     vertex_shape='hexagon',
#     vertex_color=[0., 0., 0., 1],
#     vertex_fill_color=[0.5, 0.5, 1, 0.8],
#     # vertex_size=deg,
#     # vertex_size=5
# )

start_time = time.time()
pos = random_layout(g)
graph_draw(g, pos=pos, output_size=(4096, 4096), output="e.pdf")
print("[!] random %ss\n" % round(time.time() - start_time, 2))

start_time = time.time()
pos = radial_tree_layout(g, g.vertex(1))
graph_draw(g, pos=pos, output_size=(4096, 4096), output="d.pdf")
print("[!] radial tree %ss\n" % round(time.time() - start_time, 2))

start_time = time.time()
pos = sfdp_layout(g)
graph_draw(g, pos=pos, output_size=(4096, 4096), output="a.pdf")
print("[!] sfdp %ss\n" % round(time.time() - start_time, 2))

start_time = time.time()
pos = arf_layout(g)
graph_draw(g, pos=pos, output_size=(4096, 4096), output="c.pdf")
print("[!] arf %ss\n" % round(time.time() - start_time, 2))

start_time = time.time()
pos = fruchterman_reingold_layout(g)
graph_draw(g, pos=pos, output_size=(4096, 4096), output="b.pdf")
print("[!] fruchterman reingold %ss\n" % round(time.time() - start_time, 2))


# tree = min_spanning_tree(g)
# g.set_edge_filter(tree)
# print(g.num_vertices())
# print(g.num_edges())
#
# pm, hist = label_components(g)
# print(pm)
# print(hist)
# print(g.num_vertices())
# print(g.num_edges())
