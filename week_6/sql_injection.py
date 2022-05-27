# Instructions
# 1.  Create a Query Generation

# 2. Generate a set of valid cases

# 3. Generate a set of invalid cases

# 4. write a weak mitigation function

# 5. write a strong mitigation function
# IMPORTANT TO NOTe, SQL ATTACK EXAMPLES WERE USED FROM:
#https://www.w3resource.com/sql/sql-injection/sql-injection.php
#https://www.greycampus.com/opencampus/ethical-hacking/types-of-sql-injection
#https://www.invicti.com/blog/web-security/sql-injection-cheat-sheet/#LineCommentAttacks


#imports
import platform
import re

# Function to generate SQL query
def make_query(username, password):
    query = (f"SELECT authenticate FROM users_details WHERE Username='{username}' AND Password='{password}';\n")
    print(query)
    return query

#valid tests
def jacob_valid_test():
    print("\nJacob's Valid test\n")
    print ("==========================================")
    test = ["A_b4d_u53rn4m3", "A_b4d_p455w0rd"]
    print(f"Jacob's test for a valid:\n Username: {test[0]}\n Password: {test[1]}")
    make_query(test[0], test[1])
    weak_mitigation_query(test[0], test[1])
    strong_mitigation_query(test[0], test[1])

def nathan_valid_test():
    print("\nNathan's Valid test\n")
    print ("==========================================")
    test = ["SuCh_4_G0od_l4d", "such_4_r4d_14d"]
    print(f"Nathan's test for a valid:\n Username: {test[0]}\n Password: {test[1]}")
    make_query(test[0], test[1])
    weak_mitigation_query(test[0], test[1])
    strong_mitigation_query(test[0], test[1])

def michael_valid_test():
    print("\nMichael's Valid test\n")
    print ("==========================================")
    test = ["n0rm41", "unusual"]
    print(f"Michael's test for a valid:\n Username: {test[0]}\n Password: {test[1]}")
    make_query(test[0], test[1])
    weak_mitigation_query(test[0], test[1])
    strong_mitigation_query(test[0], test[1])

#Vulnerabilities tests
def jacob_test():
    print ("Jacob's Test")
    print ("==========================================")

    #tautology attack
    username = "scrub"
    password = "anything or x=x"
    print(f"Tautology attack:\n Username: {username}\n Password: {password}")
    weak_mitigation_query(username, password)
    strong_mitigation_query(username, password)
    print ("==========================================")

    #union query attack
    username = "pass; UNION all Select * from users_details"
    password = "$whatascrub"
    print(f"Union attack:\n Username: {username}\n Password: {password}")
    weak_mitigation_query(username, password)
    strong_mitigation_query(username, password)
    print ("==========================================")

    #additional statement attack
    username = "~scrub"
    password = "; drop table xyz -- "
    print(f"Additional Statement attack:\n Username: {username}\n Password: {password}")
    weak_mitigation_query(username, password)
    strong_mitigation_query(username, password)
    print ("==========================================")

    #comment attack
    username = "admin'--"
    password = "@password"
    print(f"Comment attack:\n Username: {username}\n Password: {password}")
    weak_mitigation_query(username, password)
    strong_mitigation_query(username, password)
    print ("==========================================")


def nathan_test():
    print ("Nathan's Test")
    print ("==========================================")

    #tautology attack
    username = "bro"
    password = "pass or 1=1"
    print(f"Tautology attack:\n Username: {username}\n Password: {password}")
    weak_mitigation_query(username, password)
    strong_mitigation_query(username, password)
    print ("==========================================")

    #union query attack
    username = "dude"
    password = "UNION DROP TABLE users_details;"
    print(f"Union attack:\n Username: {username}\n Password: {password}")
    weak_mitigation_query(username, password)
    strong_mitigation_query(username, password)
    print ("==========================================")

    #additional statement attack
    username = ";UNION DROP TABLE users_details"
    password = "dudette"
    print(f"Additional Statement attack:\n Username: {username}\n Password: {password}")
    weak_mitigation_query(username, password)
    strong_mitigation_query(username, password)
    print ("==========================================")

    #comment attack
    username = "DROP users_details;#"
    password = "brosky"
    print(f"Comment attack:\n Username: {username}\n Password: {password}")
    weak_mitigation_query(username, password)
    strong_mitigation_query(username, password)
    print ("==========================================")



