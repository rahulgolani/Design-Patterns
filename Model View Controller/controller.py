# Controller interacts with model through the getAll() method which fetches all the records displayed to the end user.

from model import Person
import view

def showAll():
    peopleInDB=Person.getAll()
    return view.showAll(peopleInDB)

def start():
    view.startView()
    command=input('Press y to show all details\n')
    if command=='y':
        return showAll()
    else:
        return view.endView()

if __name__ == '__main__':
    start()
