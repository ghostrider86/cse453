# Function to generate SQL query
def make_query(username, password):
    query = "SELECT authenticate FROM users \nWHERE Username=" + "'" + username + "' AND Password=" + "'" + password + "';"
    print(query)
    return query

# Perform weak levels of mitigation on the input
def weak_mitigation_query(username, password):
    # Check for keywords contained in password
    # If keywords are found, split and keep everything before the split. 
    if "UNION" in password:
        password = password.split("UNION", 1)[0]
    if "OR" in password:
        password = password.split("OR", 1)[0]
    if "--" in password:
        password = password.split("--", 1)[0]
    if ";" in password:
        password = password.split(";", 1)[0]
    
    # Check for keywords contained in username
    # If keywords are found, split and keep everything before the split. 
    if "UNION" in username:
        username = username.split("UNION", 1)[0]
    if "OR" in username:
        username = username.split("OR", 1)[0]
    if "--" in username:
        username = username.split("--", 1)[0]
    if ";" in username:
        username = username.split(";", 1)[0]
    
    query = "SELECT authenticate FROM users \nWHERE Username=" + "'" + username + "' AND Password=" + "'" + password + "';"
    print(query)
    return query

def strong_mitigation_query(username, password):
    pass

# Main
make_query("name", "wordpass")
