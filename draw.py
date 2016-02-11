import time
from numpy import sqrt
from graph_tool.all import *
import logging as log

def draw(g, filename, pos=None):
    # for e in ebet.a:
    #     log.info(e)
    vcolors = g.vertex_properties["colors"]
    # etimes.a = sqrt(4 * etimes.a)
    deg = g.degree_property_map("out")
    # deg.a /= deg.a.max()
    deg.a = 10 * (sqrt(deg.a) * 0.5 + 0.4)
    # control = g.new_edge_property("vector<double>")
    # for e in g.edges():
    #     d = sum((pos[e.source()].a - pos[e.target()].a) ** 2)/1000
    #     control[e] = [0.3, d, 0.7, d]
    #     log.info([0.3, d, 0.7, d])
    etimes = g.edge_properties["times"]
    # vshapes = g.vertex_properties["groups"]
    etimes.a = 1 * (sqrt(etimes.a) * 2 + 0.4)
    # etimes.a = [(a*etimes.a.max() / 50)**(1/2) for a in etimes.a]
    # for a in etimes.a:
    #     log.info(a)
    # etimes.a /= etimes.a.max() / 100.
    # etimes.a /= (etimes.a.max() / etimes)**(1 / 5)
    # ebet = betweenness(g)[1]
    # ebet.a /= ebet.a.max() / 10.
    graph_draw(
        g,
        pos=pos,
        output_size=(4096, 4096),
        output=filename,

        # Vertex properties
        vertex_halo=True,
        vertex_anchor=1,
        vertex_halo_color=[.9, .9, .9, .8],
        vertex_halo_size=1.1,
        vertex_size=deg,
        vertex_fill_color=vcolors,
        vertex_color=[0., 0., 0., 1.],
        vorder=deg,

        # Edge properties
        edge_marker_size=etimes,
        edge_pen_width=etimes,
        # edge_color=ebet,
        edge_color=[.4, .4, .4, .4],
        # edge_control_points=control,
    )

def largest(g):
    start_time = time.time()
    largest = label_largest_component(g)
    g.set_vertex_filter(largest)
    draw(g, "out/largest.pdf")
    g.clear_filters()
    log.info("largest component %ss" % round(time.time() - start_time, 2))

def radial_highest(g):
    # Find max degree vertex.
    start_time = time.time()
    highest = 0
    for v in g.vertices():
        if highest < v.out_degree():
            highest = v.out_degree()
    pos = radial_tree_layout(g, g.vertex(highest))
    draw(g, "out/radial_highest.pdf", pos=pos)
    log.info("radial tree (highest) %ss" % round(time.time() - start_time, 2))

def radial_random(g):
    start_time = time.time()
    pos = radial_tree_layout(g, g.vertex(1))
    draw(g, "out/radial_random.pdf", pos=pos)
    log.info("radial tree (random) %ss" % round(time.time() - start_time, 2))

def sfdp(g):
    start_time = time.time()
    # vgroups = g.vertex_properties["groups"]
    # pos = sfdp_layout(g, groups=vgroups)
    pos = sfdp_layout(g)
    draw(g, "out/sfdp.pdf", pos=pos)
    log.info("sfdp %ss" % round(time.time() - start_time, 2))

def grouped_sfdp(g):
    start_time = time.time()
    vgroups = g.vertex_properties["groups"]
    # pos = sfdp_layout(g, groups=vgroups)
    pos = sfdp_layout(g, C=1, p=2, K=None, theta=0.6, max_level=11, groups=vgroups, gamma=0, mu=1.6, mu_p=1.)
    draw(g, "out/group_sfdp.pdf", pos=pos)
    log.info("group_sfdp %ss" % round(time.time() - start_time, 2))

def min_tree(g):
    start_time = time.time()
    tree = min_spanning_tree(g)
    g.set_edge_filter(tree)
    draw(g, "out/min-tree.pdf")
    g.clear_filters()
    log.info("min-spanning tree %ss" % round(time.time() - start_time, 2))

def hierarchy(g):
    start_time = time.time()
    state = minimize_nested_blockmodel_dl(g, deg_corr=True)
    draw_hierarchy(state, output="out/hierarchy.pdf")
    log.info("hierarchy %ss" % round(time.time() - start_time, 2))

def fruchterman(g):
    start_time = time.time()
    pos = fruchterman_reingold_layout(g)
    graph_draw(g, pos=pos, output_size=(4096, 4096), output="out/fruchterman.pdf", edge_pen_width=g.edge_properties["times"])
    log.info("fruchterman reingold %ss" % round(time.time() - start_time, 2))

def netscience(g):
    start_time = time.time()
    g = GraphView(g, vfilt=label_largest_component(g))
    g.purge_vertices()
    state = minimize_nested_blockmodel_dl(g, deg_corr=True)
    t = get_hierarchy_tree(state)[0]
    tpos = pos = radial_tree_layout(t, t.vertex(t.num_vertices() - 1), weighted=True)
    cts = get_hierarchy_control_points(g, t, tpos)
    pos = g.own_property(tpos)
    b = state.levels[0].b
    shape = b.copy()
    shape.a %= 14
    graph_draw(g, pos=pos, vertex_fill_color=b, vertex_shape=shape, edge_control_points=cts,
                   edge_color=[0, 0, 0, 0.3], vertex_anchor=0, output="out/netscience_nested_mdl.pdf")
    log.info("netscience nested mdl %ss" % round(time.time() - start_time, 2))

def minimize_blockmodel(g):
    start_time = time.time()
    g = GraphView(g, vfilt=label_largest_component(g))
    g.purge_vertices()
    state = minimize_blockmodel_dl(g)
    b = state.b
    pos = sfdp_layout(g)
    graph_draw(g, pos=pos, vertex_fill_color=b, vertex_shape=b, output="out/minimize_blockmodel.pdf")
    log.info("minimize blockmodel %ss" % round(time.time() - start_time, 2))
