from colorama import init, Fore, Back, Style
import json, sqlite3
from sqllitemanager.manager import SLite

init()
db = SLite(
    r"E:\Media\My Class\python\contact-project\json-file-database\db.sqllite3")

connection = sqlite3.connect(r'E:\Media\My Class\python\mftDB.sqlite3')

while True:
    userInput = input(
        "welcome to your contact book\n1- add contact\n2- search contact\n\n::please select an option: "
    )

    if userInput.lower() == "q":
        print("good bye ;)")
        break
    if userInput == "1":
        name = input("name: ")
        phone = input("phone: ")

        db.insert("CONTACTS", name=name, phone=phone)

        print("contact added successfully\n")
    elif userInput == "2":
        # give me what you want to search
        searchKeyWord = input("search: ")

        # initialize a matching list, this will contain the result
        matchingContacts = []

        # open the contacts file
        file = open(r".\contacts.json", "r")

        # iterate all lines to find the matching contact
        for contact in json.loads(file.read()):
            # make a list like this ['name', 'number'] and extract name and number
            try:
                # check if name matches
                if searchKeyWord.lower() in contact["name"].lower():
                    # append the result to matchingContacts list
                    matchingContacts.append(
                        [contact["name"], contact["phone"]])
            except Exception as ex:
                print(ex)

        if matchingContacts:
            for name, number in matchingContacts:
                print(Fore.RED + f"{name}\t\t{number}")
            print(Style.RESET_ALL)
            input("press enter to continue ...")
        else:
            print(Fore.RED + "no contact found :(")
            input("press enter ...")
            print(Style.RESET_ALL)
