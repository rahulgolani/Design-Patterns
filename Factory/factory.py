class Button:
    html=""
    def getHtml(self):
        return self.html

class Image(Button):
    html="<img></img>"

class Input(Button):
    html="<input></input>"

class Form(Button):
    html="<form></form>"

class ButtonFactory():
    def createButton(self,typ):
        targetClass=typ.capitalize()
        # print(targetClass)
        # print(globals())
        return globals()[targetClass]()

# The locals() function returns a dictionary containing the variables defined in the local namespace. Calling locals() in the global namespace is same as calling globals() and returns a dictionary representing the global namespace of the module.

# The globals() function returns a dictionary containing the variables defined in the global namespace. When globals() is called from a function or method, it returns the dictionary representing the global namespace of the module where the function or method is defined, not from where it is called.

if __name__ == '__main__':
    buttonObj=ButtonFactory()
    buttons=['image','input','form']
    for i in buttons:
        print(buttonObj.createButton(i).getHtml())

# The button class helps to create the html tags and the associated html page. The client will not have access to the logic of code and the output represents the creation of html page.
