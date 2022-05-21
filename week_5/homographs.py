# Instructions
# 1.  Create a canonicalization function to convert an encoding (the input path) into some canon.

# 2. Create a homograph function that determines if two file paths are the same.

# 3. Write a function to compare each of your non homograph test cases against 

# a forbidden file path to demonstrate that they are different (not homographs).

# 4. Write a function to compare each of your homograph test cases against 
# a forbidden file path to demonstrate that they are the same.

# 5. Demonstrate that all of the paths in "Non Homographs" are not homographs 
# and that all the paths in "Homographs" are in fact homographs. This will be done by writiing test cases

#imports
import platform

# user enters the file paths to compare
def test_input():
    print("Specify the first filename")
    file_path_1 = input(": ")
    
    print("Specify the second filename")
    file_path_2 = input(": ")
    test_homograph(file_path_1,file_path_2)

# cannonizes a file path provided
def canon_file(path):
    canon = []
    temporary = ''
    outcome = ''
    if(platform.system() == 'Windows'):
        slash = '\\'
    else:
        slash = '/'
    file_directory = path.split(slash)
    for x in file_directory:
        if(x == ".."):
            if(x != temporary):
                temporary = canon.pop()
        if(x != "." and x != ".."):
            canon.append(x)
    for x in range(len(canon)):
        outcome += f'{canon[x]}{slash}'
    print(outcome)
    return outcome

# Verifies if two files are homographs
def test_homograph(file_path_1, file_path_2):
    homograph = 0
    print("For:\t" + file_path_1 + "\t and\t" + file_path_2)
    if(canon_file(file_path_1) == canon_file(file_path_2)):
        homograph = 1
        print("The paths provided are Homographs\n")
    else:
        print("The paths provided are Not Homographs\n")
    return homograph


# various tests of Homograph paths
# Forbidden Path: /home/user/secret/password.txt

def homographs():
    forbiddenPath = "\\home\\user\\secret\\password.txt"
    test1 = "\\home\\..\\home\\..\\home\\user\\secret\\password.txt"
    test2 = "\\home\\user\\..\\..\\home\\user\\secret\\password.txt"
    test3 = "\\home\\user\\.\\secret\\password.txt"
    test4 = "\\home\\..\\home\\..\\home\\user\\.\\secret\\password.txt"
    test5 = "\\home\\..\\home\\..\\home\\user\\.\\.\\.\\.\\.\\..\\user\\secret\\password.txt"
    print ("==========================================")
    print("Homographs tests")

    #The following test cases verify if some file conditions are homographs

    #single back directory   
    print("Test 1 : " + test1)
    test_homograph(forbiddenPath, test1)
    #double back directory
    print("Test 2 : " + test2)
    test_homograph(forbiddenPath, test2)
    #current directory
    print("Test 3 : " + test3)
    test_homograph(forbiddenPath, test3)
    #back directory and current directory
    print("Test 4 : " + test4)
    test_homograph(forbiddenPath, test4)
    #back directory and current directory many times
    print("Test 5 : " + test5)
    test_homograph(forbiddenPath, test5)
    print ("==========================================")

# various tests of Non-Homograph paths
def non_Homographs():
    forbiddenPath = "\\home\\user\\secret\\password.txt"
    test_6 = "home\\user\\secret\\password.txt"
    test_7 = "\\home\\user\\..\\.\\secret\\password.txt"
    test_8 = "\\home\\..\\user\\secret\\password.txt"
    test_9 = "\\.\\password.txt"
    print ("==========================================")
    print("Non-Homographs tests")
    #The following test cases verify if some file conditions are not homographs

    #wrong path
    print("Test 6 : " + test_6)
    test_homograph(forbiddenPath, test_6)
    #The back directory and current directory
    print("Test 7 : " + test_7)
    test_homograph(forbiddenPath, test_7)
    #only use the back directory
    print("Test 8 : " + test_8)
    test_homograph(forbiddenPath, test_8)
    #only use the current directory
    print("Test 9 : " + test_9)
    test_homograph(forbiddenPath, test_9)
    print ("==========================================")

def main_menu ():
    options = "menu"
    print("Welcome to the Homograph menu, for helping you verify if file paths are Homographs")
    print ("select an option to continue:")
    while options == "menu":
        print("Type 'manual' to manually test paths\n      Type 'test1' to display homograph test cases \n      Type 'test2' to display non-homograph test cases\n      Type 'quit' to exit program")
        options = input("Option selected: ")
        if(options == "manual"):
            test_input()
            options="menu"
        elif (options == "test1"):
            homographs()
            options = "menu"
        elif (options == "test2"):
            non_Homographs()
            options = "menu"
        elif(options == "quit"):
            return
        else:
            options="menu"
            print("Please type in a valid input")
        
#main
main_menu()
