# Function to generate SQL query
def make_query(username, password):
    query = "SELECT * FROM users \nWHERE Username=" + "'" + username + "' AND Password=" + "'" + password + "';"
    print(query)
    return query

# Main
make_query("name", "wordpass")
