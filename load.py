import parse
import sqlite3

# graph_db retrieves values from our database and parses the name field to
# make a relational graph based on the collaboration of researchers. The graph
# groups researchers based on wich faculty they belong to and weighs edges
# based on repeated collaborations.
def rows(db_path, query):
  # Connect to our database.
  conn = sqlite3.connect(db_path)
  with conn:
      # Recieve rows as associative arrays.
      conn.row_factory = sqlite3.Row
      # Database cursor to execute or SQL queries.
      cur = conn.cursor()
      cur.execute(query)
      return cur.fetchall()
  

# def graph_db(db_path, query):
#   # Create our undirected graph to return.
#   g = Graph(directed=False)
#   # The edge properties measuring collaboration.
#   e_times = g.new_edge_property("float")
#   # Grouping value for the verticies, verticies are in the same group if the
#   # have the same value.
#   v_groups = g.new_vertex_property("int")
#   # Color the verticies based on their faculties colors.
#   v_colors = g.new_vertex_property("vector<double>")

#   # Connect to our database.
#   conn = sqlite3.connect(db_path)
#   with conn:
#       # Recieve rows as associative arrays.
#       conn.row_factory = sqlite3.Row
#       # Database cursor to execute or SQL queries.
#       cur = conn.cursor()
#       cur.execute(query)
#       while True:
#           row = cur.fetchone()
#           if not row:
#               break
#           parse.row(row['name'].split(';'), row, g, e_times, v_colors, v_groups)
#   g.edge_properties["times"] = e_times
#   g.vertex_properties["colors"] = v_colors
#   g.vertex_properties["groups"] = v_groups
#   return g
