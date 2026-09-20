import os

def writing_input():
    while True:
        global code
        code = input("> ")
        proccesing_code()

def proccesing_code():
    if code.startswith("print("):
        print_code()

    elif "=" in code:
        variable_code()

    elif code == "":
        return

    elif code == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    
    else:
        print("Invalid code :-)")

def print_code():
        what_print = code.replace("print", "")
        what_print = what_print.replace("(", "")
        what_print = what_print.replace(")", "")

        if what_print.startswith('"') and what_print.endswith('"'):
            what_print = what_print.replace('"', "")
            print(what_print)

        else:
            if what_print in globals():
                print(globals()[what_print])

            else:
                error()

def variable_code():
    global name, value
    name, value = code.split("=", 1)

    if name.startswith(" "):
        name = name[1:]

    if value.startswith(" "):
        value = value[1:]

    if name.endswith(" "):
        name = name[:-1]

    if value.endswith(" "):
        value = value[:-1]

    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1]
        globals()[name] = value

    else:
        if value in globals():
            name = globals()[value]

        else:
            error()

def error():
    print("Something with your code is not correct. This program is not smart enough to tell you what")
                 

writing_input()
