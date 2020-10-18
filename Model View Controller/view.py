# It displays all the records fetched within the model. View never interacts with model; controller does this work (communicating with model and view).

from model import Person

def showAll(list):
    # print(list)
    for person in list:
        print(person.name())

def startView():
    print("Starting View")

def endView():
    print("Ending View")
