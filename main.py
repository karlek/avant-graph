"""
Avant graf is a program to visualize the graph properties of research networks
at KTH.
"""

from time import time

from graph_tool import Graph

import draw
import load
import parse
import graph
import logging as log
import argparse

def main():
    """
    Visualizes the research network of KTH as a graph.
    """
    start_time = time()

    # Create our undirected graph to return.
    g = Graph(directed=False)
    # The edge properties measuring collaboration.
    e_times = g.new_edge_property("float")
    # Grouping value for the verticies, verticies are in the same group if the
    # have the same value.
    v_groups = g.new_vertex_property("int")
    # Color the verticies based on their faculties colors.
    v_colors = g.new_vertex_property("vector<double>")

    db_path = '/home/_/kth/kexet/db/kex.db'
    query = """SELECT *
               FROM final
               WHERE (
                 name LIKE '%kth%' and
                 name LIKE '%;%' and
                 keywords is not null and
                 year >= 2013 and
                 ContentType = 'Refereegranskat' and
                 PublicationType = 'Artikel i tidskrift'
               );"""
    rows = load.rows(db_path, query)
    for row in rows:
        nobjs = parse.names(row['name'].split(';'))
        graph.add_relation(g, nobjs, e_times, v_colors, v_groups)

    g.edge_properties["times"] = e_times
    g.vertex_properties["colors"] = v_colors
    g.vertex_properties["groups"] = v_groups

    log.info(g.num_vertices())
    log.info(g.num_edges())
    g.save('a.gt')
    log.info('graph saved: a.gt')
    log.info("db & parse %ss" % round(time() - start_time, 2))

    # start_time = time()
    # g = load_graph('a.gt')
    # log.info("loading %ss" % round(time() - start_time, 2))

    draw.largest(g.copy())
    draw.radial_highest(g.copy())
    draw.sfdp(g.copy())
    draw.grouped_sfdp(g.copy())
    draw.min_tree(g.copy())
    draw.radial_random(g.copy())
    draw.hierarchy(g.copy())
    draw.minimize_blockmodel(g.copy())
    draw.netscience(g.copy())
    draw.fruchterman(g.copy())

if __name__ == '__main__':

    p = argparse.ArgumentParser(
        description='Visualize collaboration of KTH scientists.')

    p.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

    args = p.parse_args()
    if args.verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")
    main()

