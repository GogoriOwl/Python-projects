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
        if verify(userEmail, "password", "register") == False:
            continue
        else:
            break
    
    userCommand = log_in().strip().lower()

    if userCommand == "projects":
        project_list = projects_search(projects, "names")

        if project_list == None:
            pass

        project_command = in_prject_menu()

        if project_command == "add project":
            add_project()









def verify(input, emailOrPass, logInOrReg):
    if emailOrPass == "email" and logInOrReg == "register":
        verif = re.search("[a-zA-Z]+[0-9]+@[aA-zZ]+", input) and input.endswith(".com")
        return verif

    elif emailOrPass == "pass" and logInOrReg == "register":
        verif = len(emailOrPass) >= 6
        print(verif)
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


def projects_search(projects, names_or_id):

    if names_or_id == "names":
        project_names = []

        if len(projects) == 0:
            return None

        else:
            for project in projects:
                project_names.append(project['title'])

        return project_names

    elif names_or_id[0] == "id":
        for project in projects:
            if project['id'] == names_or_id[1]:
                return project

            else: return None


def in_prject_menu():
    possible_commands = ["add project", "edit ptoject", "enter project", "sort projects", "filter projects"]

    print('''
    1.Add project
    2.Edit project
    3.Enter project
    4.Sort projects
    5.Filter projects
        ''')

    while True:
        user_command = input("Enter command: ")

        if user_command not in possible_commands:
            print("invalid command")
            continue
        else:
            return user_command


def add_project():
    

main()