def michael_test():
    print ("Michael's Test")
    print ("==========================================")

    #tautology attack
    username = "shadowdemon"
    password = "pass or 1=1"
    print(f"Tautology attack:\n Username: {username}\n Password: {password}")
    weak_mitigation_query(username, password)
    strong_mitigation_query(username, password)
    print ("==========================================")

    #union query attack
    username = "shadow; UNION Select * FROM users_details"
    password = "disruption"
    print(f"Union attack:\n Username: {username}\n Password: {password}")
    weak_mitigation_query(username, password)
    strong_mitigation_query(username, password)
    print ("==========================================")

    #additional statement attack
    username = ";import os dir ='/table/password';shutil.rmtree(dir)"
    password = "shadowpoison"
    print(f"Additional Statement attack:\n Username: {username}\n Password: {password}")
    weak_mitigation_query(username, password)
    strong_mitigation_query(username, password)
    print ("==========================================")

    #comment attack
    username = "admin'#"
    password = "demonicpurge"
    print(f"Comment attack:\n Username: {username}\n Password: {password}")
    weak_mitigation_query(username, password)
    strong_mitigation_query(username, password)
    print ("==========================================")

#WEAK MITIGATION
# Perform weak levels of mitigation on the input
def weak_mitigation_query(username, password):
    # Check for keywords contained in username and password
    bad_char = ["UNION", "OR", "--", ";", "AND", "\"", "/", "$", "#", "@", "~","="]
    test = 1
    for i in bad_char:
        #checks if unput contains a invalid charecter
        if(i in username.upper() or i in password.upper()):
            print(f"\tInput recieved from {username} is invalid, the use of {i} is not permitted.")
            test = 0
    if test == 1:
        print("\tTest input has passed: " + make_query(username, password))



#STRONG MITIGATION
# Provide strong mitigation be checking length of username and password, and checking certain charecters.
def strong_mitigation_query(username, password):
    test = 1

    if not re.match("^[A-Za-z0-9_-]*$", username):
        print ("\tInvalid username, letters and numbers only are permitted.")
        test = 0
    
    elif len(username) > 20:
        print ("\tInvalid username, username must be 20 characters or less.")
        test = 0

    elif not re.match("^[A-Za-z0-9_-]*$", password):
        print ("\tInvalid password, Only letters and numbers allowed.")
        test = 0

    elif len(password) > 30:
        print ("\tInvalid password, password must be 30 characters or less.")
        test = 0

    if test == 1:
        print("\tTest input has passed: " + make_query(username, password))

def test_manually():
    username = get_username()
    password = get_password()

    weak_mitigation_query(username, password)
    strong_mitigation_query(username, password)

def teamates_tests():
    jacob_valid_test()
    nathan_valid_test()
    michael_valid_test()
    jacob_test()
    nathan_test()
    michael_test()
    print('\n')

# Extra manual option if desired
def get_username():
    print("Please enter your username: ")
    username = input("> ")
    return username

def get_password():
    print("Please enter your password:")
    password = input("> ")
    return password

# Main
def main_menu ():
    options = "menu"
    print("Welcome to the SQL_injection menu, for helping you verify if input is valid or not")
    print ("select an option to continue:")
    while options == "menu":
        print("Type 'manual' to manually test\n      Type 'team' to display homograph test cases \n       Type 'quit' to exit program")
        options = input("Option selected: ")
        if(options == "manual"):
            test_manually()
            options="menu"
        elif (options == "team"):
            teamates_tests()
            options = "menu"
        elif(options == "quit"):
            return
        else:
            options="menu"
            print("Please type in a valid input")
        
#main
main_menu()