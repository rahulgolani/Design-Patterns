class Singleton:

    __instance=None

    @staticmethod
    def getInstance():
        if Singleton.__instance==None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance==None:
            Singleton.__instance=self
        else:
            raise Exception("This is a Singleton class")

if __name__ == '__main__':
    s=Singleton.getInstance()
    print(s)
    s=Singleton.getInstance()
    print(s)
    s=Singleton.getInstance()
    print(s)
    # Here Exception is raised
    # s=Singleton()
    # print(s)
