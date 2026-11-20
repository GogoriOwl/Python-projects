import re


def main():
    projects = []

    userInput = input("Register or log in").lower().strip()

    while True:
        if userInput == "register":
            userEmail = input("Type your email: ")
            if verify(userEmail, "email", "register") == None:
                continue
            else:
                break

    while True:
        userPassword = input("Enter your password: ")
        if verify(userEmail, "password", "register") == None:
            continue
        else:
            break
    
    userCommand = log_in().strip().lower()
    if userCommand == "projects":
        projects_menu()






def verify(input, emailOrPass, logInOrReg):
    if emailOrPass == "email" and logInOrReg == "register":
        verif = re.search("[a-zA-Z]+[0-9]+?@[aA-zZ]+", input) and input.endswith(".com")
        return verif

    elif emailOrPass == "pass" and logInOrReg == "register":
        verif = re.search("[a-zA-Z]+[0-9]+?{8}", input) and input.endswith(".com")
        return verif



def log_in():
    possible_commands = ["projects", "tasks", "search", "filters", "repository info", "exit"]

    print('''
        ==== DEV TRACK ====

        1.Projects
        2.Tasks
        3.Search
        4.Filters
        5.Repository info
        6.exit
        ''')

    while True:
        user_command = input("comand: ")
        if user_command in possible_commands:
            break
        else: print("invalid command")



    return user_command


def projects_menu(projects, names_or_id):

    if names_or_id[0] == "names":
        project_names = []
        for project in projects:
            project_names.append(project['title'])

        return project_names

    elif names_or_id[0] == "id":
        for project in projects:
            if project['id'] == names_or_id[1]:
                return project

            else: return None



main()
