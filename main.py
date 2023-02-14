from gqlalchemy import Memgraph
# import mgp

# docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <Container_ID>

# Make a connection to the database
memgraph = Memgraph(host='172.18.0.2', port=3000)

# Build the query - get all diseases
query = """MATCH path=(n0:Disease)-[:ASSOCIATES_DaG]-(n1)-[:EXPRESSES_AeG]-(n2:Anatomy)
WHERE n0.name = 'hypertension'
RETURN *
LIMIT 25;"""

# Execute the query
# memgraph.execute(query)
results = memgraph.execute_and_fetch(query)

# Print the first member
print(list(results)[0]['result'])



